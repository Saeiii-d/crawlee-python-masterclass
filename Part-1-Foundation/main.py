import sys
import asyncio
from loguru import logger
from crawlee.crawlers import BeautifulSoupCrawler
from routes import router

async def main():
    # setup logging
    logger.remove()
    logger.add(sys.stderr, format="<green>{time}</green> | <level>{level}</level>")

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