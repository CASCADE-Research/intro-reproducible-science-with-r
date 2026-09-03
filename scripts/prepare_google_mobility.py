#!/usr/bin/env python3
"""Create a compact, state-level snapshot of Google Community Mobility data."""

import csv
import sys
import urllib.request
from pathlib import Path


YEARS = (2020, 2021, 2022)
URL = "https://www.gstatic.com/covid19/mobility/{year}_US_Region_Mobility_Report.csv"
FIELDS = (
    "country_region_code",
    "country_region",
    "sub_region_1",
    "date",
    "retail_and_recreation_percent_change_from_baseline",
    "grocery_and_pharmacy_percent_change_from_baseline",
    "parks_percent_change_from_baseline",
    "transit_stations_percent_change_from_baseline",
    "workplaces_percent_change_from_baseline",
    "residential_percent_change_from_baseline",
)


def main() -> None:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "data/google-mobility-us-states.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    rows_written = 0

    with output.open("w", encoding="utf-8", newline="") as destination:
        writer = csv.DictWriter(destination, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()

        for year in YEARS:
            source_url = URL.format(year=year)
            print(f"Reading {source_url}", file=sys.stderr)
            with urllib.request.urlopen(source_url) as response:
                lines = (line.decode("utf-8") for line in response)
                for row in csv.DictReader(lines):
                    # Retain state totals; exclude the national total and county rows.
                    if row["sub_region_1"] and not row["sub_region_2"]:
                        writer.writerow({field: row[field] for field in FIELDS})
                        rows_written += 1

    print(f"Wrote {rows_written:,} rows to {output}", file=sys.stderr)


if __name__ == "__main__":
    main()
