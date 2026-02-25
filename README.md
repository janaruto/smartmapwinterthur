# SmartMapWinterthur

A small Streamlit dashboard project and companion notebooks for scraping and processing candidate answers from smartvote.ch for Winterthur elections.

## What this repository contains

- `app/` — the Streamlit app. Run `app/app.py` to start the dashboard.
- `notebooks/1_scrapper.ipynb` — a Selenium-based scraper (not part of the app requirements). Change the configuration there to scrape another city or candidate range.
- `notebooks/2_process.ipynb` — processing and transformation steps for scraped data. See it for details on how the raw CSV is converted/cleaned for the app.
- `data/` — sample data and outputs. The scraper writes to `data/raw/candidates_answers.csv` by default.
- `requirements.txt` — Python packages required to run the Streamlit app only.

## Quick start — Streamlit app

These commands assume you have Python 3.8+ and a working virtual environment.

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies for the Streamlit app:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run app/app.py
```

Notes:

- `requirements.txt` only contains the packages needed for the Streamlit dashboard (the app folder). It does NOT include the extra packages used for web-scraping.

## Web-scraping (not included in `requirements.txt`)

The scraping logic lives in `notebooks/1_scrapper.ipynb`. It uses Selenium and webdriver-manager and will require additional packages such as:

```text
selenium
webdriver-manager
pandas
```

If you want to run the scraper, install those packages into your environment (for example):

```bash
pip install selenium webdriver-manager pandas
```

Important configuration points for scraping a different city or range:

- The notebook builds a URL using a template like:

  `https://www.smartvote.ch/en/elections/26_st_winterthur_leg/candidacies/{candidateNumber}/answers`

  To target another city/election, update the path portion accordingly.

- Change the two integer variables at the top of the scraper notebook:

  - `candidateNumber` — the starting candidate id to process
  - `candidateEnd` — the (exclusive) end candidate id

Only these values (and the URL template if you target a different election/city) typically need to be changed to collect another dataset.

The scraper will append results to an in-notebook list `dfs` and (in the provided notebook) writes the final CSV to:

```
data/raw/candidates_answers.csv
```

## Processing scraped data

Open `notebooks/2_process.ipynb` to see the cleaning, feature extraction and aggregation steps applied to the raw CSV. Edit that notebook if you want to change the processing pipeline for another city or data layout.

## Pushing to GitHub

If you haven't already, create a repository on GitHub (for example `smartmapwinterthur`), add it as `origin`, and push your `main` branch:

```bash
git remote add origin https://github.com/<your-username>/smartmapwinterthur.git
git push -u origin main
```

## Safety and notes

- A local backup was recommended before removing old `.git` history (if you cloned a project). If you need the previous history, restore it from the backup you created.
- Scraping websites may be subject to the site's terms of service. Be respectful and throttle requests; the notebook contains small sleeps to avoid hammering the server.

## Contact / Next steps

If you want, I can:

- add a small `requirements-scraper.txt` listing the scraper dependencies;
- add a short example script to run the scraper headlessly;
- or wire CI to automatically run the processing notebook.

Tell me which of those (if any) you'd like and I will add it.
