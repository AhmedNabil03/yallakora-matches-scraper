# YallaKora Match Scraper

YallaKora Match Scraper is a Python-based scraping project designed to extract football match data from the YallaKora website. Given a specific date, this tool retrieves match details, including teams, match times, championships, and results, and exports the data to an Excel file for further analysis.

## Features

- Retrieve football match data for any specified date.
- Extract key details:
  - Match result
  - Match time
  - Team names
  - Championship name
- Print the data as a pandas dataframe.
- Export scraped data into an Excel file for easy access and analysis.

## How It Works

1. The script prompts the user to input a date in the format `MM/DD/YYYY`.
2. It scrapes the YallaKora website for matches on the given date.
3. Extracted data includes:
   - Match results
   - Match times
   - Team names
   - Championship names
4. The data is displayed in a tabular format in the console, as well as saved as an Excel file.

## Output Example

![Output dataframe](/example.png)

## Requirements

- Required Libraries:
  - `pandas`
  - `requests`
  - `lxml`
  - `beautifulsoup4`

Install the required libraries using:

```bash
pip install pandas requests lxml beautifulsoup4
```
