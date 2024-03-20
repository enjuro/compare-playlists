import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f901ff2443e14b088a4ee57c94a35c72",
                                                           client_secret="95ef6f1949d9478e8e48e2b397cb114a"))

# https://open.spotify.com/playlist/
def get_songs_from_playlist(playlist_url):
    # Extract playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]

    # Get playlist tracks
    results = sp.playlist_tracks(playlist_id, limit=10)
    return results['items']


def get_artist_image(artist_name):
    # アーティストを検索してIDを取得
    results = sp.search(q=artist_name, type='artist')
    items = results['artists']['items']
    if len(items) > 0:
        artist_id = items[0]['id']

        # アーティストの情報を取得して画像URLを取得
        artist_info = sp.artist(artist_id)
        if len(artist_info['images']) > 0:
            image_url = artist_info['images'][0]['url']
            return image_url
        else:
            return "No image available for this artist"
    else:
        return "Artist not found"

def get_audio_features(song_id):
    return sp.audio_features(song_id)

