import streamlit as st
import matplotlib.pyplot as plt
import module


st.title("Spotifyキーワード比較分析ツール")

'''
検索ワードから取得できるプレイリストに含まれる複数の楽曲の特徴をヒストグラムで表し、比較することができるツールです。
２つのワードの関係性を音楽の特性から見出すことができます。
'''
# 検索窓
search_query_1 = st.text_input("検索ワード１", placeholder="例：ドライブ")
search_query_2 = st.text_input("検索ワード２",  placeholder="例：カフェ")

# 検索実行ボタン
search_button = st.button("楽曲データ取得")

# ボタンが押されたとき
if search_button: 
    # 2つの検索窓に何か入力されている場合は実行
    if search_query_1 and search_query_2:
        songs_1_df, playlist_titles_1 = module.create_song_df_from_keyword(search_query_1)
        songs_2_df, playlist_titles_2 = module.create_song_df_from_keyword(search_query_2)

        st.header("取得したデータの概要")

        st.subheader(f"「{search_query_1}」で検索したプレイリストに含まれる楽曲の概要")
        st.write(songs_1_df.describe())
        st.write("取得したプレイリスト名　※各10曲抽出")
        for title in playlist_titles_1:
            st.write(f"- {title}")

        st.subheader(f"「{search_query_2}」で検索したプレイリストに含まれる楽曲の概要")
        st.write(songs_2_df.describe())
        st.write("取得したプレイリスト名　※各10曲抽出")
        for title in playlist_titles_2:
            st.write(f"- {title}")


        st.header("ヒストグラムでの各特長の比較")

        for column in songs_1_df.columns:
            st.subheader(f"{column}の比較")
            st.write(module.feature_explaination[column])
            fig, ax = plt.subplots()
            plt.hist([songs_1_df[column], songs_2_df[column]], bins=20)

            st.pyplot(fig)
            st.markdown(f"<center><font color=#1F77B4>「{search_query_1}」</font>　<font color=#FF7F0E>「{search_query_2}」</font></center>", unsafe_allow_html=True)

    # 入力欄のどちらかが空だったらアラート
    else:
        st.warning("2つの検索キーを入力してください")
