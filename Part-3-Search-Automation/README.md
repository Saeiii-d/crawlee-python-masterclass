# Web Crawling Series: Part 3 — Browser Automation with Playwright

[⬅️ Back to Main Series](../README.md)

In Part 3, we leave static HTML behind to tackle modern, JavaScript-heavy Single Page Applications (SPAs). Using Playwright, we simulate real browser interactions—typing into search bars, waiting for network idle states, and triggering infinite scroll events to unlock data that is otherwise invisible to traditional parsers.

## Key Engineering Challenges

- **Automated Search Interaction**: Programmatically identifying and filling search inputs to navigate marketplaces that don't use traditional category links.

- **Infinite Scroll Logic**: Implements a bounded loop that scrolls, waits for network activity, and monitors product counts to stop when no new items are loaded.

- **Deterministic Hashing**: A fallback SKU generation system using MD5 hashing on product URLs when a clear identifier cannot be extracted.

## Advanced Features

- **Browser-Like User-Agent**: Applies a desktop Chrome-style User-Agent to the browser page before performing the search interaction.

- **Dynamic Wait States**: Uses `wait_for_load_state("networkidle")` during scrolling to wait for network activity to settle before triggering the next interaction.

- **Persian Character Normalization**: A helper function to convert Persian digits and currency formatting into clean, storage-ready integers.

## Project Structure

```text
├── main.py          # Entry point: Initializes the crawler and logging
├── routes.py        # Logic Layer: Defines how different URLs are
└── README.md
```

## Key Takeaways

- **Interaction Over Navigation**: Sometimes data isn't at a URL; it's behind a button or a search query.
- **The Cost of JS**: While Playwright is powerful, it is significantly more resource-intensive than BeautifulSoup—use it strategically.
