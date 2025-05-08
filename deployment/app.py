import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Pilih Halaman: ', ('EDA', 'Prediction'))

if page.casefold() == 'eda':
    eda.run()
else:
    prediction.run()