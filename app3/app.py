import streamlit as st
import numpy as np

st.title("ガチャガチャをまわせ♪")

selected_animal = st.sidebar.selectbox("だれにする？", ["🐶いぬ🐶", "🐱ねこ🐱", "🐰うさぎ🐰"])

if selected_animal == "🐶いぬ🐶": 
    st.sidebar.image("dog.png")
elif selected_animal == "🐱ねこ🐱": 
    st.sidebar.image("cat.png")
elif selected_animal == "🐰うさぎ🐰": 
    st.sidebar.image("usagi.png")

st.image("gachagacha.png")

if st.button("まわす"):
    with st.spinner('ちょっと待ってね...'):
        time.sleep(2)
        
        st.image("gach.png")
        time.sleep(2)
        
        options = ["はずれ","ケーキ","ドーナツ","チョコ","キャンディ","つみき","ぬいぐるみ","しんかんせん","ラッパ"]
        luck = np.random.choice(options, 1, p=[0.4, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075, 0.075])[0]
        
        if luck == "はずれ":
            image = "hazure.png"
        elif luck == "ケーキ":
            image = "shortcake.png"
        elif luck == "ドーナツ":
            image = "donut.png"
        # 他のケースも同様に処理

        st.image(image)

if st.button("もういちど"):
    st.caching.clear_cache()