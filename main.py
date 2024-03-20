import streamlit as st
import pandas as pd
import module


st.title("Spotifyプレイリストの分析")


search_query2 = st.text_input("プレイリストのURLを入力してください")

search_button2 = st.button("楽曲情報取得")
if search_button2:
    songs_df = pd.DataFrame()

    songs = module.get_songs_from_playlist(search_query2)

    for song in songs:
        # st.write(song["track"]["name"])
        song_feature_dict = module.get_audio_features(song["track"]["uri"])
        song_feature_df = pd.DataFrame.from_dict(song_feature_dict)
        # st.dataframe(song_feature_df)
        songs_df = pd.concat([songs_df, song_feature_df])

    st.dataframe(songs_df)

