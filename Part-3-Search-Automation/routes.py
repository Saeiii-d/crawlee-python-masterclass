# part 3 routes.py
from crawlee.crawlers import PlaywrightCrawler, PlaywrightCrawlingContext
from crawlee.router import Router
from crawlee import Request
from loguru import logger
from urllib.parse import urlparse, parse_qs, urlunparse, urlencode
import re
import hashlib
from datetime import datetime

router = Router()

# Global state to ensure we only trigger the search interaction once
search_query_counter = 0

def clean_number(text: str) -> int:
    '''
    Helper to convert Persian digits and currency settings into integers.
    '''
    if not text:
        return 0
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    table = str.maketrans(persian_digits, english_digits)

    # Remove non-numeric characters and translate Persian to English digits
    cleaned = re.sub(r'[^\d۰-۹]', '', text).translate(table)
    return int(cleaned) if cleaned else 0

@router.default_handler
async def default_handler(context: PlaywrightCrawlingContext) -> None:
    '''
    Handles the initial landing page and search interaction.
    '''
    global search_query_counter

    # Setting a realistic User-Agent to avoid early detection
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    await context.page.set_extra_http_headers({"User-Agent": ua})

    if search_query_counter > 0:
        return

    logger.info(f"Processing URL: {context.request.url}")
    page = context.page
    query = "Iphone 17 Pro Max"

    # Automated Interaction: Finding the search bar and typing the query
    input_element = await page.query_selector("input[name='query']")
    if input_element:
        await input_element.fill(query)
        await input_element.press("Enter")
        
        # Explicit wait to allow dynamic search results to populate
        await page.wait_for_timeout(5000)

        logger.info(f"Search results loaded for <<{query}>>, enqueuing category page...")

        await context.add_requests([
            Request.from_url(url=page.url, label="CATEGORY", unique_key=page.url)
        ])
        search_query_counter += 1
    
    else:
        logger.warning("Search input element not found on the page.")


@router.handler("CATEGORY")
async def category_handler(context: PlaywrightCrawlingContext) -> None:
    '''
    Handles Infinite Scrolling to discover more product links.
    '''
    logger.info(f"Processing category URL: {context.request.url}")
    page = context.page

    # Initial link discovery
    try:
        await context.enqueue_links(
            selector="a[href*='/p/']", 
            label="PRODUCT",
            unique=True
        )
    except Exception as e:
        logger.error(f"Error enqueuing product links: {e}")

    logger.info("Starting pagination handling...")
    url = urlparse(context.request.url)
    query_params = parse_qs(url.query)
    current_page = int(query_params.get('page', ['1'])[0])

    scroll_attempt_cnt = 10
    current_count = len(await page.query_selector_all("a[href*='/p/']"))
    try:
        while current_page <= scroll_attempt_cnt:
            logger.info(f"Scrolling page {current_page}...")
            
            await context.page.wait_for_load_state("networkidle")

            # Use Playwright's scroll capability ti trigger JS-loading events  
            await context.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")
            await context.page.wait_for_timeout(5000) 

            new_count = len(await page.query_selector_all("a[href*='/p/']"))
            if new_count > current_count:
                logger.info(f"New products loaded: {new_count - current_count}")
                current_count = new_count
                await context.enqueue_links(
                    selector="a[href*='/p/']",
                    label="PRODUCT",
                    unique=True
                )
            else:
                logger.info("No new products loaded after scrolling.")
                break

            current_page += 1
            
        logger.info("Finished scrolling pages.")
    except Exception as e:
        logger.error(f"Error during handling scrolling: {e}")

@router.handler("PRODUCT")
async def product_handler(context: PlaywrightCrawlingContext) -> None:
    logger.info(f"Processing product URL: {context.request.url}")
    page = context.page

    # wait a few sec for loading page
    await context.page.wait_for_load_state("domcontentloaded")

    # SKU extraction
    sku = None
    sku_match = re.match(r".*/p/([^/]+)/?", context.request.url)
    if sku_match:
        sku = sku_match.group(1)
    else:
        logger.warning(f"SKU not found in URL: {context.request.url}")

        url_hash = hashlib.md5(context.request.url.encode()).hexdigest()
        sku = f"{url_hash[:10].upper()}"
    logger.info(f"Extracted SKU: {sku}")

    # Title extraction
    title = await page.query_selector("div[class*='Showcase_name'] h1")
    title_text = await title.text_content() if title else "No title found"
    logger.info(f"Extracted Title: {title_text}")

    # Price extraction
    price = None
    cheapest_seller = None
    is_available = True
    price_element = await page.query_selector_all("div[class*='Showcase_cheapest_seller'] div[class*='Showcase_buy_box_text']")
    if price_element:
        # check if it is available or not
        price_text = await price_element[1].text_content()
        if "ناموجود" in price_text:
            is_available = False
        
        cheapest_seller = (await price_element[0].text_content()).strip()
        cheapest_seller = cheapest_seller.replace("مشاهده در", '').replace("خرید از", '').strip()
        price = clean_number(price_text) if is_available else None
    
    # Used status
    is_used = False
    used_element = await page.query_selector("div[Showcase_main_info] div[class*='stock-status']")
    if (used_element):
        is_used = True

    # Image extraction
    image_urls = []
    image_elements = await page.query_selector_all("img[class*='ImageVideoSliderGallery_media']")
    for img in image_elements:
        src = await img.get_attribute("src")
        if src:
            image_urls.append(src)
    if not image_urls:
        image_elements = await page.query_selector_all("div[class*='imageGallery_cell__'] picture source")
        for img in image_elements:
            srcset = await img.get_attribute("srcset")
            if srcset:
                img_url = srcset.split(",")[-1]
                img_url = img_url.replace(" 2x", "").strip()
                image_urls.append(img_url)

    data = {
        "sku": sku,
        "url": context.request.url,
        "ts": datetime.utcnow(),
        "title": title_text,
        "is_available": is_available,
        "cheapest_price": price,
        "cheapest_seller": cheapest_seller,
        "used": bool(is_used),
        "images": image_urls,
    }

    await context.push_data(data)