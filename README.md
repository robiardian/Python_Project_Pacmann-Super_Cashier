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
   - `Trnsct_123 = Transaction()`
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

## D. Flowchart program
[link flowchart]
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
     - Nama item: Body Lotion, Qty: 3, Harga: 12000
   Output :
   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/a4204d02-ff56-4cdb-b218-1ff11a4491e3)

   ![image](https://github.com/robiardian/Python_Project_Pacmann-Super_Cashier/assets/75802585/83556174-5271-46b5-88c5-690412f874d6)

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

## Kesimpulan

1. Beberapa method dalam kode:
   - `add_item()`: Menambahkan item baru ke dictionary.
   - `update_item()`: Membuka menu update item dan memungkinkan perubahan nama, jumlah, atau harga item.
   - `delete_item()`: Menghapus item dari dictionary.
   - `reset_transaction()`: Menghapus semua item dan transaction ID.
   - `check_order()`: Menampilkan daftar item dan total harga.
   - `total_price()`: Menghitung total harga, menerapkan diskon, dan menampilkan struk pembayaran.

2. Beberapa menu dalam kode:
   - Tambah Item
   - Update Item
   - Hapus Item
   - Reset Transaksi
   - Check Order
   - Bayar
   - Keluar

Catatan: Ketika daftar belanja kosong, hanya opsi "Tambah Item" dan "Keluar" yang tersedia. Setelah ada item dalam daftar belanja, semua menu utama (1-6) beserta "Keluar" akan muncul.
