import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f901ff2443e14b088a4ee57c94a35c72",
                                                           client_secret="95ef6f1949d9478e8e48e2b397cb114a"))
def create_song_df_from_keyword(keyword):
    
        # キーワードからプレイリストを取得しそれらのidを配列に代入
    playlist_items = sp.search(q=keyword, type='playlist', limit=2)["playlists"]["items"]
    playlist_ids = list(map(lambda item: item["id"], playlist_items))
    playlist_titles = list(map(lambda item: item["name"], playlist_items))


    total_song_items = []
    # プレイリストのidで曲情報を取得
    for playlist_id in playlist_ids:
        song_items = sp.playlist_tracks(playlist_id, limit=10)["items"]
        total_song_items += song_items
    
    # songs_df = pd.DataFrame()
    song_ids = list(map(lambda item: item["track"]["id"], total_song_items))
    # idのリストでfeatureを取得
    song_feature_dict = sp.audio_features(song_ids)
    song_feature_df = pd.DataFrame.from_dict(song_feature_dict)
    # 数値のデータのみに限定
    song_feature_df = song_feature_df.select_dtypes(include='float64')

    return song_feature_df, playlist_titles


