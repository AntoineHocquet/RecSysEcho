import sqlite3
import pandas as pd
from pathlib import Path
from tabulate import tabulate

DB_PATH = "data/raw/track_metadata.db"

def list_tables(conn: sqlite3.Connection) -> list[str]:
    query = "SELECT name FROM sqlite_master WHERE type='table';"
    tables = pd.read_sql_query(query, conn)
    return tables['name'].tolist()

def show_schema(conn: sqlite3.Connection, table: str) -> pd.DataFrame:
    query = f"PRAGMA table_info({table});"
    return pd.read_sql_query(query, conn)

def count_rows(conn: sqlite3.Connection, table: str) -> int:
    query = f"SELECT COUNT(*) as row_count FROM {table};"
    return pd.read_sql_query(query, conn).iloc[0]['row_count']

def preview_data(conn: sqlite3.Connection, table: str, limit: int = 5) -> pd.DataFrame:
    query = f"SELECT * FROM {table} LIMIT {limit};"
    return pd.read_sql_query(query, conn)

def run_eda(db_path: str = DB_PATH) -> None:
    if not Path(db_path).exists():
        print(f"❌ Database not found at {db_path}")
        return

    print(f"\n🔍 Exploring database: {db_path}")
    conn = sqlite3.connect(db_path)
    tables = list_tables(conn)

    if not tables:
        print("⚠️ No tables found in the database.")
        conn.close()
        return

    print(f"\n📋 Found {len(tables)} table(s): {tables}")

    for table in tables:
        print(f"\n{'='*60}\n📄 Table: '{table}'")
        try:
            schema = show_schema(conn, table)
            print("\n📐 Schema:")
            print(tabulate(schema, headers='keys', tablefmt='grid', showindex=False))

            row_count = count_rows(conn, table)
            print(f"\n🔢 Row count: {row_count}")

            preview = preview_data(conn, table)
            print(f"\n👁️ Preview (first {len(preview)} rows):")
            print(tabulate(preview, headers='keys', tablefmt='fancy_grid', showindex=False))

        except Exception as e:
            print(f"\n⚠️ Skipped table '{table}' due to error:\n{e}")

    conn.close()
    print(f"\n✅ EDA completed successfully.\n{'='*60}")

def main() -> None:
    run_eda()

if __name__ == "__main__":
    main()
