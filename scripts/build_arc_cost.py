"""Rebuild working-data-tables/arc-cost-per-task.csv from ARC Prize's data files.

Usage:
    python scripts/build_arc_cost.py evaluations.json models.json YYYY-MM-DD

Inputs: https://arcprize.org/media/data/leaderboard/evaluations.json and
https://arcprize.org/media/data/models.json . The third argument is the download date.

Output: one row per verified ARC-AGI-2 run (semi-private set) that reports a cost per
task, for the labs in LABS. ARC Prize runs these itself, so the cost is what the run
actually cost at list prices, including reasoning tokens, not a price per token.
"""
import json
import sys
from pathlib import Path

import pandas as pd

LABS = {
    "OpenAI": "OpenAI", "Anthropic": "Anthropic", "Google": "Google", "xAI": "xAI",
    "Meta AI": "Meta", "Meta": "Meta", "DeepSeek": "DeepSeek", "Moonshot AI": "Moonshot",
    "Z.ai": "Z.ai", "Alibaba": "Alibaba",
}
DATASET = "v2_Semi_Private"
SOURCE = "https://arcprize.org/media/data/leaderboard/evaluations.json"


def main(evals_path: str, models_path: str, download_date: str) -> None:
    evals = json.load(open(evals_path))
    models = {m["id"]: m for m in json.load(open(models_path))}
    rows = []
    for e in evals:
        m = models.get(e["modelId"])
        if e["datasetId"] != DATASET or not e.get("display") or not m:
            continue
        if m.get("providerId") not in LABS or not e.get("costPerTask") or not m.get("modelReleaseDate"):
            continue
        rows.append(
            dict(
                Date=m["modelReleaseDate"][:10],
                Config=m["displayName"],
                Model_Group=m.get("modelGroup") or m["displayName"],
                Org=LABS[m["providerId"]],
                ARC_AGI_2=round(e["score"] * 100, 1),
                Cost_per_task_usd=round(e["costPerTask"], 4),
                Retrieved=download_date,
                Source=SOURCE,
            )
        )
    out = pd.DataFrame(rows).sort_values(["Date", "Org", "Cost_per_task_usd"])
    dest = Path(__file__).resolve().parent.parent / "working-data-tables" / "arc-cost-per-task.csv"
    out.to_csv(dest, index=False)
    print(f"wrote {len(out)} rows to {dest}")
    print(out.groupby("Org").size())


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
