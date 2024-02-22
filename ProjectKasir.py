from tabulate import tabulate

class Transaction:
    transaction_id = 0  # ID transaksi awal

    def __init__(self):
      """
       Menginisialisasi objek transaksi dengan membuat dictionary untuk menyimpan data transaksi
      dan menghasilkan ID transaksi baru.

      Parameter:
        transaction_data (dic(dic)): penyimpanan data dalam sistem
        transaction_id : id transaksi 
      """
      self.transaction_data = {}
      self.transaction_id = Transaction.generate_transaction_id()


    def generate_transaction_id():
      """
      Mengenerate id transaksi

      Parameter:
        transaction_id (int): id transaksi sebelum transaksi id di reset


      return :
        transaction_id (int) : id transaksi setelah transaksi id di reset

      """
      Transaction.transaction_id += 1
      return Transaction.transaction_id

    def add_item(self):

      """
       menambahkan item baru

       Parameter :
        item_name (str)         : nama item yang ingin ditambahkan
        quantity  (int)         : jumlah item yang ingin ditambahkan
        price_per_item (float)  : harga per item yang ingin ditambahkan


      """
      try:
          item_name = str(input("Nama Item: "))
          quantity = int(input("Jumlah: "))
          price_per_item = float(input("Harga per Item: "))
          self.transaction_data[item_name] = {'quantity': quantity, 'price_per_item': price_per_item}
          print("--------------------------")
          print("Item berhasil ditambahkan.")
          print("--------------------------")

      except ValueError:
          print("Error: Masukan tidak valid. Pastikan jumlah adalah bilangan bulat dan harga adalah bilangan bukan string.")

    def update_item(self):
      """
      masuk ke menu update item

      Parameter :
        item_name (str) : nama item yang ingin dibuah (baik dari nama,jumlah item, dan harga per item)

      """
      try:
          item_name = str(input("Nama Item yang akan diupdate: "))
          if item_name in self.transaction_data:
              print("Pilih opsi update:")
              print("1. Update Nama Item")
              print("2. Update Jumlah Item")
              print("3. Update Harga per Item")
              update_choice = input("Masukkan pilihan: ")

              if update_choice == '1':
                  self.update_item_name(item_name)
              elif update_choice == '2':
                  self.update_item_qty(item_name)
              elif update_choice == '3':
                  self.update_item_price(item_name)
              else:
                  raise ValueError("Pilihan tidak valid.")
          else:
              raise ValueError("Item tidak ditemukan.")
      except ValueError as ve:
          print("Error:", ve)

    def update_item_name(self, item_name):
      """
      Mengupdate nama dari item yang telah di tambahkan

      Parameter :
        item_name (str) : nama item yang ingin diupdate
        new_name (str)  : nama baru item yang diinginkan

      """
      try:
          new_name = input ("Nama Item Baru: ")
          self.transaction_data[new_name] = self.transaction_data.pop(item_name)
          print("----------------------------")
          print("Nama item berhasil diupdate.")
          print("----------------------------")
      except KeyError:
          print("Error: Item tidak ditemukan.")

    def update_item_qty (self, item_name):
      """
      Mengupdate jumlah dari item yang telah ditambahkan

      Parameter :
        item_name (str)    : nama pada item yang ingin diubah
        new_quantity (int) : jumlah baru item yang ingin diubah

      """
      try:
          new_quantity = int(input("Jumlah Item Baru: "))
          self.transaction_data[item_name]['quantity'] = new_quantity
          print("------------------------------")
          print("Jumlah item berhasil diupdate.")
          print("------------------------------")
      except ValueError:
          print("Error: Masukan tidak valid. Pastikan jumlah adalah bilangan bulat.")

    def update_item_price(self, item_name):
      """
      Mengupdate harga dari item yang telah ditambahkan

      Parameter :
        item_name (str)   : nama pada item yang ingin diubah
        new_price (float) : harga baru dari item yang ingin diubah

      """
      try:
          new_price = float(input("Harga per Item Baru: "))
          self.transaction_data[item_name]['price_per_item'] = new_price
          print("-----------------------------")
          print("Harga item berhasil diupdate.")
          print("-----------------------------")
      except ValueError:
          print("Error: Masukan tidak valid. Pastikan harga adalah bilangan.")

    def delete_item(self):
      """
      Menghapus salah satu item yang telah ditambahkan

      Parameter :
        item_name (str) : nama item yang ingin dihapus

      """
      try:
        item_name = str(input("Nama Item yang akan dihapus: "))
        if item_name in self.transaction_data:
          del self.transaction_data[item_name]
          print("----------------------")
          print("Item berhasil dihapus.")
          print("----------------------")
        else:
          raise ValueError("Item tidak ditemukan.")
      except ValueError as ve:
        print("Error:", ve)

    def reset_transaction(self):
      """
      Menghapus seluruh item yang telah ditambahkan

      Parameter :
        transaction_data (dic(dic)) : data item
        transaction_id (int) : id transaksi

      """
      self.transaction_data = {}
      self.transaction_id = Transaction.generate_transaction_id()  # Generate  transaction id yang baru
      print("----------------------------")
      print("Transaksi berhasil di-reset.")
      print("----------------------------")

    def check_order(self):
      """
      Menampilkan keseluruhan item yang telah ditambahkan untuk mengecek item

      Parameter :
        item_name (str) : nama item yang telah ditambahkan
        quanity (int) : jumlah item
        price_per_item (float) : harga item

      """
      try:
          data = []

          if not self.transaction_data:
              raise ValueError("Tidak ada item dalam transaksi.")

          if all(item_name.strip() and isinstance(item['quantity'], (int, float)) and isinstance(item['price_per_item'], (int, float))
          and item['quantity'] > 0 and item['price_per_item'] > 0 for item_name, item in self.transaction_data.items()):
              print("----------------------------- Pemesanan sudah benar ---------------------------")

          try:
              for item_name in self.transaction_data.keys():
                  if not item_name.strip():
                      raise ValueError("--- terdapat kesalahan nama item atau jumlah item atau harga item ---")
                  if self.transaction_data[item_name]['quantity'] == 0:
                      raise ValueError("--- terdapat kesalahan nama item atau jumlah item atau harga item ---")
                  if self.transaction_data[item_name]['price_per_item'] == 0:
                      raise ValueError("--- terdapat kesalahan nama item atau jumlah item atau harga item ---")
              print("Tidak ada masalah dengan transaksi.")
          except ValueError as ve:
              print("Error:", ve)


          for item_name, item_info in self.transaction_data.items():
              total_price = item_info['quantity'] * item_info['price_per_item']
              data.append([item_name, item_info['quantity'], item_info['price_per_item'], total_price])

          print(tabulate(data, headers=['Nama Item', 'Jumlah', 'Harga per Item', '         Total Harga         '], tablefmt="github" , numalign="center"))

      except ValueError as ve:
          print("Error:", ve)

    def total_price(self):
      """
      Menampilkan kesuluruhan item dan total harga yang harus dibayar, diskon, dan juga struk pembayaran

      Parameter :
        item_name (str) : nama item yang telah ditambahkan
        quantity (int) : jumlah item yang telah ditambahkan
        price_per_item (float) : harga per item dari item yang telah di tambahkan

      """
      try:
          total_before_discount = sum(item['quantity'] * item['price_per_item'] for item in self.transaction_data.values())
          discount = 0

          # mengaplikasikan diskon
          if total_before_discount > 500000:
              discount = total_before_discount * 0.1
          elif total_before_discount > 300000:
              discount = total_before_discount * 0.08
          elif total_before_discount > 200000:
              discount = total_before_discount * 0.05

          total_after_discount = total_before_discount - discount

          # data untuk ditampilkan ke tabel
          data = []
          for item_name, item_info in self.transaction_data.items():
              total_price = item_info['quantity'] * item_info['price_per_item']
              data.append([item_name, item_info['quantity'], item_info['price_per_item'], total_price])

          # menampilkan struk belanja menggunakan tabulate
          print("============================== Daftar Item Belanjaan ==========================")
          print("================================= TOKO ANDI ==================================")
          # menampilkan transaction id
          print("-----------------Nomor ID Transaksi:", self.transaction_id )
          print(tabulate(data, headers=['Nama Item', 'Jumlah', 'Harga per Item', '         Total Harga         '], tablefmt="github" , numalign="center"))
          print("==============================================================================")
          print("Total harga sebelum diskon: Rp.", total_before_discount)
          print("Diskon yang didapat: Rp.", discount)
          print("Total harga setelah diskon: Rp.", total_after_discount)

          # opsi pembayaran atau pembatalan
          while True:
              choice = input("Pilih:\n1. Bayar\n2. Cancel\nMasukkan pilihan: ")
              if choice == '1':  # jika user memilih untuk membayar
                  amount_paid = float(input("Masukkan jumlah uang yang dibayarkan: "))
                  change = amount_paid - total_after_discount
                  if change >= 0:
                      # menampilkan struk akhir sebelum mereset transaksi
                      print("")

                      print("============================== Struk Belanja  ==============================")
                      print("================================ TOKO ANDI =================================")
                      print("----------------Nomor ID Transaksi:", self.transaction_id)
                      print(tabulate(data, headers=['Nama Item', 'Jumlah', 'Harga per Item', '         Total Harga         '], tablefmt="github" , numalign="center"))
                      print("============================================================================")
                      print("Total harga setelah diskon: Rp.", total_after_discount)
                      print("Uang yang dibayarkan: Rp.", amount_paid)
                      print("Uang kembalian: Rp.", change)
                      print("")
                      print("----- Transaksi selesai ------")
                      print("")
                      self.reset_transaction()  # mereset transaksi setelah pembayaran
                      break
                  else:
                      print("Maaf, jumlah uang yang Anda bayarkan kurang.")
              elif choice == '2':  # jika user memilih untuk batal
                  print("Transaksi dibatalkan.")
                  self.reset_transaction()  # Reset transaksi setelah pembatalan
                  break
              else:
                  print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")
      except ValueError as ve:
          print("Error:", ve)