from pathlib import Path
import pandas as pd

from normaliser import normalize_year, normalize_ticker


BASE_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = BASE_DIR / "data"
PROCESSED_DIR = DATA_DIR / "processed"


def load_csv(file_path):
    return pd.read_csv(file_path)


def normalize_dataframe(df):
    df = df.copy()

    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    if "ticker" in df.columns:
        df["ticker"] = df["ticker"].apply(normalize_ticker)

    return df


def save_processed(df, filename):
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    output_path = PROCESSED_DIR / filename
    df.to_csv(output_path, index=False)

    return output_path


def process_file(file_path):
    print(f"Loading: {file_path.name}")

    df = load_csv(file_path)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")

    df = normalize_dataframe(df)

    output_path = save_processed(
        df,
        f"{file_path.stem}_cleaned.csv"
    )

    print(f"Saved: {output_path.name}")
    print("-" * 50)


if __name__ == "__main__":

    print("Data directory:", DATA_DIR)
    print("Processed data directory:", PROCESSED_DIR)

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    files = list(DATA_DIR.glob("*.csv"))

    print(f"CSV files found: {len(files)}")
    print("=" * 50)

    for file in files:
        process_file(file)

    print("Data loading and normalization completed.")