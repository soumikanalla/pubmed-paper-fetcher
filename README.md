# PubMed Paper Fetcher

CLI tool to fetch PubMed papers with at least one non-academic author affiliated with a biotech or pharmaceutical company.

## Features

- Accepts PubMed query as CLI input.
- Identifies non-academic authors using affiliation heuristics.
- Exports results to CSV or prints to console.
- Uses Poetry for packaging.

## Setup
```bash
git clone https://github.com/soumikanalla/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher
poetry install

## Usage
poetry run get-papers-list "cancer immunotherapy" -f output.csv
