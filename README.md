# Hacker News Scraper 🔎

A simple Python script that scrapes top news from [Hacker News](https://news.ycombinator.com/) and displays their titles, links, and points.

## Features

- Uses `requests` and `BeautifulSoup` to scrape data
- Collects post titles, URLs, and vote count
- Sorts posts by score
- Handles articles with missing votes

## How to Run

```bash
pip install requests beautifulsoup4
python hackernews_scraper.py
