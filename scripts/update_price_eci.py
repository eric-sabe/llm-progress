"""Fill the ECI column of working-data-tables/model-prices.csv from Epoch's file.

Usage:
    python scripts/update_price_eci.py path/to/eci_scores.csv

Each row of model-prices.csv names its Epoch model in `Epoch_Name` (blank when Epoch
has not scored it). Prices themselves are maintained by hand from provider pricing
pages; this script only refreshes the index scores so they share one Epoch vintage
with eci-scores.csv.
"""
import sys
from pathlib import Path

import pandas as pd


def main(src: str) -> None:
    eci = pd.read_csv(src).set_index("Model")["eci"]
    dest = Path(__file__).resolve().parent.parent / "working-data-tables" / "model-prices.csv"
    p = pd.read_csv(dest)
    named = p["Epoch_Name"].notna()
    missing = sorted(set(p.loc[named, "Epoch_Name"]) - set(eci.index))
    if missing:
        sys.exit(f"Epoch_Name not found in {src}: {missing}")
    p["ECI"] = p["Epoch_Name"].map(eci).round(2)
    p.to_csv(dest, index=False)
    print(f"{named.sum()} of {len(p)} rows have an index score")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
