# src/features.py

import pandas as pd

def filter_users_with_min_interactions(df: pd.DataFrame, min_interactions: int = 90) -> pd.DataFrame:
    """Filters out users with fewer than `min_interactions`."""
    return df.groupby("user_id").filter(lambda x: len(x) >= min_interactions)

def encode_ids(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes 'user_id' and 'song_id' into integer indices (for matrix factorization models).
    Adds 'user_idx' and 'song_idx' columns.
    """
    df = df.copy()
    df["user_idx"] = df["user_id"].astype("category").cat.codes
    df["song_idx"] = df["song_id"].astype("category").cat.codes
    return df

def apply_filters(df: pd.DataFrame, min_interactions: int = 90) -> pd.DataFrame:
    df = filter_users_with_min_interactions(df, min_interactions)
    # insert other filter here (later)
    return df