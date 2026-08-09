# Resilient Web Crawling Series: Part 2 — Deep Extraction & Pagination

[⬅️ Back to Main Series](../README.md)

Part 2 focuses on real-world resilience. We move beyond basic titles to extract full product schemas—including pricing, variants, and availability—while implementing automated navigation through paginated categories.

## Advanced Technical Features

- **Recursive Pagination**: Automatically detects and enqueues "Next Page" links to traverse paginated category archives.
- **Data Normalization & Fallbacks**:
  - Implements SHA-1 hashing via `hashlib` to generate deterministic SKUs when a target site provides "Unknown" or missing identifiers.
  - Uses `datetime.utcnow()` to timestamp every record for production-ready data pipelines.
- **Complex Attribute Parsing**: Extracts nested variant data (Colors and Sizes) from HTML tables by traversing structured div and table elements.
- **Dynamic Sale Logic**: Distinguishes between original prices and discounted prices by detecting specific CSS classes like price-on-sale.
- **Defensive Crawling**: Uses localized exception handling for link enqueueing and explicit fallbacks and `loguru` warnings for missing product fields.

## Project Structure

```text
├── main.py        # Entry point: Configured for bulk crawls (1000 requests)
├── routes.py      # Logic Layer: Detailed handlers for Discovery, Categories, and Products
└── README.md
```

## Key Takeaways from Part 2

- **State Management**: By labeling routes as `CATEGORY` and `PRODUCT`, we maintain a clean execution flow across many URLs.

- **Data Integrity**: Using hashing for SKUs ensures that your dataset remains consistent even when the source website is missing primary keys or using localized placeholders like `"نامعلوم"`.

- **Observability**: Important extraction issues and missing fields are logged with URL context using `loguru`, making crawl behavior and data-quality problems easier to inspect.
