import argparse
from papers import fetcher, filters, utils


def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", help="PubMed query string")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    ids = fetcher.fetch_pubmed_ids(args.query)
    xml_root = fetcher.fetch_paper_details(ids)

    papers = []
    for article in xml_root.findall(".//PubmedArticle"):
        paper_data = filters.extract_paper_info(article)
        if paper_data["Non-academic Author(s)"]:
            papers.append(paper_data)

    if args.file:
        utils.save_to_csv(args.file, papers)
        print(f"Saved {len(papers)} papers to {args.file}")
    else:
        for p in papers:
            print(p)


if __name__ == "__main__":
    main()