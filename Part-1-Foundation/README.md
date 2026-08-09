# Resilient Web Crawling Series: Part 1 - Building a Modular Crawlee Architecture

[⬅️ Back to Main Series](../README.md)

In this module, we implement a decoupled crawling architecture. Instead of a single monolithic script, we use a Router-based approach to handle different page types (Listings vs. Products) with unique logic for each.

## Technical Features

- **Decoupled Routing**: Uses the Router class to manage state and logic flow between listing/category pages and product detail pages.

- **Asynchronous Processing**: Built on Python’s `asyncio` for high-performance, non-blocking network I/O.

- **Structured Logging**: Implements `loguru` for professional-grade observability and debugging.

- **Automatic Storage**: Leverages Crawlee’s internal Dataset storage to automatically save `JSON` results to `./storage`.

## Project Structure

```text
├── main.py          # Entry point: Initializes the crawler and logging
├── routes.py        # Logic Layer: Defines how different URLs are
└── README.md
```

## Key Takeaways from Part 1

- **Separation of Concerns**: By defining a `default_handler` for discovery and a `PRODUCT` handler for extraction, the code remains clean and maintainable.
- **Link Enqueueing**: Demonstrated the use of CSS selectors to filter and enqueue relevant links while ensuring uniqueness to prevent infinite loops.
