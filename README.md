# News Headline Scraper

This Python script scrapes the top news headlines from the BBC News website using the `requests` and `BeautifulSoup` libraries. It extracts the content of `<h2>` and `<h3>` tags and stores the headlines in a `.txt` file.

## Tools & Libraries

* Python 3
* `requests`
* `beautifulsoup4`

## Files Included

* `headlines.py` – Python script that performs web scraping
* `headlines.txt` – Output file with the list of scraped headlines

## How to Run

1. Install dependencies:

   ```bash
   pip install requests beautifulsoup4
   ```

2. Run the script:

   ```bash
   python headlines.py
   ```

3. Check the Output:

   * The extracted headlines will be saved in `headlines.txt`.

## Notes

* The script currently scrapes from [BBC News](https://www.bbc.com/news).
* change the URL or modify the tag list (e.g., `['h2', 'h3']`) to adapt the scraper to other news websites.

