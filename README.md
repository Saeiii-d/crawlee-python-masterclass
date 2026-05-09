# Resilient Web Crawling & Data Engineering Masterclass

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Crawlee](https://img.shields.io/badge/Powered%20by-Crawlee-green.svg)](https://crawlee.dev/)

Welcome to the complete source code for my web crawling series. This repository documents a journey from basic HTML parsing to building industrial-scale, production-ready data pipelines. Throughout this series, we utilize the Crawlee for Python framework to build modular, maintainable, and highly efficient crawlers.

## Series Roadmap
| Part | Focus                  | Key Technologies                           | Project                | Repository            |
|------|------------------------|---------------------------------------------|------------------------|------------------------|
| 01   | Static Parsing         | BeautifulSoup, Crawlee                      | Basic Extractors       | Current                |
| 02   | Scaling & Routing      | Router Pattern, Request Queues              | Multi-Page Scraping    | Current                |
| 03   | Browser Automation     | Playwright, Infinite Scroll                 | Torob Marketplace      | Current                |
| 04   | Industrial Hybrid      | API Interception, AIOHTTP                   | Mashhad Leather        | [View Part 4 Repo](https://github.com/Saeiii-d/mashhad-leather-crawler)     |


## Part 1 & 2: Foundations & Scaling
The first two modules focus on the transition from simple scripts to organized architectures. We introduce the Router Pattern, allowing us to separate logic for homepages, category listings, and product details.

**Key Learning**: Handling pagination and deep-linking without spaghetti code.

**Deduplication**: Implementing unique keys to ensure we never scrape the same page twice.

## Part 3: Mastering the Dynamic Web (Torob)
Modern websites are often Single Page Applications (SPAs) that require a browser to "render" the data. This module tackles Torob, a JavaScript-heavy marketplace.

### Technical Highlights:
| Topic                   | Description |
|-------------------------|-------------|
| Browser Orchestration   | Automating search bar interactions with Playwright, typing queries like a real user. |
| Infinite Scroll Logic   | Custom scroll manager watching item counts & network idle to detect stagnation. |


## Part 4: The Capstone — High-Performance Hybrid (Mashhad Leather)
*Note: This project is hosted in its own repository due to its complexity and industrial-grade architecture.*

While Part 3 uses Playwright, Part 4 intentionally pivots back to a Hybrid Approach for 10-20x higher performance.

### Why this is "The Best Possible" Crawler:
| Feature                  | Why It Matters |
|--------------------------|----------------|
| API Interception         | Skip UI rendering and talk directly to internal endpoints for huge speed gains. |
| Variant‑Level Modeling   | Dataclasses model Colors, Sizes, and live Stock with clarity and accuracy. |
| Speed & Efficiency       | No more Playwright bottlenecks → ultra‑fast crawling with minimal RAM. |
| Production Observability | Loguru + Rich enable clean logs, clear dashboards, and debuggable pipelines. |


## Installation & Setup
1. Clone the Repository:

```Bash
git clone https://github.com/Saeiii-d/crawlee-python-masterclass.git
cd crawl_series
```

2. Install dependencies:
```Bash
pip install crawlee[all] aiohttp loguru rich hashlib
```

```Bash
playwright install chromium
```

3. Run a Module:
```Bash
python main.py
```

## Articles & Tutorials
Detailed breakdowns of the engineering logic behind these codes can be found on my Medium profile:

* **Part 1**: [stop writing scraping scripts start building data systems](https://medium.com/@saeiiid.khazaei/stop-writing-scraping-scripts-start-building-data-systems-02cf1a9e1c69)

* **Part 2**: [beyond the basics handling recursive pagination and deep extraction](https://medium.com/@saeiiid.khazaei/beyond-the-basics-handling-recursive-pagination-and-deep-extraction-45d57bb8dc87)

* **Part 3**: [teaching a crawler to think playwright infinite scroll and search automation](https://medium.com/@saeiiid.khazaei/teaching-a-crawler-to-think-playwright-infinite-scroll-and-search-automation-db594ffa9773)

* **Part 4**: []()

## Connect with me:

* *LinkedIn*: [Saeid Khazaei](https://www.linkedin.com/in/saeidkhazaei/)

* *GitHub*: [@Saeiii-d](https://github.com/Saeiii-d)
