import streamlit as st

# import numpy as np
# import pandas as pd
# from PIL import Image
import module



st.title("streamlitでSpotify APIを使う")


# 入力フィールドを追加
search_query = st.text_input("検索クエリ:")

# 検索ボタンを追加
search_button = st.button("検索")




if search_button:
    result = module.get_artist_image(search_query)
    st.write(search_query)
    st.image(result)





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
