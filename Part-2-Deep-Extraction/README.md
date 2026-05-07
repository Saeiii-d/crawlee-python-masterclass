# Resilient Web Crawling Series: Part 2 — Deep Extraction & Pagination

[⬅️ Back to Main Series](../README.md)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Crawlee](https://img.shields.io/badge/Powered%20by-Crawlee-green.svg)](https://crawlee.dev/)

Part 2 focuses on real-world resilience. We move beyond basic titles to extract full product schemas—including pricing, variants, and availability—while implementing automated navigation through paginated categories.

## Advanced Technical Features
   - **Recursive Pagination**: Automatically detects and enqueues "Next Page" links to ensure 100% coverage of category archives.
   - **Data Normalization & Fallbacks**: 
      *   Implements SHA-1 hashing via `hashlib` to generate deterministic SKUs when a target site provides "Unknown" or missing identifiers.
      *   Uses `datetime.utcnow()` to timestamp every record for production-ready data pipelines.
   - **Complex Attribute Parsing**: Extracts nested variant data (Colors and Sizes) from HTML tables by traversing structured div and table elements.
   - **Dynamic Sale Logic**: Distinguishes between original prices and discounted prices by detecting specific CSS classes like price-on-sale.
   - **Defensive Crawling**: Uses nested try-except blocks and `loguru` warnings to ensure the crawler continues running even if individual elements or links are missing.

## Project Structure
   ```text
   ├── main.py        # Entry point: Configured for bulk crawls (1000 requests)
   ├── routes.py      # Logic Layer: Detailed handlers for Discovery, Categories, and Products
   └── README.md       
   ```


## Key Takeaways from Part 2
* **State Management**: By labeling routes as `CATEGORY` and `PRODUCT`, we maintain a clean execution flow across thousands of URLs.

* **Data Integrity**: Using hashing for SKUs ensures that your dataset remains consistent even when the source website is missing primary keys or using localized placeholders like `"نامعلوم"`.

* **Observability**: Every extraction failure or missing field is logged with context using `loguru`, allowing for easy data quality audits after a massive crawl.