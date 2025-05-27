# src/models/popularity.py

import pandas as pd

class PopularityRecommender:
    """
    A simple popularity-based recommender.
    Recommends globally most-listened-to songs.
    """

    def __init__(self):
        self.popularity_df = None

    def fit(self, df: pd.DataFrame):
        """Fit by computing global song popularity."""
        self.popularity_df = (
            df.groupby("song_id")["play_count"]
            .sum()
            .sort_values(ascending=False)
            .reset_index()
        )

    def recommend(self, top_k=10) -> pd.DataFrame:
        """Returns top-k most popular songs."""
        if self.popularity_df is None:
            raise ValueError("Model has not been fitted yet.")
        return self.popularity_df.head(top_k)
