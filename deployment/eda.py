import pandas as pd
import numpy as np

import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    # introdution

    st.title('Eksploratory Data Analysis Loan Approval')

    st.write('---')

    # gambar
    st.image('https://st5.depositphotos.com/7819052/61904/v/450/depositphotos_619044762-stock-illustration-white-coupon-banner-word-loan.jpg',
            caption = 'source : google.com')

    # menampilkan dataframe

    st.write('## Dataframe')

    data = pd.read_csv('loan_data.csv')
    st.dataframe(data.head())

    st.write('''
    - person_age (Float):
Usia seseorang dalam tahun, direpresentasikan dalam angka desimal. Misalnya, seseorang berusia 25.5 tahun.

- person_gender (Categorical):
Jenis kelamin individu, biasanya berupa kategori seperti "Male", "Female"

- person_education (Categorical):
Tingkat pendidikan tertinggi yang diraih oleh individu.

- person_income (Float):
Pendapatan tahunan individu dalam bentuk angka desimal.

- person_emp_exp (Integer):
Lama pengalaman kerja individu dalam tahun. Misalnya, 5 berarti individu tersebut memiliki pengalaman kerja selama 5 tahun.

- person_home_ownership (Categorical):
Status kepemilikan rumah, seperti "Rent" (menyewa), "Own" (memiliki), atau "Mortgage" (kredit rumah).

- loan_amnt (Float):
Jumlah pinjaman yang diminta oleh individu dalam bentuk angka desimal.

- loan_intent (Categorical):
Tujuan dari pinjaman yang diminta, seperti "Education" (pendidikan), "Business" (usaha), "Home Improvement" (perbaikan rumah), dan lain-lain.

- loan_int_rate (Float):
Suku bunga pinjaman.

- loan_percent_income (Float):
Rasio jumlah pinjaman terhadap pendapatan tahunan individu, dinyatakan sebagai persentase. Misalnya, 0.2 berarti pinjaman sebesar 20% dari pendapatan tahunan.

- cb_person_cred_hist_length (Float):
Panjang riwayat kredit individu dalam tahun. Misalnya, jika seseorang memiliki riwayat kredit selama 7.5 tahun, maka nilai ini adalah 7.5.

- credit_score (Integer):
Skor kredit individu yang mencerminkan kelayakan kredit mereka, biasanya berada pada rentang tertentu seperti 300-850.

- previous_loan_defaults_on_file (Categorical):
Indikator apakah individu pernah gagal bayar pinjaman sebelumnya, biasanya "Yes" (pernah) atau "No" (tidak pernah).

- loan_status (Categorical):
Status persetujuan pinjaman, di mana 1 menunjukkan pinjaman disetujui dan 0 menunjukkan pinjaman ditolak.
    ''')

    # Sub-BAB Visualisasi
    st.write('## Visualisasi')
    st.write('### Berapa jumlah peminjaman yang sering diajukan oleh peminjam')

    # create canvas
    fig = plt.figure(figsize=(10,8))
    sns.histplot(x='loan_amnt',data=data,bins=10, kde=True, color='orange')
    st.pyplot(fig)
    st.write('**Insight :**')
    st.write('berdasarkan plot, rata-rata orang akan meminta peminjaman dirange sebesar 5000 hingga 10000. sehingga jika seseorang ingin melakukan peminjaman, sebaiknya meminjam direntang 5000 hingga 10000')



    st.write('### Direntang umur berapakah seseorang sering melakukan peminjaman')
    fig = plt.figure(figsize=(10,8))
    sns.histplot(x='person_age',data=data, bins=40, kde=True, color='skyblue')
    st.pyplot(fig)
    st.write('**Insight :**')
    st.write('dari dataset, rata-rata orang yang ingin melakukan peminjaman berada diumur 20 hingga 30 tahun ')



    st.write('### Bagaimana distribusi dari skor kredit peminjam')
    fig = plt.figure(figsize=(10,8))
    sns.histplot(x='credit_score',data=data, bins=50, kde=True, color='green')
    st.pyplot(fig)
    st.write('**Insight :**')
    st.write('Skor kredit peminjaman adalah angka yang digunakan untuk menilai kelayakan kredit seseorang atau kemampuan individu untuk membayar kembali pinjaman. jika semakin tinggi nilai skor kredit seseorang maka dia melakukan pembayaran utang sebelumnya tepat waktu. berdasarkan chart, kebanyakan kredit skor peminjam berada disekitar 600 hingga 700 yang mana individu tersebut memiliki kelayakan kredit yang bagus.')



    st.write('### Apakah orang yang menyewa tempat tinggal lebih banyak yang ingin melakukan peminjaman daripada yang sudah memiliki rumah sendiri?  ')
    fig = plt.figure(figsize=(10,8))
    sns.countplot(x='person_home_ownership',data=data,palette='muted')
    st.pyplot(fig)
    st.write('**Insight :**')
    st.write('berdasarkan chart, kebanyakan orang yang ingin melakukan peminjaman adalah orang yang masih menyewa tempat tinggal dan kredit rumah.')



    st.write('### Untuk tujuan apa kebanyakan orang akan melakukan peminjaman')
    fig = plt.figure(figsize=(12,8))
    sns.countplot(
    data=data,            
    x='loan_intent',             
    order=data['loan_intent'].value_counts().index, 
    palette="viridis"              
    )
    st.pyplot(fig)

    st.write('**Insight :**')
    st.write('berdasarkan dataset, kebanyakan orang biasanya akan melakukan peminjaman untuk tujuan pendidikan dan kesehatan. pendidikan dan kesehatan merupakan 2 hal yang sangat penting sehingga orang-orang akan melakukan peminjaman apabila terdesak.')


    # #plotly
    # st.write('### Relation Between Overall vs Value EUR')
    # fig = px.scatter(data, x='ValueEUR', y='Overall')
    # st.plotly_chart(fig)

if __name__ == '__main__':
    run()