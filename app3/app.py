import streamlit as st
import numpy as np
import time

st.title("ガチャガチャをまわせ♪")


selected_animal = st.sidebar.selectbox("だれにする？", ["🐶　いぬ　🐶", "🐱　ねこ　🐱", "🐰　うさぎ　🐰"])

if selected_animal == "🐶　いぬ　🐶": 
   st.sidebar.image("dog.png")
elif  selected_animal == "🐱　ねこ　🐱": 
      st.sidebar.image("cat.png")
elif selected_animal == "🐰　うさぎ　🐰": 
      st.sidebar.image("usagi.png")


st.image("gachagacha.png")

if st.button("まわす"):
  time.sleep(2)

  st.image("gach.png")
  time.sleep(2)

  options = ["はずれ","ケーキ","ドーナツ"]
  luck = np.random.choice(options, 1, p=[0.4,0.3,0.3])[0]
 
  if luck=="はずれ":
     image = "hazure.png"
  elif luck=="ケーキ":
       image = "shortcake.png"
  elif luck=="ドーナツ":
       image = "donut.png"

  st.image(image)
if st.button("もういちど"):
  placeholder = st.empty()
  placeholder.empty()