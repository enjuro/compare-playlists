import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import module


st.title("Spotifyプレイリストの分析")

search_query_1 = st.text_input("検索ワード1", "")
search_query_2 = st.text_input("検索ワード2", "")

search_button = st.button("プレイリスト情報取得")
if search_button:
    songs_df = pd.DataFrame()

    songs_1 = module.get_songs_by_playlist_keyword(search_query_1)
    songs_2 = module.get_songs_by_playlist_keyword(search_query_2)



    songs_1_df = module.create_song_df(songs_1)
    songs_2_df = module.create_song_df(songs_2)

    st.write(f"検索ワード：{search_query_1}")
    st.write(songs_1_df.describe())

    st.write(f"検索ワード：{search_query_2}")
    st.write(songs_2_df.describe())
    
    # st.dataframe(songs_1_df)
    # st.dataframe(songs_2_df)

    # for column in songs_df.columns:
    #     st.subheader(f'Histogram for {column}')
    #     plt.figure(figsize=(8, 6))
    #     plt.hist(songs_df[column], bins=10, edgecolor='black')
    #     plt.title(column)
    #     plt.xlabel(column)
    #     plt.ylabel('Frequency')
    #     st.pyplot(plt)