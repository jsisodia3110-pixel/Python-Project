import streamlit as st

st.write('hello, I am Jitendra. Welcome to my quiz zone. Hope you like the game. You may please proceed further for gaming...')
age = st.number_input('Enter your age')
if age>=18:
  st.write('Yu are eligible for license....')
  st.stars()
else:
  st.write('You are not eligible')

