"""Rebuild working-data-tables/eci-scores.csv from one download of Epoch's ECI file.

Usage:
    python scripts/build_eci_scores.py path/to/eci_scores.csv YYYY-MM-DD

Get the input from https://epoch.ai/data/eci_scores.csv (or the copy inside
https://epoch.ai/data/benchmark_data.zip). The second argument is the download date.

Output: one row for every model that raised its own lab's best score, for the labs
listed in LABS. `Is_Frontier` marks rows that also raised the best score of any lab.
Everything comes from the single input file, so the table never mixes Epoch vintages.
"""
import sys
from pathlib import Path

import pandas as pd

LABS = {
    "OpenAI": "OpenAI",
    "Anthropic": "Anthropic",
    "Google DeepMind": "Google",
    "Google": "Google",
    "Google DeepMind,Google": "Google",
    "xAI": "xAI",
    "Meta AI": "Meta",
    "Microsoft": "Microsoft",
    "Microsoft Research": "Microsoft",
    "DeepSeek": "DeepSeek",
    "Moonshot": "Moonshot",
    "Z.ai (Zhipu AI)": "Z.ai",
    "Alibaba": "Alibaba",
}
START = "2023-03-01"
SOURCE = "https://epoch.ai/data/eci_scores.csv"


def main(src: str, download_date: str) -> None:
    d = pd.read_csv(src).dropna(subset=["eci", "date"])
    d = d[d["date"] >= START].sort_values(["date", "eci"])

    d["frontier_before"] = d["eci"].cummax().shift(fill_value=float("-inf"))
    frontier_models = set(d.loc[d["eci"] > d["frontier_before"], "Model"])

    d = d[d["Organization"].isin(LABS)].copy()
    d["Org"] = d["Organization"].map(LABS)
    d["lab_before"] = d.groupby("Org")["eci"].transform(
        lambda s: s.cummax().shift(fill_value=float("-inf"))
    )
    d = d[d["eci"] > d["lab_before"]]

    out = pd.DataFrame(
        {
            "Date": d["date"],
            "Model": d["Display name"].fillna(d["Model"]),
            "Org": d["Org"],
            "Weights": d["Accessibility group"].str.replace(" weights", "", regex=False),
            "Access_Detail": d["Model accessibility"],
            "ECI": d["eci"].round(2),
            "CI_lo": d["eci_ci_low"].round(2),
            "CI_hi": d["eci_ci_high"].round(2),
            "Is_Frontier": d["Model"].isin(frontier_models).map({True: "yes", False: "no"}),
            "Vintage": f"Epoch download {download_date}",
            "Source": SOURCE,
        }
    )
    dest = Path(__file__).resolve().parent.parent / "working-data-tables" / "eci-scores.csv"
    out.to_csv(dest, index=False)
    print(f"wrote {len(out)} rows to {dest}")
    print(out.groupby("Org").agg(rows=("ECI", "size"), best=("ECI", "max")).sort_values("best"))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
