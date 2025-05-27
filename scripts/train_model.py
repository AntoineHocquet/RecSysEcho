# scripts/train_model.py

import argparse
from src import data_loader, features
from src.models.popularity import PopularityRecommender


# dummy polularity model (can be removed)
def train_popularity_model(df):
    """Trains a dummy popularity-based model by song play count."""
    song_counts = df.groupby("song_id").size().sort_values(ascending=False)
    return song_counts.head(10)

def main():
    parser = argparse.ArgumentParser(description="Train a music recommender model.")
    parser.add_argument("--model", type=str, default="popularity", help="Model to train: [popularity | item_cf | mf]")
    parser.add_argument("--min_interactions", type=int, default=3, help="Minimum interactions per user")
    args = parser.parse_args()

    print(f"📥 Loading data...")
    df = data_loader.load_preprocessed_data()

    print(f"🔍 Filtering users with >= {args.min_interactions} interactions...")
    df = features.filter_users_with_min_interactions(df, min_interactions=args.min_interactions)

    print(f"🔢 Encoding user/song IDs...")
    df = features.encode_ids(df)

    if args.model == "popularity":
        model = PopularityRecommender()
        print("📊 Training popularity-based recommender...")
        model.fit(df)
        top_songs = model.recommend(top_k=10)
        print("🎧 Top recommended songs:")
        print(top_songs)

    elif args.model == "item_cf":
        from src.models.item_cf import ItemBasedCFRecommender
        model = ItemBasedCFRecommender()
        model.fit(df)

        user_id = df["user_id"].iloc[0]  # pick a sample user
        print(f"👤 Recommendations for user: {user_id}")
        recommendations = model.recommend(user_id, top_k=10)
        print("🎧 Top recommended songs:")
        print(recommendations)

    else:
        print(f"❌ Model '{args.model}' not yet implemented.")


if __name__ == "__main__":
    main()
