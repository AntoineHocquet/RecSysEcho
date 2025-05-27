# tests/test_data_loader.py

from src import data_loader

def test_load_song_data():
    df = data_loader.load_song_data()
    assert not df.empty
    assert "song_id" in df.columns

def test_load_count_data():
    df = data_loader.load_count_data()
    assert not df.empty
    assert "song_id" in df.columns

def test_merge_datasets():
    song_df = data_loader.load_song_data()
    count_df = data_loader.load_count_data()
    merged = data_loader.merge_datasets(song_df, count_df)
    assert "song_id" in merged.columns
    assert "artist_name" in merged.columns  # present in song_data
