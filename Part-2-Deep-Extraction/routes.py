from crawlee.router import Router
from crawlee.crawlers import BeautifulSoupCrawlingContext
from loguru import logger
from datetime import datetime
import hashlib

router = Router()

@router.default_handler
async def default_handler(context: BeautifulSoupCrawlingContext) -> None:
    """
    Default handler for all routes.
    """
    logger.info(f"Processing URL: {context.request.url}")

    try:
        await context.enqueue_links(
            selector="a[href*='/product-category/']", # category page links
            label="CATEGORY",
            unique=True
        )

    except Exception as e:
        logger.error(f"Error enqueuing category links: {e}")

@router.handler("CATEGORY")
async def category_handler(context: BeautifulSoupCrawlingContext) -> None:
    """
    Handler for category pages. Logs the URL of the category page being crawled.
    Args:
        context (BeautifulSoupCrawlingContext): The crawling context containing the URL and other information.
    """
    logger.info(f"Processing CATEGORY URL: {context.request.url}")

    try:
        await context.enqueue_links(
            selector="a[href*='/product/']", # product page links
            label="PRODUCT",
            unique=True
        )

        try:
            await context.enqueue_links(
                selector="a.next.page-number", # next page link
                label="CATEGORY",
            )

        except Exception as e:
            logger.error(f"Error enqueuing next page link: {e}")

    except Exception as e:
        logger.error(f"Error enqueuing product links: {e}")

@router.handler("PRODUCT")
async def product_handler(context: BeautifulSoupCrawlingContext) -> None:
    """
    Handler for product pages. Logs the URL of the product page being crawled.
    Args:
        context (BeautifulSoupCrawlingContext): The crawling context containing the URL and other information.
    """
    logger.info(f"Processing PRODUCT URL: {context.request.url}")

    soup = context.soup

    # Extract SKU
    sku_element = soup.select_one("span.sku")

    if sku_element and sku_element.text.strip() != "نامعلوم":
        sku = sku_element.text.strip()
    else:
        logger.warning(f"SKU not found for URL: {context.request.url}")

        # Create a fallback SKU using SHA‑1 hash of the URL cause some products have 'نامعلوم' as SKU
        url_hash = hashlib.sha1(context.request.url.encode("utf-8")).hexdigest()

        sku = f"{url_hash[:10].upper()}"

    # Extract colors and sizes
    colors = []
    sizes = []

    variant_rows = soup.select("table.variations div.vi-wpvs-variation-wrap-wrap")

    for row in variant_rows:
        attr_name = row.get("data-wpvs_attribute_name", "")

        options = row.select("div.vi-wpvs-option-wrap")

        values = []
        for opt in options:
            value = opt.get("data-attribute_value")
            label = opt.get("data-attribute_label")

            if value:
                values.append({
                    "value": value.strip(),
                    "label": label.strip() if label else value.strip()
                })

        if "color" in attr_name:
            colors = [v["label"] for v in values]
        else:
            sizes = [v["value"] for v in values]

    # Extract images
    image = ''
    image_element = soup.select_one("div.wvg-gallery-image img")
    if image_element:
        image = image_element.get("src", "")
    else:
        logger.warning(f"Image not found for URL: {context.request.url}")


    # Extract description
    description = ""
    desc_element = soup.select("div.woocommerce-Tabs-panel--description.panel p")
    if desc_element:
        description = "".join([p.text.strip() for p in desc_element])

    # Extract price
    price = None
    discount_price = None
    have_discount = bool(soup.select_one("p.price.product-page-price.price-on-sale"))
    if have_discount:
        price_element = soup.select_one("p.price.product-page-price del span.woocommerce-Price-amount.amount")
        discount_price_element = soup.select_one("p.price.product-page-price ins span.woocommerce-Price-amount.amount")

        if price_element:
            price = price_element.get_text(strip=True)
        else:
            logger.warning(f"Original price not found for URL: {context.request.url}")
            price = "Unknown"

        if discount_price_element:
            discount_price = discount_price_element.get_text(strip=True)
        else:
            logger.warning(f"Discount price not found for URL: {context.request.url}")
            discount_price = "Unknown"
    else:
        price_element = soup.select_one("p.price.product-page-price span.woocommerce-Price-amount.amount")
        if price_element:
            price = price_element.get_text(strip=True)
        else:
            logger.warning(f"Price not found for URL: {context.request.url}")
            price = "Unknown"  

    # Determine availability
    is_available = not bool(soup.select_one("p.stock.out-of-stock"))

    # Extract category
    category = []
    category_element = soup.select("span.posted_in a")
    if category_element:
        category = [cat.text.strip() for cat in category_element]
    else:
        logger.warning(f"Category not found for URL: {context.request.url}")
    
    data = {
        "sku": sku,
        "ts": str(datetime.utcnow()),
        "url": context.request.url,
        "title": context.soup.title.string.strip() if context.soup.title else "Unknown",
        "colors": colors,
        "sizes": sizes,
        "image": image,
        "description": description,
        "price": price,
        "discount_price": discount_price,
        "is_available": is_available,
        "category": category
    }

    await context.push_data(data)