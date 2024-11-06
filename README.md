# Name - Spotifyキーワード比較分析ツール

検索ワードから取得できるプレイリストに含まれる複数の楽曲の特徴をヒストグラムで表し、比較することができるツールです。

# DEMO

https://compare-playlists-8m6jmvkwzla2t6jyik4ztu.streamlit.app/

# Features


# Requirement
* streamlit 1.32.2
* pandas 2.2.1
* matplotlib 3.8.3
* spotipy 2.23.0

# Usage

検索ワード１，２に好きなワードを入力し、楽曲データ取得を押下すると、それぞれのワードから取得できるプレイリストに含まれる楽曲をデータフレームとしてまとめ、
楽曲情報の概要やヒストグラムを表示することができます。

APIの使用と、Pythonのデータの視覚化ライブラリを勉強する目的で作成しました。
