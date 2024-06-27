import streamlit as st
st.title("サンプルアプリ")

# input

options = ["1", "2"]
sample_select = st.sidebar.selectbox(
    '好きな画像を選んで！', options)
if sample_select == "1":
    sentence = "これは1です"
    img = "1.png"
elif sample_select == "2":
    sentence = "これは2です"
    img = "2.png"
else:
    sentence = "画像が見つかりませんでした"
    img = "notfound.png"


# output
st.text(sentence)
st.image(img, caption='sample', use_column_width=True)
