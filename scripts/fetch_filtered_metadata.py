import os
import argparse
import sqlite3
import pandas as pd
import urllib.request

DB_URL = "https://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/track_metadata.db"
DB_PATH = "data/raw/track_metadata.db"
SAMPLE_PATH = "data/sample/filtered_tracks.csv"

def download_sqlite_db():
    os.makedirs("data/raw", exist_ok=True)
    if not os.path.exists(DB_PATH):
        print("Downloading metadata SQLite database...")
        urllib.request.urlretrieve(DB_URL, DB_PATH)
        print("Download complete.")
    else:
        print("Database already exists, skipping download.")

def filter_by_year(min_year=0, limit=10000):
    print(f"Filtering tracks with year >= {min_year} ...")
    conn = sqlite3.connect(DB_PATH)
    query = f"""
        SELECT track_id, title, artist_name, year
        FROM songs
        WHERE year >= {min_year}
        ORDER BY year
        LIMIT {limit}
    """
    df = pd.read_sql_query(query, conn)
    os.makedirs("data/sample", exist_ok=True)
    df.to_csv(SAMPLE_PATH, index=False)
    print(f"Saved {len(df)} tracks to {SAMPLE_PATH}")

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter Million Song Dataset metadata")
    parser.add_argument('--filter', type=str, choices=['year'], required=True, help="Filter type (only 'year' supported for now)")
    parser.add_argument('--min_year', type=int, default=0, help="Minimum year of tracks to include")
    parser.add_argument('--limit', type=int, default=10000, help="Max number of rows to output")

    args = parser.parse_args()
    download_sqlite_db()

    if args.filter == 'year':
        filter_by_year(min_year=args.min_year, limit=args.limit)

if __name__ == "__main__":
    main()
