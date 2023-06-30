import streamlit as st
import gspread
import random


from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file(
    'API.json',
    scopes=scopes
)

gc = gspread.authorize(credentials)


SP_SHEET_KEY = '1mCkBvteK3WQevKncCyRNw08yyr2ZU6QDyRNvdAik1FM'

sh = gc.open_by_key(SP_SHEET_KEY)

st.title('一般熱処理学科試験過去問')

rank = st.sidebar.selectbox(
    '1級(1)or2級(2)',
    list(range(1,3)))

if rank == 1:

   nendo = st.sidebar.selectbox(
      '何年度の問題を実施しますか？',
      list(range(2017,2023)))


   if nendo == 2017:
      SP_SHEET = '2017_1'
   elif nendo == 2018:
      SP_SHEET = '2018_1'
   elif nendo == 2019:
      SP_SHEET = '2019_1'
   elif nendo == 2020:
      SP_SHEET = '2020_1'
   elif nendo == 2021:
      SP_SHEET = '2021_1'
   elif nendo == 2022:
      SP_SHEET = '2022_1'   
   
      SP_SHEET = '2017_1'

   worksheet = sh.worksheet(SP_SHEET)
   data = worksheet.get_all_values()

   st.write(nendo,'年度学科')

   for j in range(50):
      st.write(data[j+1][0])
      st.write(data[j+1][1])
      st.write('■選択肢')
      for i in range(4):
         st.write(data[j+1][i+2])

      expander = st.expander('★答え')
      expander.write(data[j+1][6])
      expander.write(data[j+1][7])

if rank == 2:

   nendo = st.sidebar.selectbox(
      '何年度の問題を実施しますか？',
      list(range(2017,2023)))


   if nendo == 2017:
      SP_SHEET = '2017_2'
   elif nendo == 2018:
      SP_SHEET = '2018_2'
   elif nendo == 2019:
      SP_SHEET = '2019_2'
   elif nendo == 2020:
      SP_SHEET = '2020_2'
   elif nendo == 2021:
      SP_SHEET = '2021_2'
   elif nendo == 2022:
      SP_SHEET = '2022_2'   


   worksheet = sh.worksheet(SP_SHEET)
   data = worksheet.get_all_values()

   st.write(nendo,'年度学科')

   for j in range(50):
      st.write(data[j+1][0])
      st.write(data[j+1][1])
      st.write('■選択肢')
      for i in range(4):
         st.write(data[j+1][i+2])

      expander = st.expander('★答え')
      expander.write(data[j+1][6])
      expander.write(data[j+1][7])



#gspread==5.0.0
#gspread-dataframe==3.2.2