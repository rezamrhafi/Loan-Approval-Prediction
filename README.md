# Milestone-2

## Objective
saya adalah seorang data scientist di sebuah BANK, saya diminta untuk membuat sebuah model yang dapat memprediksi seseorang dapat menerima pinjaman sehingga orang yang ingin melakukan pengecekan apakah mereka dapat melakukan peminjaman atau tidak.

---
## Conceptual Problems
### Jelaskan latar belakang adanya bagging dan cara kerja bagging !
Bagging adalah teknik ensemble yang dikembangkan untuk mengatasi masalah performa model prediktif, khususnya untuk model yang memiliki masalah overfitting (seperti Decision Tree) atau model yang kurang stabil. cara kerja dari bagging adalah melibatkan pelatihan beberapa model secara independen dan menggabungkan prediksi mereka melalui perataan atau pemungutan suara

### Jelaskan perbedaan cara kerja algoritma Random Forest dengan algoritma boosting yang Anda pilih !
Random Forest adalah algoritma yang menggunakan metode bagging, di mana ia membuat banyak Decision Tree independen dari subset data yang dihasilkan melalui bootstrapping, dan hasil akhir diperoleh dengan voting mayoritas (untuk klasifikasi) dari semua pohon. Sedangkan XGBoost menggunakan pendekatan boosting, di mana ia membangun pohon secara berurutan. Setiap pohon baru mencoba memperbaiki kesalahan pohon sebelumnya dengan meminimalkan fungsi loss melalui pengoptimalan gradien.

### Jelaskan apa yang dimaksud dengan Cross Validation !
Cross-validation adalah teknik evaluasi model yang digunakan untuk menilai kemampuan generalisasi suatu model terhadap data baru dengan cara membagi data menjadi beberapa subset. Proses ini bertujuan untuk mengurangi overfitting atau underfitting dan memastikan model memiliki performa yang konsisten.

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
