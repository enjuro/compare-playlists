import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f901ff2443e14b088a4ee57c94a35c72",
                                                           client_secret="95ef6f1949d9478e8e48e2b397cb114a"))

def search_playlists_by_keyword(keyword):
    return  sp.search(q=keyword, type='playlist', limit=10)["playlists"]["items"]
    # ids = list(map(lambda item: item["id"], playlist_items))
    # return ids

def get_songs_from_playlist(playlist_id):
    # Extract playlist ID from the URL
    playlist_id = playlist_id.split('/')[-1]

    # Get playlist tracks
    results = sp.playlist_tracks(playlist_id, limit=100)
    return results['items']


def get_audio_features(song_id):
    return sp.audio_features(song_id)

def create_song_df(songs):
    songs_df = pd.DataFrame()

    for song in songs:
        # タイトルを取得
        song_title = song["track"]["name"]
        # 楽曲の特徴を辞書型で取得
        song_feature_dict = sp.audio_features(song["track"]["id"])
        # 楽曲の特徴の辞書型をデータフレーム型に変換
        song_feature_df = pd.DataFrame.from_dict(song_feature_dict)
        # 数値のデータのみに限定
        song_feature_df = song_feature_df.select_dtypes(include='float64')
        song_feature_df.index = [song_title]
        songs_df = pd.concat([songs_df, song_feature_df])

    return songs_df


def get_songs_by_playlist_keyword(keyword):
    playlist_items = sp.search(q=keyword, type='playlist', limit=10)["playlists"]["items"]
    playlist_ids = list(map(lambda item: item["id"], playlist_items))

    songs = []
    for playlist_id in playlist_ids:
        song_items = sp.playlist_tracks(playlist_id, limit=10)["items"]
        songs += song_items
    return songs