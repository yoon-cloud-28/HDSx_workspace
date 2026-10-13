from pathlib import Path
import pandas as pd


def load_and_preview(path, n_rows=5):
    """Load a CSV, print its shape, and return the first rows."""
    csv_path = Path(path)
    if not csv_path.exists():
        raise FileNotFoundError(f"Could not find file: {csv_path}")

    data = pd.read_csv(csv_path)
    print(f"Loaded {data.shape[0]} rows and {data.shape[1]} columns")
    return data.head(n_rows)


def summarise_mean_sd(data, value, group1, group2):
    """Summarise a value column by two grouping columns; pass column names as strings."""
    columns = [value, group1, group2]
    return (
        data.dropna(subset=columns)
        .groupby([group1, group2], as_index=False, sort=True)
        .agg(
            n=(value, "size"),
            mean_value=(value, "mean"),
            sd_value=(value, "std"),
        )
        .assign(
            mean_value=lambda summary: summary["mean_value"].round(2),
            sd_value=lambda summary: summary["sd_value"].round(2),
        )
    )