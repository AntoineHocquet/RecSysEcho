import os
import sqlite3
import pandas as pd

DB_PATH = "data/raw/track_metadata.db"

def test_year_filter():
    assert os.path.exists(DB_PATH), "Metadata DB not found. Run the fetch script first."

    conn = sqlite3.connect(DB_PATH)
    query = """
        SELECT track_id, title, artist_name, year
        FROM songs
        WHERE year >= 2010
        ORDER BY year
        LIMIT 100
    """
    df = pd.read_sql_query(query, conn)

    assert not df.empty, "No rows returned."
    assert all(df['year'] >= 2010), "Some rows have invalid years."

    print("✅ test_year_filter passed")

if __name__ == "__main__":
    test_year_filter()
