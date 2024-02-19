import streamlit as st
from random import choice

if st.button("おみくじ"):
    r = choice(["大吉","中吉","小吉","凶"])
    st.write(r)