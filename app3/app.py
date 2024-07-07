import streamlit as st
import PIL.Image
import numpy as np
import time

st.title("ガチャガチャをまわせ♪")

# 画像ファイルのパス
dog_path = "streamlit/app3/dog.png"
cat_path = "streamlit/app3/cat.png"
usagi_path = "streamlit/app3/usagi.png"

selected_animal = st.sidebar.selectbox("だれにする？", ["🐶いぬ🐶", "🐱ねこ🐱", "🐰うさぎ🐰"])

# 選択したキャラクターに応じて画像を表示
if selected_animal == "🐶いぬ🐶":
    st.sidebar.image(Image.open(dog_path), caption="いぬ")
elif selected_animal == "🐱ねこ🐱":
    st.sidebar.image(Image.open(cat_path), caption="ねこ")
elif selected_animal == "🐰うさぎ🐰":
    st.sidebar.image(Image.open(usagi_path), caption="うさぎ")

st.image("streamlit/app3/gachagacha.png")

if st.button("まわす"):
    with st.spinner('ちょっと待ってね...'):
        time.sleep(2)
        
        st.image("streamlit/app3/gach.png")
        time.sleep(2)
        
        options = ["はずれ", "ケーキ", "ドーナツ"]
        luck = np.random.choice(options, 1, p=[0.33, 0.34, 0.33])[0]
        
        if luck == "はずれ":
            image_path = "streamlit/app3/hazure.png"
        elif luck == "ケーキ":
            image_path = "streamlit/app3/shortcake.png"
        elif luck == "ドーナツ":
            image_path = "streamlit/app3/donut.png"

        st.image(image_path)

if st.button("もういちど"):
    st.caching.clear_cache()