る
import streamlit as st
import numpy as np
import time

st.title("ガチャガチャをまわせ♪")

selected_animal = st.sidebar.selectbox("だれにする？", ["🐶いぬ🐶", "🐱ねこ🐱", "🐰うさぎ🐰"])

if selected_animal == "🐶いぬ🐶":
    st.sidebar.image("static/dog.png")
elif selected_animal == "🐱ねこ🐱":
    st.sidebar.image("static/cat.png")
elif selected_animal == "🐰うさぎ🐰":
    st.sidebar.image("static/usagi.png")

st.image("static/gachagacha.png")

if st.button("まわす"):
    with st.spinner('ちょっと待ってね...'):
        time.sleep(2)
        
        st.image("static/gach.png")
        time.sleep(2)
        
        options = ["はずれ","ケーキ","ドーナツ","チョコ","キャンディ","つみき","ぬいぐるみ","しんかんせん","ラッパ"]
        luck = np.random.choice(options, 1, p=[0.4, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075])[0]
        
        if luck == "はずれ":
            image = "static/hazure.png"
        elif luck == "ケーキ":
            image = "static/shortcake.png"
        elif luck == "ドーナツ":
            image = "static/donut.png"
        # 他のケースも同様に処理

        st.image(f"static/{image}")

if st.button("もういちど"):
    placeholder = st.empty()
    placeholder.empty()