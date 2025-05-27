# tests/test_features.py

import pandas as pd
from src import data_loader, features

def test_filter_users_with_min_interactions():
    df = data_loader.load_preprocessed_data()
    filtered = features.filter_users_with_min_interactions(df, min_interactions=3)
    assert "user_id" in filtered.columns
    assert all(filtered.groupby("user_id").size() >= 3)

def test_encode_ids():
    df = data_loader.load_preprocessed_data()
    df_encoded = features.encode_ids(df)
    assert "user_idx" in df_encoded.columns
    assert "song_idx" in df_encoded.columns
    assert df_encoded["user_idx"].dtype == "int32" or "int64"
