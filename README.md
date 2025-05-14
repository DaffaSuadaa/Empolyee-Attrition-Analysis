# Submission Pertama: Menyelesaikan Permasalahan Human Resources

## Business Understanding
Jaya Jaya Maju adalah perusahaan multinasional dengan lebih dari 1000 karyawan. Meskipun telah beroperasi sejak tahun 2000 dan mengalami pertumbuhan signifikan, perusahaan menghadapi tantangan serius dalam mengelola dan mempertahankan karyawan, yang ditandai dengan tingginya tingkat attrition (lebih dari 10%).


### Permasalahan Bisnis

Attrition rate yang tinggi menimbulkan biaya besar bagi perusahaan, sementara manajemen belum mengetahui secara jelas faktor-faktor penyebabnya dan belum memiliki sistem dashboard yang memadai untuk memantau kondisi karyawan secara komprehensif dan real-time.


### Cakupan Proyek

1. Mengidentifikasi faktor-faktor kunci yang berkontribusi terhadap attrition karyawan menggunakan data historis.
2. Membuat model prediktif yang dapat memprediksi kemungkinan karyawan akan keluar.
3. Membuat dashboard analitik yang mudah dipahami oleh tim HR untuk membantu mereka memantau kondisi karyawan dan mengambil tindakan preventif.


### Persiapan

Sumber data: [Dataset Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)


## Setup Environment
1. Ekstrack Folder .zip

Ekstrak file attrition-analysis.zip, berikut tampilan struktur folder setelah di ekstrack:

```
attrition-analysis/
├── Attrition_Analysis_Dicoding.ipynb     
├── cleaned_employee_data.csv            
├── employee_data.csv                     
├── random_forest_model.joblib          
├── daffa_suada_i9ug-dashboard.png       
├── link-dashboard.txt                     
├── requirements.txt                      
├── README.md                             
```
2. Buat setup environtment dan aktifkan dengan kode berikut :
```
conda create --name attrition-env python=3.11
conda activate attrition-env
```
> Note : Karena requirement.txt berada dalam attrition-analysis maka :
```
cd attrition-analysis
```
```
pip install -r requirements.txt
```

3. Jalankan notebook
```
Attrition_Analysis_Dicoding.ipynb
```
--- 
### Cara Menjalankan prediction (Lanjutan)
4. Jalankan prediction di terminal dengan kode berikut:
```
python prediction.py
```
Note : Data testing yang terdapat pada prediction dapat di ubah sesuai dengan kebutuhan (hal ini dapat mempengaruhi prediksi yang akan di tampilkan)

## Business Dashboard
Link : https://lookerstudio.google.com/reporting/b6501916-f125-44e6-9e09-83bd677ea6d4

<img width="809" alt="Screen Shot 2025-05-01 at 18 11 18" src="https://github.com/user-attachments/assets/28ea1566-9672-460b-91a2-985819723022" />


## Conclusion

Dari infromasi yang telah saya paparkan, ada bebearapa kesimpulan yang dapat saya sampaikan. 
1. Attrition paling tinggi ada pada department Sales, dengan presentase sebesar 20%, diikuti Hr sebesar 15,79% dan R&D 15.26%. Jika di lihat dari Environment dan Statisfaction mereka cenderung nyaman, namun Jika di lihat dari Work Life Balance masih cenderung biasa saja, Bahkan dilihat dari datanya, karyawan yang sering lembur lebih berkecenderungan untuk keluar.
2. Jika dilihat dari presentasi rata rata karyawan yang attrition mereka cenderung mendapatkan income yang lebih sedikit. Hal ini menunjukkan bahwa kompensasi menjadi salah satu faktor potensial penyebab attrition.
3. Perusahaan dapat lebih memperhatikan pegawainya yang rentang usianya mulai dari 25 - 35 tahun, terutama pada karyawan pria yang belum menikah.

### Rekomendasi Action Items (Optional)

Berdasarkan kesimpulan di atas, berikut adalah beberapa rekomendasi yang dapat dilakukan oleh perusahaan untuk mengurangi tingkat pergantian karyawan:
1. Perusahaan dapat mengevaluasi beban kerja, sistem infsentif dan peluang perkembangan karir pada setiap departement, memberikan training skill pada tiap departemen, dan dapat melakukan exit interview pada karyawan yang keluar untuk mengetahui secara spesifik mengapa mereka keluar.

2. Menerapkan batas maksimal overtime serta memberikan kompensasi lembur yang adil pada setiap karyawan, memberikan karyawan program program yang dapat meningkatkan kesejahteraan karyawan seperti memberi program olahraga, memberikan jam kerja yang fleksibel, dan kenaikan gaji karyawan berdasarkan performa.

3. Perusahaan dapat mereview gaji dan tunjangan yang di berikan terutama pada karyawan yang memiliki performa tinggi, memberikan insentif berbasis kinerja seperti bonus untuk meningkatkan motifasi karyawan.

4. Untuk pegawai dengan usia muda perusahaan dapat membuat program mentoring atau career path, mengadakan review berkala yang membahas pertumbuhan karir dan keterampilan. 
