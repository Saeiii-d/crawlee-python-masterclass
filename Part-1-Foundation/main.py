import sys
import asyncio
from loguru import logger
from crawlee.crawlers import BeautifulSoupCrawler
from routes import router

async def main():
    # setup logging
    log_filename = f"logs/crawler.log"
    logger.remove()

    logger.add(
        log_filename,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <blue>{name}</blue>:<blue>{function}</blue>:<blue>{line}</blue> - <level>{message}</level>",
        encoding="utf-8",
    )

    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <blue>{name}</blue>:<blue>{function}</blue>:<blue>{line}</blue> - <level>{message}</level>",
        level="INFO",
    )

    logger.level("asyncio", no=30) 
    logger.level("crawlee", no=20) 

    # Initialize the crawler with the router
    crawler = BeautifulSoupCrawler(
        request_handler=router,
        max_requests_per_crawl=50,
    )

    start_urls = [
        'https://www.mashadleather.com/product/MenBOOTS',
        ] 
    
    logger.info("Running crawler...")
    await crawler.run(start_urls)
    logger.info("Crawl completed. Data saved to ./storage/datasets/default")

if __name__ == '__main__':
    asyncio.run(main())