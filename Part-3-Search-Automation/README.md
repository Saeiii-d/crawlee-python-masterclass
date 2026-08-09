# Web Crawling Series: Part 3 — Browser Automation with Playwright

[⬅️ Back to Main Series](../README.md)

In Part 3, we leave static HTML behind to tackle modern, JavaScript-heavy Single Page Applications (SPAs). Using Playwright, we simulate real browser interactions—typing into search bars, waiting for network idle states, and triggering infinite scroll events to unlock data that is otherwise invisible to traditional parsers.

## Key Engineering Challenges

- **Automated Search Interaction**: Programmatically identifying and filling search inputs to navigate marketplaces that don't use traditional category links.

- **Infinite Scroll Logic**: Implementing a robust while loop that scrolls, waits for network idle states, and monitors item counts to prevent "stagnation" and infinite loops.

- **Deterministic Hashing**: A fallback SKU generation system using MD5 hashing on product URLs when a clear identifier cannot be extracted.

## Advanced Features

- **Human-Like Headers**: Applies a browser-like User-Agent to subsequent page requests.

- **Dynamic Wait States**: Utilizing wait_for_load_state("`networkidle`") to ensure asynchronous content is fully rendered before extraction begins.

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
