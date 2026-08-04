# Resilient Web Crawling & Data Engineering Masterclass

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Crawlee](https://img.shields.io/badge/Powered%20by-Crawlee-green.svg)](https://crawlee.dev/)

This repository contains the source code for a four-part web crawling series. It demonstrates a progression from basic HTML extraction to modular routing, pagination, browser automation, and hybrid HTML/API data collection using Crawlee for Python.

## Series Roadmap

| Part | Focus                      | Key Technologies               | Project             | Repository                                                              |
| ---- | -------------------------- | ------------------------------ | ------------------- | ----------------------------------------------------------------------- |
| 01   | Static Parsing             | BeautifulSoup, Crawlee         | Basic Extractors    | Current                                                                 |
| 02   | Scaling & Routing          | Router Pattern, Request Queues | Multi-Page Scraping | Current                                                                 |
| 03   | Browser Automation         | Playwright, Infinite Scroll    | Torob Marketplace   | Current                                                                 |
| 04   | Hybrid HTML/API Extraction | Direct API Requests, AIOHTTP   | Mashhad Leather     | [View Part 4 Repo](https://github.com/Saeiii-d/mashhad-leather-crawler) |

## Part 1 & 2: Foundations & Scaling

The first two modules focus on the transition from simple scripts to organized architectures. We introduce the Router Pattern, allowing us to separate logic for homepages, category listings, and product details.

**Key Learning**: Handling pagination and deep-linking without spaghetti code.

**Deduplication**: Implementing unique keys to ensure we never scrape the same page twice.

## Part 3: Mastering the Dynamic Web (Torob)

Modern websites are often Single Page Applications (SPAs) that require a browser to "render" the data. This module tackles Torob, a JavaScript-heavy marketplace.

### Technical Highlights:

| Topic                 | Description                                                                          |
| --------------------- | ------------------------------------------------------------------------------------ |
| Browser Orchestration | Automating search bar interactions with Playwright, typing queries like a real user. |
| Infinite Scroll Logic | Custom scroll manager watching item counts & network idle to detect stagnation.      |

## Part 4: Hybrid HTML/API Extraction — Mashhad Leather

_Note: This project is hosted in a separate repository because it is a larger standalone example with its own dependencies and documentation._

While Part 3 uses Playwright, Part 4 intentionally pivots back to a Hybrid Approach to reduce browser-rendering overhead by requesting variant data directly from the site's internal endpoints.

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

Detailed breakdowns of the engineering logic behind these codes can be found on my Medium profile:

- **Part 1**: [stop writing scraping scripts start building data systems](https://medium.com/@saeiiid.khazaei/stop-writing-scraping-scripts-start-building-data-systems-02cf1a9e1c69)

- **Part 2**: [beyond the basics handling recursive pagination and deep extraction](https://medium.com/@saeiiid.khazaei/beyond-the-basics-handling-recursive-pagination-and-deep-extraction-45d57bb8dc87)

- **Part 3**: [teaching a crawler to think playwright infinite scroll and search automation](https://medium.com/@saeiiid.khazaei/teaching-a-crawler-to-think-playwright-infinite-scroll-and-search-automation-db594ffa9773)

- **Part 4**: [building a high performance hybrid web crawler with Direct API Requests](https://medium.com/@saeiiid.khazaei/building-a-high-performance-hybrid-web-crawler-with-api-interception-3d3e357da55b)

## Connect with me:

- _LinkedIn_: [Saeid Khazaei](https://www.linkedin.com/in/saeidkhazaei/)

- _GitHub_: [@Saeiii-d](https://github.com/Saeiii-d)
