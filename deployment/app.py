import streamlit as st

import eda
import prediction

# navigation
navigation = st.sidebar.selectbox('Pilih Halaman',('predictor','EDA'))

# pilih page

if navigation == 'predictor':
    prediction.run()
else:
    eda.run()