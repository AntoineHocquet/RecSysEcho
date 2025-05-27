# tests/test_models.py

from src.data_loader import load_preprocessed_data
from src.features import filter_users_with_min_interactions, encode_ids
from src.models.popularity import PopularityRecommender
from src.models.item_cf import ItemBasedCFRecommender


def test_popularity_model_recommendation():
    df = load_preprocessed_data()
    df = filter_users_with_min_interactions(df)
    df = encode_ids(df)

    model = PopularityRecommender()
    model.fit(df)
    top_k = model.recommend(top_k=5)

    assert len(top_k) == 5
    assert "song_id" in top_k.columns
    assert "play_count" in top_k.columns


def test_item_cf_model():
    df = load_preprocessed_data()
    df = filter_users_with_min_interactions(df)
    df = encode_ids(df)

    model = ItemBasedCFRecommender()
    model.fit(df)
    user_id = df["user_id"].iloc[0]
    recs = model.recommend(user_id=user_id, top_k=5)
    assert isinstance(recs, list)
    assert len(recs) == 5

