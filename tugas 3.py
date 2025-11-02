import sys

def atm_simulation():
    
    balance = 1000000
    
    print("Selamat datang di atm sederhana")
    print(f"Saldo anda saat ini : Rp {balance:,.0f}")
    
    while True:
        print("\nmenu Transaksi")
        print("1. Tarik Tunai")
        print("2. Cek saldo")
        print("3. Keluar")
        
        choice = input("Pilih opsi (1/2/3): ")
        
        if choice == '1':
            try:
                amount_to_withdraw = int(input("masukan jumlah penarikan: Rp "))
                
                if amount_to_withdraw <= 0:
                    print("Jumlah Penarikan harus lebih dari 0")
                elif amount_to_withdraw > balance:
                    print(f"Saldo tidak mencukupi. Saldo Anda: Rp {balance:,.0f}")
                else:
                    balance -= amount_to_withdraw
                    print(f"Penarikan sebesar Rp {amount_to_withdraw:,.0f}")
                    print("Penarikan Berhasil !")
                    print(f"Saldo Anda sekarang : Rp {balance:,.0f}")
                    
                    # akan di loop ketika saldonya telah habis
                    if balance == 0:
                        print("Saldo Anda telah habis. Silahkan isi kembali")
                        break
                    
            except ValueError:
                print("input tidak valid. Harap masukan Angka.")
                
        elif choice == '2':
            print(f"Saldo Anda saat ini: Rp {balance:,.0f}")
        elif choice == '3':
            print("Terima kasih telah menggukan ATM kami.")
            # akan keluar program dengan sendirinya
            sys.exit()
            
        else:
            print("Pilihan tidak valid. mohon masukan Angka 1/2/3")


if __name__ == "__main__":
    atm_simulation()
