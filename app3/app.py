import streamlit as st
import numpy as np
import time
from PIL import Image

# キャラクター画像のデータ
character_images = {
    "🐶いぬ🐶": Image.open("dog.png"),
    "🐱ねこ🐱": Image.open("cat.png"),
    "🐰うさぎ🐰": Image.open("usagi.png")
}

# ガチャ結果の画像のデータ
gacha_images = {
    "はずれ": Image.open("hazure.png"),
    "ケーキ": Image.open("shortcake.png"),
    "ドーナツ": Image.open("donut.png"),
    "チョコ": Image.open("itachoco.png"),
    "キャンディ": Image.open("candy.png"),
    "つみき": Image.open("tsumiki.png"),
    "ぬいぐるみ": Image.open("bear.png"),
    "しんかんせん": Image.open("shinkansen.png"),
    "ラッパ": Image.open("rappa.png")
}

st.title("ガチャガチャをまわせ♪")

selected_animal = st.sidebar.selectbox("だれにする？", ["🐶いぬ🐶", "🐱ねこ🐱", "🐰うさぎ🐰"])

# 選ばれたキャラクターの画像をサイドバーに表示
if selected_animal in character_images:
    st.sidebar.image(character_images[selected_animal], caption=selected_animal)

# ガチャガチャの画像を表示
st.image(Image.open("gachagacha.png"))

if st.button("まわす"):
    with st.spinner('ちょっと待ってね...'):
        time.sleep(2)
        
        st.image(Image.open("gach.png"))
        time.sleep(2)
        
        options = ["はずれ", "ケーキ", "ドーナツ", "チョコ", "キャンディ", "つみき", "ぬいぐるみ", "しんかんせん", "ラッパ"]
        probabilities = [0.4, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075]
        luck = np.random.choice(options, 1, p=probabilities)[0]
        
        # 選ばれたアイテムの画像を表示
        st.image(gacha_images[luck])

if st.button("もういちど"):
    st.caching.clear_cache()