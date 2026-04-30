from crawlee.router import Router
from crawlee.crawlers import BeautifulSoupCrawlingContext
from loguru import logger

router = Router()

@router.default_handler
async def default_handler(context: BeautifulSoupCrawlingContext) -> None:
    """
    Default handler for all routes. Logs the URL of the page being crawled.
    Args:
        context (BeautifulSoupCrawlingContext): The crawling context containing the URL and other information.
    """
    logger.info(f"Processing URL: {context.request.url}")

    await context.enqueue_links(
        selector="a[href*='/product-detail/']", # product page links
        label="PRODUCT",
        unique=True
    )

@router.handler("PRODUCT")
async def product_handler(context: BeautifulSoupCrawlingContext) -> None:
    """
    Handler for product pages. Logs the URL of the product page being crawled.
    Args:
        context (BeautifulSoupCrawlingContext): The crawling context containing the URL and other information.
    """
    logger.info(f"Processing PRODUCT URL: {context.request.url}")

    data = {
        "url": context.request.url,
        "title": context.soup.title.string.strip() if context.soup.title else "Unknown"
    }

    await context.push_data(data)