# saham_app

Saham_app adalah aplikasi yang didesain untuk memprediksi harga saham di index Indonesia dengan
menggunakan bantuan machine learning. Prediksi saham ini menggunakan ridge regression yang dilakukan
dengan fitur dataset berupa penurunan atau kenaikan harga selama beberapa bulan terakhir.

Data yang digunakan untuk analisis didapatkan dari google finance. Data di peroleh dan diproses 
di program node.js berupa API yang memberikan data ke program python dalam format array.

## How to use

1. Setup node.js

  Pertama-tama install dependency dengan masuk ke directory api lalu run
    `npm install`
    
  selanjutnya jalankan api node.js dengan command
    `node index.js`
   
   
2. Jalankan program python

  Terdapat dua menu untuk menjalankan aplikasi yaitu terminal dan web. Namun hingga saat ini
  aplikasi web masih belum selesai sehingga aplikasi baru bisa dijalankan di terminal
  
  jalankan aplikasi dengan masuk ke direktori src_terminal lalu jalankan
  `python3 main_terminal.py`
  
  jika gagal karena ada dependency yang belum terinstall maka install dengan comman
  `pip3 install x` dimana x adalah package yang diperlukan
