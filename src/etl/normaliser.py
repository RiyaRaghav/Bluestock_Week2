import re
import pandas as pd


def normalize_year(value):
    if pd.isna(value):
        return None

    value = str(value).strip()

    match = re.search(r"(19|20)\d{2}", value)

    if match:
        return int(match.group())

    return None


def normalize_ticker(value):
    if pd.isna(value):
        return None

    value = str(value).strip().upper()
    value = re.sub(r"\s+", "", value)

    return value