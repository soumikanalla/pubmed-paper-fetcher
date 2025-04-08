import csv
from typing import List, Dict


def save_to_csv(filename: str, data: List[Dict]) -> None:
    if not data:
        return
    with open(filename, mode="w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)