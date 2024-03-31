import streamlit as st
import matplotlib.pyplot as plt
import japanize_matplotlib
japanize_matplotlib.japanize()
import seaborn as sns
import module


st.title("Spotifyプレイリストの比較分析ツール")

'''
2つの検索ワードを入力すると、そのワードからSpotify上のプレイリストを複数取得し、それらに含まれる楽曲をまとめ、特徴をヒストグラムに表示します。
それぞれのキーワードから得られるプレイリストに含まれる曲が、どのように異なるのかを比較することができます。
'''
# 検索窓
search_query_1 = st.text_input("検索ワード1", placeholder="例：ドライブ")
search_query_2 = st.text_input("検索ワード2",  placeholder="例：リラックス")

# 検索実行ボタン
search_button = st.button("プレイリスト情報取得")

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
        st.write(", ".join(playlist_titles_1))

        st.subheader(f"「{search_query_2}」で検索したプレイリストに含まれる楽曲の概要")
        st.write(songs_2_df.describe())
        st.write("取得したプレイリスト名　※各10曲抽出")
        st.write(", ".join(playlist_titles_2))


        st.header("ヒストグラムでの各特長の比較")
        for column in songs_1_df.columns:
            # st.subheader(f"{column}の比較")

            # fig, ax = plt.subplots()
            # plt.hist(songs_1_df[column], color="red", alpha=0.5)
            # plt.hist(songs_2_df[column], color="blue", alpha=0.5)
            # plt.legend([search_query_1, search_query_2], prop={"family": "MS Gothic"})
            # st.pyplot(fig)

            st.subheader(f"{column}の比較")

            # seabornでスタイルを設定
            sns.set_style("darkgrid")
            # フォントを設定
            plt.rcParams["font.family"] = "MS Gothic"

            fig, ax = plt.subplots()
            sns.histplot(data=songs_1_df[column], color="red", alpha=0.5, ax=ax)
            sns.histplot(data=songs_2_df[column], color="blue", alpha=0.5, ax=ax)
            ax.legend([search_query_1, search_query_2])
            st.pyplot(fig)
    # 入力欄のどちらかが空だったらアラート
    else:
        st.warning("2つの検索キーを入力してください")
