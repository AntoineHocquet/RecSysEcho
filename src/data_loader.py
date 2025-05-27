# src/data_loader.py

import pandas as pd
from pathlib import Path

DATA_DIR = Path("data/sample")

def load_song_data():
    """Loads the song metadata from CSV."""
    return pd.read_csv(DATA_DIR / "song_data.csv")

def load_count_data():
    """Loads the user-song count data from CSV."""
    return pd.read_csv(DATA_DIR / "count_data.csv")

def merge_datasets(song_df: pd.DataFrame, count_df: pd.DataFrame) -> pd.DataFrame:
    """Merges song and count data on 'song_id'."""
    df = pd.merge(count_df, song_df, on="song_id")
    return df

def load_preprocessed_data() -> pd.DataFrame:
    """
    Loads and merges both datasets into a single DataFrame.
    Returns the full dataset for model input.
    """
    song_df = load_song_data()
    count_df = load_count_data()
    df = merge_datasets(song_df, count_df)

    # Optional cleanup: drop NAs, filter bad values, etc.
    df.dropna(inplace=True)
    return df
