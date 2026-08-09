# Web Crawling with Crawlee for Python: A Four-Part Series

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Crawlee](https://img.shields.io/badge/Powered%20by-Crawlee-green.svg)](https://crawlee.dev/)

This repository contains the source code for a four-part web crawling series built with Crawlee for Python. The series progresses from modular static crawling and structured product extraction to pagination, Playwright-based browser automation, and hybrid HTML/API data collection.

## Series Roadmap

| Part | Focus                              | Key Technologies                       | Project                 |
| ---- | ---------------------------------- | -------------------------------------- | ----------------------- |
| 01   | Modular Static Crawling            | Crawlee, BeautifulSoup, Router         | Basic Product Crawler   |
| 02   | Pagination & Structured Extraction | Crawlee, BeautifulSoup, Request Queues | Deep Product Extraction |
| 03   | Search & Infinite Scroll           | Crawlee, Playwright                    | Torob Marketplace       |
| 04   | Hybrid HTML/API Extraction         | Crawlee, BeautifulSoup, aiohttp        | Mashhad Leather         |

Part 4 is maintained as a [separate standalone repository](https://github.com/Saeiii-d/mashhad-leather-crawler) because it has its own dependencies and documentation.

## Part 1 & 2: Foundations & Scaling

The first two modules focus on the transition from simple scripts to organized architectures. We introduce the Router Pattern, allowing us to separate logic for homepages, category listings, and product details.

**Key Learning**: Handling pagination and deep-linking without spaghetti code.

**Request Deduplication**: Uses Crawlee's unique link enqueueing to reduce duplicate URL processing.

## Part 3: Browser Automation with Playwright

Some websites depend on JavaScript and browser interaction for important parts of their workflow. Part 3 uses Playwright to automate search, process dynamically updated results, trigger additional loading through scrolling, and extract structured product data from the rendered page.

### Technical Highlights:

| Topic                 | Description                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Search Automation     | Locates the search input, fills a predefined query, and submits it with Playwright.                                               |
| Infinite Scroll Logic | Scrolls the results page, waits for network activity to settle, and monitors product counts to stop when no new items are loaded. |

## Part 4: Hybrid HTML/API Extraction — Mashhad Leather

_Note: This project is hosted in a separate repository because it is a larger standalone example with its own dependencies and documentation._

While Part 3 uses Playwright, Part 4 intentionally pivots to a hybrid approach that reduces browser-rendering overhead by requesting variant data directly from the site's internal endpoints.

### Why Use a Hybrid Crawling Approach?

| Feature                  | Why It Matters                                                                     |
| ------------------------ | ---------------------------------------------------------------------------------- |
| Direct API Requests      | Retrieves variant data without rendering the complete user interface.              |
| Variant-Level Modeling   | Dataclasses represent colors, sizes, prices, and stock in a structured format.     |
| Reduced Browser Overhead | Avoiding browser rendering can reduce resource usage for supported data endpoints. |
| Logging and Monitoring   | Loguru and Rich provide readable logs and terminal progress information.           |

## Installation & Setup

1. Clone the Repository:

```Bash
git clone https://github.com/Saeiii-d/crawlee-python-masterclass.git
cd crawlee-python-masterclass

python -m venv .venv # On Windows: .venv\Scripts\Activate.ps1
```

2. Install dependencies:

```Bash
python -m pip install "crawlee[all]" loguru
playwright install
```

3. Run a Module:

```Bash
python Part-1-Foundation/main.py
python Part-2-Deep-Extraction/main.py
python Part-3-Search-Automation/main.py
```

## Articles & Tutorials

Detailed explanations of the design decisions, implementation details, and limitations of each part are available on Medium:

- **Part 1**: [From a Scraping Script to a Modular Web Crawler with Crawlee](https://medium.com/@saeiiid.khazaei/stop-writing-scraping-scripts-start-building-data-systems-02cf1a9e1c69)

- **Part 2**: [Adding Pagination and Structured Product Extraction to a Crawlee Project](https://medium.com/@saeiiid.khazaei/beyond-the-basics-handling-recursive-pagination-and-deep-extraction-45d57bb8dc87)

- **Part 3**: [Automating Search and Infinite Scroll with Crawlee and Playwright](https://medium.com/@saeiiid.khazaei/teaching-a-crawler-to-think-playwright-infinite-scroll-and-search-automation-db594ffa9773)

- **Part 4**: [Combining HTML Crawling with Direct API Requests for Product Variants](https://medium.com/@saeiiid.khazaei/building-a-high-performance-hybrid-web-crawler-with-api-interception-3d3e357da55b)

## Connect with me:

- _LinkedIn_: [Saeid Khazaei](https://www.linkedin.com/in/saeidkhazaei/)

- _GitHub_: [@Saeiii-d](https://github.com/Saeiii-d)
