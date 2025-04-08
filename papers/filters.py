from typing import List, Tuple
from xml.etree.ElementTree import Element


def is_non_academic(affiliation: str) -> bool:
    keywords = ["inc", "ltd", "gmbh", "corp", "biotech", "pharma", "therapeutics"]
    academic_indicators = ["university", "institute", "school", "college", "hospital", "center", "centre"]
    aff_lower = affiliation.lower()
    return any(k in aff_lower for k in keywords) and not any(a in aff_lower for a in academic_indicators)


def extract_paper_info(paper_element: Element) -> dict:
    paper_info = {
        "PubmedID": "",
        "Title": "",
        "Publication Date": "",
        "Non-academic Author(s)": [],
        "Company Affiliation(s)": [],
        "Corresponding Author Email": "",
    }

    paper_info["PubmedID"] = paper_element.findtext(".//PMID")
    paper_info["Title"] = paper_element.findtext(".//ArticleTitle")
    paper_info["Publication Date"] = paper_element.findtext(".//PubDate/Year") or "Unknown"

    affiliations = set()
    non_academic_authors = []

    for author in paper_element.findall(".//Author"):
        name = (author.findtext("ForeName") or "") + " " + (author.findtext("LastName") or "")
        for aff in author.findall(".//AffiliationInfo/Affiliation"):
            if is_non_academic(aff.text or ""):
                non_academic_authors.append(name.strip())
                affiliations.add(aff.text)

    paper_info["Non-academic Author(s)"] = list(set(non_academic_authors))
    paper_info["Company Affiliation(s)"] = list(affiliations)

    # Extract corresponding email
    for aff in paper_element.findall(".//AffiliationInfo/Affiliation"):
        if "@" in aff.text:
            paper_info["Corresponding Author Email"] = aff.text.split()[-1]
            break

    return paper_info