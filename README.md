# PROJECT CASHIER

## A. Latar Belakang Masalah
Andi adalah pemilik supermarket yang ingin membuat sistem kasir self-service di supermarketnya. Pelanggan dapat memasukkan item yang dibeli, jumlahnya, harga, dan menggunakan fitur lainnya.

## B. Tools
### a. Language
- Python
### b. Libraries
- tabulate

## C. Requirement / Objectives Program
1. Membuat id customer
   - `generate_transaction_id = Transaction()`
2. Menambahkan item:
   - `add_item([<nama item>, <jumlah item>, <harga per item>])`
3. Update item jika terjadi kesalahan:
   - Update nama item: `update_item_name(<nama item>, <update nama item>)`
   - Update jumlah item: `update_item_qty(<nama_item>, <update jumlah item>)`
   - Update harga item: `update_item_price (<nama_item>, <update harga item>)`
4. Menghapus item:
   - `delete_item(<nama_item>)`
5. Check apabila ada kesalahan input:
   - `check_order()`
6. Menghitung total belanja:
   - `total_price()`
## Objectives
- Menggunakan Python untuk membuat program kasir otomatis yang memungkinkan pengguna untuk melakukan operasi tambah, update, hapus, reset transaksi, check order, dan melakukan pembayaran.
- Memberikan pengalaman pengguna yang baik dengan antarmuka yang interaktif dan pemberian informasi yang jelas.
- Memastikan keamanan data dan menjaga integritas transaksi selama proses.
## D. Flowchart program
[link flowchart : https://app.diagrams.net/#G1zNwEM2BBjJyKWyv1jfpzTf8P8ytEfKnO ]
![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/e93cb430-78a5-420d-8735-4abeed08bd95)


## E. Function atau atribut yang dibuat

| No  | Function             | Deskripsi                             |
| --- | -------------------- | ------------------------------------- |
| 1   | generate_transaction_id | Process: generate id transaksi    |
| 2   | add_item()           | Input: Nama item, Jumlah item, Harga per item |
| 3   | update_item()        | Input: Pilih menu update             |
| 4   | update_item_name()   | Input: Update nama item              |
| 5   | update_item_qty()    | Input: Update jumlah item            |
| 6   | update_item_price()  | Input: Update harga item             |
| 7   | delete_item()        | Menghapus item                        |
| 8   | reset_transaction()  | Reset transaction                    |
| 9   | check_order()        | Display: Menampilkan item, jumlah item, dan harga per item |
| 10  | total_price()        | Display: Menampilkan keseluruhan item beserta total harganya |


## F. Test Case

1. **Test 1**
   - User menambahkan dua item baru menggunakan `add_item()`.
     - Nama item: Pasta Gigi, Qty: 2, Harga: 5000
     - ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/67ce5b60-7cae-4773-acf2-4dcb8da5fb38)
     - Nama item: Body Lotion, Qty: 3, Harga: 12000
     - ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/d697c3ec-a9b7-42e5-bfa9-4237fa612392)

    

2. **Test 2**
   - Menggunakan `update_item()` dan `update_item_name()` untuk memperbaiki nama item yang salah.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/7da16a34-f19a-4fb0-8973-6797a69dd55d)

3. **Test 3**
   - Menggunakan `update_item()` dan `update_item_qty()` untuk memperbaiki jumlah item yang salah.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/341e4855-561b-4bc4-9296-8b7c81eae99b)


4. **Test 4**
   - Menggunakan `update_item()` dan `update_item_price()` untuk memperbaiki harga item yang salah.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/25234a06-393d-4d8d-86c0-9bc77f34463d)


5. **Test 5**
   - Menggunakan `delete_item()` untuk menghapus item yang salah dimasukkan.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/8d5c3ee1-cff9-475e-8223-acce74a3b60f)

6. **Test 6**
   - Menggunakan `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/998bb389-ed32-4cdf-878f-96e7c04d442d)

7. **Test 7**
   - Menggunakan `check_order()` untuk memeriksa item yang telah diinputkan setelah di-reset.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/77208d07-77f3-450e-8d1b-7e9b2fa04f4a)

8. **Test 8**
   - Menggunakan `total_price()` untuk menghitung total belanja.
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/708903c1-f44d-4037-b0d6-39e39688f99c)

# Kesimpulan

## Sistem Kasir Sederhana

Program ini adalah implementasi sederhana dari sistem kasir yang memungkinkan pengguna untuk menambah, mengupdate, menghapus item, serta melakukan berbagai operasi terkait transaksi seperti reset transaksi, pemeriksaan pesanan, dan pembayaran. Program ini menggunakan Python dan memiliki antarmuka teks melalui terminal.

## Fitur Utama

1. **Penanganan Transaksi:**
   - Program ini menyediakan fungsi untuk menambahkan item ke dalam transaksi, mengupdate item, menghapus item, dan mereset transaksi.
   - Pengguna dapat memasukkan nama item, jumlah, dan harga per item saat menambahkan item.
   - Untuk mengupdate item, pengguna dapat memilih opsi untuk mengupdate nama item, jumlah, atau harga per item.
   - Program juga memungkinkan pengguna untuk menghapus item yang telah ditambahkan.

2. **Pengecekan dan Struk Pembayaran:**
   - Terdapat fungsi untuk menampilkan keseluruhan item yang telah ditambahkan untuk memeriksa pesanan.
   - Fungsi lainnya menghitung total harga transaksi dengan mempertimbangkan diskon berdasarkan jumlah belanja.
   - Program mencetak struk pembayaran dengan rincian item, total harga sebelum diskon, diskon yang diterima, total harga setelah diskon, jumlah uang yang dibayarkan, dan kembalian (jika ada).

3. **Diskon Berdasarkan Jumlah Belanja:**
   - Program memberikan diskon berdasarkan jumlah total belanja, dengan batasan diskon tertentu untuk setiap kisaran total belanja.

4. **Manajemen Transaksi:**
   - Transaksi dapat di-reset, sehingga pengguna dapat memulai transaksi baru setelah pembayaran selesai.

5. **Antarmuka Pengguna:**
   - Pengguna dapat memilih berbagai opsi melalui antarmuka teks yang disediakan di terminal.
   - Program memberikan umpan balik jika terjadi kesalahan input.

## Cara Penggunaan

1. Pastikan Python terpasang di sistem Anda.
2. Instal modul tabulate dengan menjalankan perintah pip install tabulate.
3. Jalankan program dengan menjalankan file yang berisi kode (`main.py`).
4. Pilih menu yang sesuai dengan tugas yang ingin dilakukan (tambah item, update item, hapus item, reset transaksi, cek pesanan, bayar, atau keluar).
5. Ikuti petunjuk yang diberikan oleh program untuk setiap operasi yang dipilih.
6. Setelah selesai, program dapat dihentikan dengan memilih opsi keluar.

## Catatan

- Pastikan untuk memberikan input sesuai dengan petunjuk yang diberikan oleh program.
- Jika terjadi kesalahan, program memberikan pesan error yang menjelaskan penyebab kesalahan.
- Program ini memberikan layanan sederhana untuk kasir dengan fungsionalitas dasar untuk mengelola transaksi dan pembayaran.

