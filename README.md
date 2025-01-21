# Milestone-2

## Objective
saya adalah seorang data scientist di sebuah BANK, saya diminta untuk membuat sebuah model yang dapat memprediksi seseorang dapat menerima pinjaman sehingga orang yang ingin melakukan pengecekan apakah mereka dapat melakukan peminjaman atau tidak.

## Conceptual Problems
### Jelaskan latar belakang adanya bagging dan cara kerja bagging !
Bagging adalah teknik ensemble yang dikembangkan untuk mengatasi masalah performa model prediktif, khususnya untuk model yang memiliki masalah overfitting (seperti Decision Tree) atau model yang kurang stabil. cara kerja dari bagging adalah melibatkan pelatihan beberapa model secara independen dan menggabungkan prediksi mereka melalui perataan atau pemungutan suara

### Jelaskan perbedaan cara kerja algoritma Random Forest dengan algoritma boosting yang Anda pilih !
Random Forest adalah algoritma yang menggunakan metode bagging, di mana ia membuat banyak Decision Tree independen dari subset data yang dihasilkan melalui bootstrapping, dan hasil akhir diperoleh dengan voting mayoritas (untuk klasifikasi) dari semua pohon. Sedangkan XGBoost menggunakan pendekatan boosting, di mana ia membangun pohon secara berurutan. Setiap pohon baru mencoba memperbaiki kesalahan pohon sebelumnya dengan meminimalkan fungsi loss melalui pengoptimalan gradien.

### Jelaskan apa yang dimaksud dengan Cross Validation !
Cross-validation adalah teknik evaluasi model yang digunakan untuk menilai kemampuan generalisasi suatu model terhadap data baru dengan cara membagi data menjadi beberapa subset. Proses ini bertujuan untuk mengurangi overfitting atau underfitting dan memastikan model memiliki performa yang konsisten.
