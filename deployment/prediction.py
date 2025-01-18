import pandas as pd
import numpy as np

import streamlit as st

import pickle

# load model

with open('model_v1.pkl', 'rb') as file:
    model = pickle.load(file)

def run():
    #set title

    st.title('Loan Approval Predictor')
    st.write('---')

    # set banner

    link_gambar = ('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKWGaveyTGVVXNQs3f_kzdsa2dO1Ymlq7S8g&s')
    st.image(link_gambar)

    # deskripis
    st.write('Halaman ini berisi model untuk melakukan prediksi Loan Approval')

    # buat form
    with st.form(key='form paramters'):
        age = st.number_input('Age :',min_value=0,value=25)
        gender = st.selectbox('Gender:',('male','female'))
        education = st.selectbox('Education:',('Master', 'High School', 'Bachelor', 'Associate', 'Doctorate'))
        income = st.number_input('Income:',min_value=0,value=40000,step=100)
        Employment_Experience = st.number_input('Years of employment experience:',min_value=0,max_value=100)
        home_ownership = st.selectbox('Home Ownership:',('RENT', 'OWN', 'MORTGAGE', 'OTHER'))
        loan_amnt = st.number_input('Loan Amount:',min_value=0,value=7000,step=100)
        loan_intent = st.selectbox('Purpose of Loan:',('PERSONAL', 'EDUCATION', 'MEDICAL', 'VENTURE', 'HOMEIMPROVEMENT', 'DEBTCONSOLIDATION'))
        loan_int_rate = st.slider('Loan interest rate (%) :',min_value=0.0,max_value= 100.0)
        loan_percent_income = st.slider('Loan amount as a percentage of annual income (if 5% = 0.05):',0.0, 1.0,)
        credit_history = st.number_input('Credit History (year):',min_value=0,max_value=100)
        credit_score = st.number_input('Credit Score:',min_value=0,max_value=1000,step=100)
        previous_loan = st.selectbox('previous loan defaults on file:',('Yes','No'))

        submit = st.form_submit_button('Prediksi')

    data_raw = {
        'person_age':age,
        'person_gender':gender,
        'person_education':education,
        'person_income':income,
        'person_emp_exp':Employment_Experience,
        'person_home_ownership':home_ownership,
        'loan_amnt':loan_amnt,
        'loan_intent':loan_intent,
        'loan_int_rate':loan_int_rate,
        'loan_percent_income':loan_percent_income,
        'cb_person_cred_hist_length':credit_history,
        'credit_score':credit_score,
        'previous_loan_defaults_on_file':previous_loan
    }

    data = pd.DataFrame([data_raw])
    st.dataframe(data)

    if submit:
        result = model.predict(data)
        st.write(f"### Hasil Prediksi Loan Aprroval : {result[0]:.2f}")


if __name__ == '__main__':
    run()