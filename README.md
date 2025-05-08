# Telecommunication Company Customer Churn Prediction

## Repository Outline
1. description.md - Penjelasan gambaran umum project
2. notebook.ipynb - Notebook yang berisi pengolahan data dengan python
3. notebook_inference.ipynb - Notebook yang berisi hasil prediksi data inferens
4. correlation_cal.py - File python yang berisi function perhitungan korelasi
5. outlier_detection.py - File python yang berisi function untuk mengecek outlier.
6. url.txt - Berisi url link dataset dan huggingface.co
7. customer_churn_telecom_services.csv - Dataset yang digunakan dalam program
8. README.md - Penjelasan bagaimana projek dikerjakan.
9. deployment - Folder berisi file python dan model yang akan digunakan saat deployment menggunakan website huggingface.co
    - app.py - File python yang menjadi jembatan antara file eda.py dan predictio.eda.
    - eda.py - File python yang menunjukan hasil analisis eda yang dilakukan dalam sebuah webpage.
    - prediction.py - File python yang berupa form untuk memasukan data baru untuk prediksi apakah pelanggan akan churn atau tidak.
    - best_rf_model.pkl - File ini menyimpan hasil model terbagus yaitu model Random Forest Classifier
    - requirements.txt - File ini mengandung semua library yang digunakan pada folder deployment.


## Problem Background
**Latar Belakang:**<br>
Dalam sebuah perjalanan bisnis, kita tentu saja ingin membangun bisnis dengan pelanggan yang setia agar mereka terus menerus melakukan transaksi dengan kita. Tetapi ada saja suatu ketika dimana pelanggan mangambil keputusan untuk tidak melakukan bisnis dengan kita lagi. Hal ini dinamakan Churn. Perusahaan yang memiliki nilai churn tinggi akan menemukan bahwa mempertahankan bisnis itu sangat sulit jika pelanggan terus memutuskan untuk tidak melakukan bisnis dengan mereka. Begitu juga halnya untuk bisnis telecom. Sebagai salah satu pegawai data analyst di Telecom Inc., saya diminta oleh pihak perusahaan untuk membantu mereka mencari tahu bagian apa yang bisa mereka kembangkan untuk meminimalkan kemungkinan pelanggan akan churn. Selain itu perusahaan ingin mencari tahu untuk kedepannya, apakah pelanggan baru akan melakukan churn, sehingga saya sebagai data analyst diminta untuk membuat sebuah model yang dapat memprediksi apakah pelanggan akan churn atau tidak.

**Problem Statement:**<br>
Bagaimana cara menurunkan tingkat Churn sebesar 10% dalam 6 bulan kedepan menggunakan hasil analisis data untuk mencari bagian layanan yang bisa diperbagus?


## Project Output
Output project ini adalah sebuah model prediksi yang dapat melakukan prediksi apakah pelanggan akan Churn atau tidak yang akan di-deploy menggunakan huggingface.co


## Data
Sumber Data: https://www.kaggle.com/datasets/kapturovalexander/customers-churned-in-telecom-services<br><br>
Jumlah Kolom: 20 <br>
Jumlah Baris: 7043 <br>
Missing Value: 11 pada kolom TotalCharges <br>
Kategorikal Kolom: 17 <br>
Numerikal Kolom: 3<br><br>
**Deskripsi Kolom**
|Kolom|Tipe Data|Deskripsi| 
|-----|---------|---------|
|`gender`|object|Kolom berisi deskripsi kelamin Male atau Female.|
|`SeniorCitizen`|int|Mengindikasikan apakah pelanggan tergolong Senior (1 = Yes, 0 = No).|
|`Partner`|object|Menunjukan apakah pelanggan memiliki pasangan (Yes/No).|
|`Dependents`|object|Menunjukan apakah pelanggan memiliki dependents (Yes/No).|
|`tenure`|int|Berapa bulan pelanggan sudah menggunakan service perusahaan.|
|`PhoneService`|object|Menunjukan apakah pelanggan memiliki Phone Service (Yes/No).|
|`MultipleLines`|object|Menunjukan apakah pelanggan memiliki lebih dari satu saluran telepon (Yes/No/No phone service).|
|`InternetService`|object|Tipe internet yang digunakan (DSL/Fiber Optic/No).|
|`OnlineSecurity`|object|Apakah pelanggan memiliki layanan online security (Yes/No/No Internet Service).|
|`OnlineBackup`|object|Apakah pelanggan memiliki layanan online backup (Yes/No/No Internet Service).|
|`DeviceProtection`|object|Apakah pelanggan memiliki layanan perlindungan device (Yes/No/No Internet Service).|
|`TechSupport`|object|Apakah pelanggan memiliki layanan tech Support (Yes/No/No Internet Service).|
|`StreamingTV`|object|Apakah pelanggan memiliki layanan Streaming TV (Yes/No/No Internet Service).|
|`StreamingMovies`|object|Apakah pelanggan memiliki layanan Streaming Movies (Yes/No/No Internet Service).|
|`Contract`|object|Tipe kontrak (Month-to-month/One year/Two year).|
|`PaperlessBilling`|object|Apakah pelanggan memiliki paperless billing (Yes/No).|
|`PaymentMethod`|object|Tipe pembayaran yang digunakan (Electronic check/Mailed check/Bank transfer/Credit card).|
|`MonthlyCharges`|int|Biaya tagihan bulanan yang dibayar pelanggan.|
|`TotalCharges`|int|Biaya tagihan total yang sudah dibayar.|
|`Churn`|object|Menunjukan apakah pelanggan Churn atau tidak (Yes/No).|

## Method
Metode untuk memecahkan masalah prediksi yang digunakan adalah supervised machine learning model:
1. K-Nearest Classifier
2. Support Vector Classifier
3. Decision Tree Classifier
4. Random Forest Classifier
5. XGBoost

## Stacks
Bahasa Pemrograman: Python<br>
<br>Library:<br>
1. pandas
2. matplotlib
3. missingno
4. seaborn
5. importlib
6. sklearn
7. xgboost

<br>
Tools dan Source lain: <br>
1. huggingface.co
<br>

<br>File Tambahan:
1. correlation_calc (Python file milik sendiri untuk menghitung korelasi)
2. outlier_detection (Python file milik sendiri untuk mencari outlier)

## Reference

- ### Dataset:
    [Dataset](https://www.kaggle.com/datasets/kapturovalexander/customers-churned-in-telecom-services)

- ### Referensi:
    - [Apa Itu Churn Rate dan Bagaimana Cara Menguranginya?](https://mekari.com/blog/penjelasan-churn-rate/)
    - [Memahami Churn Rate: Apa Itu dan Mengapa Penting?](https://www.idxchannel.com/economics/memahami-churn-rate-apa-itu-dan-mengapa-penting)
    - [Seluk-beluk Customer Churn Rate dan 3 Cara Ampuh Menguranginya](https://glints.com/id/lowongan/churn-rate-adalah/)

 - ### Deploy:
    [Link Deployment](https://huggingface.co/spaces/ray-dion/Milestones-2)
---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)