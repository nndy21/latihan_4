import random

# Meminta input dari pengguna untuk menentukan jumlah bilangan (n)
while True:
    try:
        n_input = input("Masukkan jumlah bilangan acak yang ingin ditampilkan (n): ")
        # Mengubah input menjadi integer
        n = int(n_input)
        # Memastikan n adalah bilangan positif
        if n > 0:
            break
        else:
            print("Masukkan bilangan bulat positif.")
    except ValueError:
        # Menangani jika input bukan angka
        print("Input tidak valid. Harap masukkan bilangan bulat.")

print(f"\nMenampilkan {n} bilangan acak yang lebih kecil dari 0.5:")

# Menggunakan loop for untuk mengulang sebanyak n kali
for i in range(n):
    # Menggunakan loop while untuk memastikan bilangan yang dihasilkan < 0.5
    bilangan_acak = random.random()
    while bilangan_acak >= 0.5:
        bilangan_acak = random.random()
    print(f"Bilangan acak ke-{i + 1}: {bilangan_acak:.4f}")
