from ProjectKasir import Transaction

if __name__ == "__main__":
    transaction = Transaction()

    menu_options = {
        '1': transaction.add_item,
        '2': transaction.update_item,
        '3': transaction.delete_item,
        '4': transaction.reset_transaction,
        '5': transaction.check_order,
        '6': transaction.total_price,
        '7': lambda: print("Terima kasih telah menggunakan program kasir.")
    }
    
    while True:
        if len(transaction.transaction_data) == 0:
            print("")
            print("")
            print("\nPilih menu:")
            print("1. Tambah Item")
            print("7. Keluar")
            choice = input("Masukkan pilihan: ")

            if choice in menu_options:
                if choice == '7':
                    menu_options[choice]()
                    break
                else:
                    menu_options[choice]()
            else:
                print("Pilihan tidak valid.")
        else:
            print("")
            print("")
            print("\nPilih menu:")
            print("1. Tambah Item")
            print("2. Update Item")
            print("3. Hapus Item")
            print("4. Reset Transaksi")
            print("5. Check Order")
            print("6. Bayar")
            print("7. Keluar")
            choice = input("Masukkan pilihan: ")

            if choice in menu_options:
                if choice == '7':
                    menu_options[choice]()
                    break
                else:
                    menu_options[choice]()
            else:
                print("Pilihan tidak valid.")
