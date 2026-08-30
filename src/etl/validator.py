def validate_dataframe(df):
    if df is None:
        return False

    if df.empty:
        return False

    if len(df.columns) == 0:
        return False

    return True