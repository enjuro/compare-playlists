import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import module


st.title("Spotifyプレイリストの分析")


search_query2 = st.text_input("プレイリストのURLを入力してください")

search_button2 = st.button("楽曲情報取得")
if search_button2:
    songs_df = pd.DataFrame()

    songs = module.get_songs_from_playlist(search_query2)

    for song in songs:
        # タイトルを取得
        song_title = song["track"]["name"]
        # 楽曲の特徴を辞書型で取得
        song_feature_dict = module.get_audio_features(song["track"]["uri"])
        # 楽曲の特徴の辞書型をデータフレーム型に変換
        song_feature_df = pd.DataFrame.from_dict(song_feature_dict)
        # 数値のデータのみに限定
        song_feature_df = song_feature_df.select_dtypes(include='float64')
        song_feature_df.index = [song_title]
        songs_df = pd.concat([songs_df, song_feature_df])
        
    st.dataframe(songs_df)


    # for column in songs_df.columns:
    #     st.write(column)
    #     # 選択した列の要素をプロット
    #     plt.figure(figsize=(8, 6))
    #     plt.bar(songs_df.index, songs_df[column])
    #     plt.title(f'Plot of {column}')
    #     plt.xlabel('Index')
    #     plt.ylabel('Value')
    #     plt.grid(True)
    #     st.pyplot(plt)

    for column in songs_df.columns:
        st.subheader(f'Histogram for {column}')
        plt.figure(figsize=(8, 6))
        plt.hist(songs_df[column], bins=10, edgecolor='black')
        plt.title(column)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        st.pyplot(plt)