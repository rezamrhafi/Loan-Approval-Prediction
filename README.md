# Loan Approval Prediction 💡

Repositori ini berisi project prediksi konversi menggunakan beberapa model (KNN, SVM, Decision Tree, Random Forest, XGBoost) klasifikasi dengan base parameter, lalu model terbaik selanjutnya dilakukan hyperparameter tuning, hasilnya model ini menggunakan XGBoost sebagai model prediksi. Project ini bertujuan untuk menerapkan model machine learning untuk memprediksi konversi berdasarkan dataset yang tersedia. Repositori ini mencakup file Jupyter Notebook yang menjelaskan proses secara menyeluruh, mulai dari eksplorasi data hingga percobaan model menggunakan unseen data.

---
## Project Overview 📝

Dalam proyek ini, saya menggunakan beberapa model klasifikasi dengan base parameter, lalu model terbaik selanjutnya dilakukan hyperparameter tuning untuk menganalisis data dan membangun model prediksi konversi. Beberapa langkah utama yang dicakup dalam proyek ini adalah:

1. **Import Libraries dan Eksplorasi Data**:
    - Memuat dataset dan melakukan eksplorasi awal untuk memahami struktur dan karakteristik data.

2. **Preprocessing Data**:
    - Melakukan pembersihan dan persiapan data, termasuk penanganan outlier dan imputasi nilai yang hilang.

3. **Pengembangan Model**:
    - Membangun dan melatih model lima model klasifikasi untuk memprediksi konversi.

4. **Evaluasi Model**:
    - Menggunakan metrik evaluasi untuk menilai kinerja model.

5. **Hyperparameter Tuning**:
   - Melakukan hyperparameter tuning menggunakan model terbaik.
     
7. **Evaluasi Model**:
   - Melakukan evaluasi terhadap model yang sudah dituning
     
9. **Pengambilan Keputusan untuk Model dan Bisnis**:
    - Mengambil keputusan terhadap model dan untuk bisnis

---

## Latar Belakang Masalah 🧐

Dalam industri perbankan, pemberian pinjaman merupakan salah satu layanan utama yang berkontribusi terhadap profitabilitas dan pertumbuhan bisnis. Namun, proses penentuan kelayakan kredit bagi calon peminjam sering kali menjadi tantangan, terutama dalam mengurangi risiko kredit macet dan meningkatkan efisiensi operasional.

Seiring dengan perkembangan teknologi dan pemanfaatan data dalam pengambilan keputusan, penggunaan model prediktif berbasis machine learning dapat membantu bank dalam menilai kemungkinan seorang calon peminjam mendapatkan persetujuan pinjaman. Model ini akan menganalisis berbagai variabel seperti riwayat kredit, penghasilan, pekerjaan, dan faktor lainnya untuk memberikan prediksi yang akurat mengenai kelayakan peminjam.

Dengan adanya model prediktif ini, calon peminjam juga dapat melakukan pengecekan awal mengenai kemungkinan mereka mendapatkan pinjaman sebelum mengajukan permohonan resmi. Hal ini tidak hanya meningkatkan transparansi bagi nasabah tetapi juga membantu bank dalam mengoptimalkan proses persetujuan kredit, mengurangi risiko kredit macet, serta meningkatkan kepuasan pelanggan.

Oleh karena itu, pengembangan model prediksi kelayakan pinjaman ini menjadi langkah strategis dalam meningkatkan efisiensi dan akurasi proses evaluasi kredit di bank.

---
## Dataset Description
Dataset ini berisi informasi demografis, keuangan, dan riwayat kredit individu. Berikut adalah deskripsi tiap kolom:

| **Column Name**                   | **Data Type** | **Description**                                                                 |
|------------------------------------|---------------|---------------------------------------------------------------------------------|
| **person_age**                    | Float         | Usia individu dalam tahun.                                                     |
| **person_gender**                 | Categorical   | Jenis kelamin individu (\"Male\", \"Female\").                                     |
| **person_education**              | Categorical   | Tingkat pendidikan tertinggi individu.                                         |
| **person_income**                 | Float         | Pendapatan tahunan individu.                                                   |
| **person_emp_exp**                | Integer       | Lama pengalaman kerja dalam tahun.                                             |
| **person_home_ownership**         | Categorical   | Status kepemilikan rumah (\"Rent\", \"Own\", \"Mortgage\").                         |
| **loan_amnt**                     | Float         | Jumlah pinjaman yang diminta.                                                  |
| **loan_intent**                   | Categorical   | Tujuan pinjaman (\"Education\", \"Business\", \"Home Improvement\", dll).           |
| **loan_int_rate**                 | Float         | Suku bunga pinjaman.                                                           |
| **loan_percent_income**           | Float         | Rasio jumlah pinjaman terhadap pendapatan tahunan individu.                    |
| **cb_person_cred_hist_length**    | Float         | Panjang riwayat kredit individu dalam tahun.                                   |
| **credit_score**                  | Integer       | Skor kredit individu (biasanya 300-850).                                       |
| **previous_loan_defaults_on_file**| Categorical   | Indikator apakah pernah gagal bayar sebelumnya (\"Yes\"/\"No\").                  |
| **loan_status**                   | Categorical   | Status persetujuan pinjaman (1 = Disetujui, 0 = Ditolak).                      |

---

## Metode yang Digunakan 🛠️

- Statistik Inferensial
- Machine Learning
- Visualisasi Data
- Pemodelan Prediktif

---

## Kesimpulan Analisa 🧠
- setelah membandingkan antara 5 model, model XGBoost memiliki performa yang baik dan stabil meskipun modelnya overfit ringan.
- dengan melakukan hyperparameter tuning, model dapat meningkatkan performanya karena dapat menyesuaikan parameter yang dibutuhkan berdasarkan dataset.
- dengan mengoptimalkan nilai f1-score, model dapat menghindari memprediksi disetujui tetapi tidak harusnya disetujui dan memprediksi tidak disetujui tetapi harusnya disetujui.
- pendidikan dan kesehatan merupakan alasan paling tinggi untuk seseorang melakukan peminjaman.
- rekomendasi 1 : peminjam jika ingin melakukan peminjaman, sebaiknya menyesuaikan jumlah yang ingin dipinjam dengan pemasukan pertahunnya.
- rekomendasi 2 : dengan menggunakan model ini, peminjam dapat mengetahui apakah mereka layak untuk menerima pinjaman berdasarkan data yang mereka berikan.
- rekomendasi 3 : peminjam sebaiknya tidak meminjam terlalu banyak apabila pernah gagal dalam pembayaran pinjaman sebelumnya.
