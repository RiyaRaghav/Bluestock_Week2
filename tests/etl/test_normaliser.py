import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[2] / "src" / "etl")
)


from normaliser import normalize_year, normalize_ticker


def test_normalize_year_integer():
    assert normalize_year(2025) == 2025


def test_normalize_year_string():
    assert normalize_year("2025") == 2025


def test_normalize_year_with_text():
    assert normalize_year("FY 2024") == 2024


def test_normalize_year_with_date():
    assert normalize_year("31-03-2023") == 2023


def test_normalize_year_invalid():
    assert normalize_year("Invalid") is None


def test_normalize_year_empty():
    assert normalize_year("") is None


def test_normalize_ticker_uppercase():
    assert normalize_ticker("reliance") == "RELIANCE"


def test_normalize_ticker_spaces():
    assert normalize_ticker(" RELIANCE ") == "RELIANCE"


def test_normalize_ticker_lowercase():
    assert normalize_ticker("tcs") == "TCS"


def test_normalize_ticker_internal_spaces():
    assert normalize_ticker("T C S") == "TCS"


def test_normalize_ticker_empty():
    assert normalize_ticker("") == ""


def test_normalize_ticker_none():
    assert normalize_ticker(None) is None