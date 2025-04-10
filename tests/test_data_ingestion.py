# tests/test_data_ingestion.py
from src.data.data_ingestion import ingest_data
import pandas as pd

def test_ingest_data_returns_dataframe():
    df = ingest_data("tests/sample_weather.csv")
    assert isinstance(df, pd.DataFrame)
    assert "RainTomorrow" in df.columns
    assert df["RainTomorrow"].dropna().isin([0, 1]).all()