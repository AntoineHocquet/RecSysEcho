# src/models/item_cf.py

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class ItemBasedCFRecommender:
    """
    Item-Based Collaborative Filtering using cosine similarity.
    """

    def __init__(self):
        self.user_item_matrix = None
        self.song_similarity = None
        self.song_id_map = None
        self.song_id_reverse_map = None

    def fit(self, df: pd.DataFrame):
        """
        Build the user-item matrix and compute item-item similarity.
        """
        # Map song_id to numerical indices
        song_idx = df["song_id"].astype("category").cat.codes
        df["song_idx"] = song_idx
        self.song_id_map = dict(enumerate(df["song_id"].astype("category").cat.categories))
        self.song_id_reverse_map = {v: k for k, v in self.song_id_map.items()}

        user_item = df.pivot_table(index="user_id", columns="song_idx", values="play_count", fill_value=0)
        self.user_item_matrix = user_item

        # Compute item-item similarity matrix
        self.song_similarity = cosine_similarity(user_item.T)

    def recommend(self, user_id: str, top_k: int = 10) -> list:
        """
        Recommend top_k songs to the given user based on item similarity.
        """
        if self.user_item_matrix is None or self.song_similarity is None:
            raise ValueError("Model not fitted.")

        if user_id not in self.user_item_matrix.index:
            return []

        user_vector = self.user_item_matrix.loc[user_id].values
        scores = np.dot(user_vector, self.song_similarity)

        # Zero out already listened songs
        listened = user_vector > 0
        scores[listened] = -np.inf

        top_indices = np.argsort(scores)[-top_k:][::-1]
        recommended_song_ids = [self.song_id_map[idx] for idx in top_indices]

        return recommended_song_ids
