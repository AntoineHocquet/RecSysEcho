import os
import sqlite3
import pandas as pd
import requests
import certifi
import argparse
from tqdm import tqdm

DB_URL = "https://labrosa.ee.columbia.edu/millionsong/sites/default/files/AdditionalFiles/track_metadata.db"
DB_PATH = "data/raw/track_metadata.db"
SAMPLE_PATH = "data/sample/filtered_tracks.csv"

def download_sqlite_db(insecure=False):
    os.makedirs("data/raw", exist_ok=True)

    if os.path.exists(DB_PATH):
        size_mb = os.path.getsize(DB_PATH) / 1e6
        print(f"⚠️ Database already exists at {DB_PATH} ({size_mb:.2f} MB)")
        return

    print("⬇️  Downloading metadata SQLite database...")

    verify_cert = False if insecure else certifi.where()

    try:
        with requests.get(DB_URL, stream=True, verify=verify_cert) as r:
            r.raise_for_status()
            total_size = int(r.headers.get("Content-Length", 0))
            temp_path = DB_PATH + ".tmp"

            with open(temp_path, "wb") as f, tqdm(
                total=total_size,
                unit="B", unit_scale=True, desc="Downloading", ncols=80
            ) as pbar:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        pbar.update(len(chunk))

            os.rename(temp_path, DB_PATH)
            print("✅ Download complete and saved.")

    except Exception as e:
        print(f"❌ Download failed: {e}")
        if os.path.exists(DB_PATH + ".tmp"):
            os.remove(DB_PATH + ".tmp")
        raise

def filter_by_year(min_year=0, limit=10000):
    print(f"🔎 Filtering tracks with year >= {min_year} ...")
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
    print(f"✅ Saved {len(df)} tracks to {SAMPLE_PATH}")

def main():
    parser = argparse.ArgumentParser(description="Fetch and filter Million Song Dataset metadata")
    parser.add_argument('--filter', type=str, choices=['year'], required=True, help="Filter type (only 'year' supported for now)")
    parser.add_argument('--min_year', type=int, default=0, help="Minimum year of tracks to include")
    parser.add_argument('--limit', type=int, default=10000, help="Max number of rows to output")
    parser.add_argument('--insecure', action='store_true', help="Disable SSL verification (not recommended)")

    args = parser.parse_args()
    download_sqlite_db(insecure=args.insecure)

    if args.filter == 'year':
        filter_by_year(min_year=args.min_year, limit=args.limit)

if __name__ == "__main__":
    main()
