import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src import data_loader, features


# Create plot directory if it doesn't exist
PLOT_DIR = "plots"
os.makedirs(PLOT_DIR, exist_ok=True)


def print_basic_stats(df):
    print(f"Unique users: {df['user_id'].nunique()}")
    print(f"Unique songs: {df['song_id'].nunique()}")
    print(f"Unique artists: {df['artist_name'].nunique()}")
    return None


def print_most_active_users(df):
    print("\n--- Most Active Users ---")
    user_counts = df['user_id'].value_counts().head(10)
    print(user_counts)
    return None


def print_most_popular_songs(df):
    print("\n--- Most Popular Songs (Filtered Data) ---")
    song_counts = df['song_id'].value_counts().head(10)
    top_songs = df[df['song_id'].isin(song_counts.index)]
    song_info = (
        top_songs[['song_id', 'title', 'artist_name', 'year']]
        .drop_duplicates()
        .set_index('song_id')
    )
    top_10_songs = song_info.loc[song_counts.index]
    print(top_10_songs)
    return None


def plot_songs_released_per_year(df):
    print("\n--- Plotting Songs Released per Year ---")
    released_counts = (
        df.groupby('year').count()['song_id'].rename('songs_released')
    )
    plt.figure(figsize=(12, 6))
    sns.barplot(x=released_counts.index, y=released_counts.values)
    plt.xticks(rotation=90)
    plt.xlabel("Year")
    plt.ylabel("Number of Songs Released")
    plt.title("Songs Released per Year")
    plt.tight_layout()
    plot_path = os.path.join(PLOT_DIR, "songs_released_per_year.png")
    plt.savefig(plot_path)
    plt.close()
    print(f"Plot saved to {plot_path}")
    return None


def plot_play_count_distribution(df):
    print("\n--- Plotting Play Count Distribution ---")
    plt.figure(figsize=(10, 5))
    sns.histplot(df['play_count'], bins=50, kde=True)
    plt.xlabel("Play Count")
    plt.title("Distribution of Play Counts (Filtered Data)")
    plt.tight_layout()
    hist_path = os.path.join(PLOT_DIR, "play_count_distribution.png")
    plt.savefig(hist_path)
    plt.close()
    print(f"Histogram saved to {hist_path}")
    return None


def main():
    # Load and filter data
    df_nofilter = data_loader.load_preprocessed_data()
    df_filter = features.apply_filters(df_nofilter)

    print("\n--- Basic Statistics ---")
    for label, df in zip(["Unfiltered", "Filtered"], [df_nofilter, df_filter]):
        print(f"\n{label} data:")
        print_basic_stats(df)

    # Most active users for filtered data only
    print_most_active_users(df_filter)

    # Most popular songs for filtered data only
    print_most_popular_songs(df_filter)

    # Plot: songs released per year
    plot_songs_released_per_year(df_nofilter)

    # Plot: play count distribution
    plot_play_count_distribution(df_filter)


if __name__ == "__main__":
    main()
    print("\n✅ EDA completed successfully!")