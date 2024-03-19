import streamlit as st

# import numpy as np
import pandas as pd
# from PIL import Image
import module


st.title("streamlitでSpotify APIを使う")


search_query1 = st.text_input("検索クエリ:")
search_button1 = st.button("検索1")

if search_button1:
    image = module.get_artist_image(search_query1)
    st.write(search_query1)
    st.image(image)


search_query2 = st.text_input("プレイリストのURLを入力してください")

search_button2 = st.button("検索2")
if search_button2:
    songs = module.get_songs_from_playlist(search_query2)
    df = pd.DataFrame()

    for song in songs:
        st.write(song["track"]["name"])

        feature = module.get_audio_features(song["track"]["uri"])
        new_row = pd.DataFrame.from_dict(feature)
        st.dataframe(new_row)

    # st.dataframe(df)








"""
# タイトル
# test change


```
import streamlit as st
```
"""

# st.write("dataframe")

# df = pd.DataFrame({
#     "1": [1, 2, 3, 4],
#     "2": [12, 22, 32, 42]
# })

# st.dataframe(df)



# img = Image.open("./climb.JPG")
# st.image(img, caption="登っている俺", use_column_width=True)
