import pandas as pd

from src.etl.validator import validate_dataframe


def test_validate_dataframe_valid():
    df = pd.DataFrame({"A": [1, 2, 3]})
    assert validate_dataframe(df) is True


def test_validate_dataframe_empty():
    df = pd.DataFrame()
    assert validate_dataframe(df) is False


def test_validate_dataframe_none():
    assert validate_dataframe(None) is False


def test_validate_dataframe_multiple_columns():
    df = pd.DataFrame({
        "fund_name": ["Fund A", "Fund B"],
        "nav": [100.5, 105.2]
    })
    assert validate_dataframe(df) is True