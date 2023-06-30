import streamlit as st
import gspread
import random
from PIL import Image


st.title('一般熱処理　実技')

syutsudai = st.sidebar.selectbox(
    '番号順(1)orランダム(2)',
    list(range(1,3)))

image = Image.open('2_29_1.jpeg')

st.image(image, caption='2級_29年度_大問1',use_column_width=True)

expander = st.expander('★設問1答え')
expander.write('イ')

expander = st.expander('★設問2答え')
expander.write('1')

expander = st.expander('★設問3答え')
expander.write('a')