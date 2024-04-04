import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="f901ff2443e14b088a4ee57c94a35c72",
                                                           client_secret="95ef6f1949d9478e8e48e2b397cb114a"))
def create_song_df_from_keyword(keyword):
    # キーワードからプレイリストを取得しそれらのidを配列に代入
    playlist_items = sp.search(q=keyword, type='playlist', limit=10)["playlists"]["items"]
    playlist_ids = list(map(lambda item: item["id"], playlist_items))
    playlist_titles = list(map(lambda item: item["name"], playlist_items))

    total_song_items = []
    # プレイリストのidで曲情報を取得
    for playlist_id in playlist_ids:
        song_items = sp.playlist_tracks(playlist_id, limit=10)["items"]
        total_song_items += song_items
    
    song_ids = list(map(lambda item: item["track"]["id"], total_song_items))
    # idのリストでfeatureを取得
    song_feature_dict = sp.audio_features(song_ids)
    song_feature_df = pd.DataFrame.from_dict(song_feature_dict)
    # 数値のデータのみに限定
    song_feature_df = song_feature_df.select_dtypes(include='float64')

    return song_feature_df, playlist_titles


feature_explaination = {   
    "danceability":'"danceability"については、テンポ、リズムの安定性、ビートの強さ、全体的な規則性など、音楽的要素の組み合わせに基づいて、トラックがダンスにどの程度適しているかを表します。0.0は最もダンサブルではなく、1.0は最もダンサブルです。',
    "energy":'"energy"については、0.0から1.0までの尺度で、強度と活動の知覚的尺度を表します。一般的に、エネルギッシュな曲は速く、うるさく、騒々しく感じられます。例えば、デスメタルはエネルギーが高く、バッハの前奏曲は低いです。この属性に寄与する知覚的特徴には、ダイナミック・レンジ、知覚されるラウドネス、音色、オンセット・レート、および一般的なエントロピーが含まれています。',
    "loudness":'"loudness"については、トラック全体のラウドネスをデシベル(dB)で表します。ラウドネス値はトラック全体の平均であり、トラックの相対的なラウドネスを比較するのに便利です。ラウドネスとは、物理的な強さ(振幅)と心理的な相関関係がある音の質のことです。値の範囲は一般的に-60~0dbです。',
    "speechiness":'"speechiness"については、トラック中の話し言葉の存在を検出します。より話し言葉に近い録音(トークショー、オーディオブック、詩など)ほど、属性値は1.0に近くなります。0.66以上の値は、おそらくすべて話し言葉で構成されているトラックを表すと考えられます。0.33から0.66の間の値は、音楽と話し言葉の両方が含まれる可能性のあるトラックを表します。0.33以下の値は、音楽やその他の音声以外のトラックを表している可能性が高いです。',
    "acousticness":'"acousticness"については、トラックがアコースティックであるかどうかを0.0から1.0までの信頼度で表します。1.0は、トラックがアコースティックであることの確信度が高いことを表します。',
    "instrumentalness":'"instrumentalness"については、トラックにボーカルが含まれていないかどうかを予測します。"Ooh"や"aah"といった音は、この文脈ではインストゥルメンタルとして扱われます。ラップや話し言葉のトラックは明らかに「ボーカル」です。instrumentalnessの値が1.0に近いほど、トラックにボーカルが含まれていない可能性が高くなります。0.5以上の値はインストゥルメンタル・トラックを表すことを意図していますが、値が1.0に近づくほど信頼度は高くなります。',
    "liveness":'"liveness"については、録音中のオーディエンスの存在を検出します。ライブ性の値が高いほど、そのトラックがライブで演奏された可能性が高くなります。値が0.8を超えると、そのトラックがライブである可能性が高くなると考えられます。',
    "valence": '"valence"については、0.0から1.0までの数値で、トラックが伝える音楽的なポジティブさを表します。ヴァレンスの高い曲はよりポジティブ(例えば、ハッピー、陽気、多幸感)に聞こえ、ヴァレンスの低い曲はよりネガティブ(例えば、悲しい、憂鬱、怒り)に聞こえます。',
    "tempo": '"tempo"については、トラックの全体的な推定テンポを1分あたりの拍数(BPM)で表します。音楽用語では、テンポは与えられた曲の速度またはペースのことで、平均拍継続時間から直接導かれます。'
}
