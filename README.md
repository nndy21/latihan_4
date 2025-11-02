# latihan_4
Andi Nurcahyana/312510201

# 🎲 Latihan 1

# 🎯 Tujuan Program

Program ini menghasilkan sejumlah n bilangan acak antara 0 sampai 0.5 (tidak termasuk 0.5) berdasarkan input dari pengguna.

# 🔧 Bagian 1: Import Library

```python

import random
```

Mengimpor modul random yang berisi fungsi untuk menghasilkan bilangan acak.

# 📥 Bagian 2: Input Validation dengan Error Handling

```python
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
```

Mekanisme Validasi Input:

```python
    while True: - Loop infinite sampai input valid

    try-except - Menangani error konversi string ke integer

    n = int(n_input) - Mengkonversi input ke integer

    if n > 0: - Memastikan bilangan positif

    break - Keluar loop ketika input valid
```

Contoh Error Handling:
```python
    Input: "abc" → "Input tidak valid. Harap masukkan bilangan bulat."

    Input: "-5" → "Masukkan bilangan bulat positif."

    Input: "3" → Valid, lanjut ke program
```

# 📊 Bagian 3: Konfirmasi Input

```python

print(f"\nMenampilkan {n} bilangan acak yang lebih kecil dari 0.5:")
```

Menampilkan pesan konfirmasi dengan jumlah bilangan yang akan digenerate.

# 🔄 Bagian 4: Generator Bilangan Acak

```python
for i in range(n):
    # Menggunakan loop while untuk memastikan bilangan yang dihasilkan < 0.5
    bilangan_acak = random.random()
    while bilangan_acak >= 0.5:
        bilangan_acak = random.random()
    print(f"Bilangan acak ke-{i + 1}: {bilangan_acak:.4f}")
```

Proses Generasi Bilangan:
```python
    for i in range(n): - Loop sebanyak n kali

    random.random() - Menghasilkan bilangan acak antara [0.0, 1.0)

    while bilangan_acak >= 0.5: - Loop sampai dapat bilangan < 0.5

    {bilangan_acak:.4f} - Format 4 angka desimal
```

# 🎪 Contoh Output Program:

```txt
Masukkan jumlah bilangan acak yang ingin ditampilkan (n): 3

Menampilkan 3 bilangan acak yang lebih kecil dari 0.5:
Bilangan acak ke-1: 0.2345
Bilangan acak ke-2: 0.0891
Bilangan acak ke-3: 0.4567
```

# ⚡ Cara Kerja Random Generation:

```txt
random.random() menghasilkan bilangan desimal antara:
text

0.0 ≤ bilangan < 1.0

Loop while memastikan:
text

0.0 ≤ bilangan < 0.5
```

Contoh proses:
```txt
    Generate: 0.7 → ≥ 0.5 → generate ulang

    Generate: 0.3 → < 0.5 → ✅ gunakan bilangan ini
```

# 📊 Tugas 2

Program ini mensimulasikan perkembangan investasi selama 8 bulan dengan sistem bunga bergulung (compound interest), dimana laba setiap bulan ditambahkan ke modal untuk perhitungan bulan berikutnya.
```python

modal_awal = 100000000  # 100 juta rupiah
modal_sekarang = modal_awal
```

    modal_awal: Nilai investasi awal sebesar Rp 100,000,000

    modal_sekarang: Variabel dinamis yang akan berubah setiap bulan seiring dengan penambahan laba

# 📈 Bagian 2: Data Persentase Laba

```python

persentase_laba_per_bulan = [0, 0, 0.01, 0.01, 0.06, 0.06, 0.06, 0.04]
```

# Breakdown persentase laba per bulan:

    Bulan 1-2: 0% (masa awal belum menghasilkan)

    Bulan 3-4: 1% (stabil di fase awal profit)

    Bulan 5-7: 6% (peningkatan signifikan)

    Bulan 8: 4% (sedikit penurunan)

# 🔄 Bagian 3: Proses Simulasi (Loop)

```python

for bulan in range(8):
    laba_bulan_ini = modal_sekarang * persentase_laba_per_bulan[bulan]
    total_keuntungan += laba_bulan_ini
    modal_sekarang += laba_bulan_ini  # Laba ditambahkan ke modal
```


# Proses yang terjadi setiap bulan:

   Hitung Laba Bulanan:
```txt

Laba = Modal Sekarang × Persentase Laba
```

# Akumulasi Total Keuntungan:

```txt
Total Keuntungan = Total Keuntungan + Laba Bulan Ini

Update Modal (Compound Effect):
text

Modal Baru = Modal Sekarang + Laba Bulan Ini
```

# 📊 Bagian 4: Output Detail per Bulan

```python
print(f"Bulan ke-{bulan + 1}:")
print(f"  Persentase laba: {persentase_laba_per_bulan[bulan]*100:.1f}%")
print(f"  Laba bulan ini: Rp{laba_bulan_ini:,.2f}")
print(f"  Modal akhir bulan: Rp{modal_sekarang:,.2f}")
```

# Contoh output untuk beberapa bulan:

```txt
Bulan 3 (Pertama kali profit):

Bulan ke-3:
  Persentase laba: 1.0%
  Laba bulan ini: Rp1,000,000.00
  Modal akhir bulan: Rp101,000,000.00

Bulan 5 (Laba meningkat):
Bulan ke-5:
  Persentase laba: 6.0%
  Laba bulan ini: Rp6,060,000.00  # Dari modal Rp101,000,000
  Modal akhir bulan: Rp107,060,000.00
```

# 💰 Bagian 5: Hasil Akhir

```python

print(f"Total keuntungan selama 8 bulan: Rp{total_keuntungan:,.2f}")
print(f"Modal akhir setelah 8 bulan: Rp{modal_sekarang:,.2f}")
print(f"Return on Investment (ROI): {(total_keuntungan/modal_awal)*100:.2f}%")
```
Metrik yang dihitung:

    Total Keuntungan: Seluruh laba yang terkumpul dalam 8 bulan

    Modal Akhir: Nilai total investasi di akhir periode

    ROI: Persentase keuntungan terhadap modal awal


# Hasil Output
```python
=== SIMULASI INVESTASI 8 BULAN ===

Modal awal: Rp100,000,000.00

Bulan ke-1:
  Persentase laba: 0.0%
  Laba bulan ini: Rp0.00
  Modal akhir bulan: Rp100,000,000.00

Bulan ke-2:
  Persentase laba: 0.0%
  Laba bulan ini: Rp0.00
  Modal akhir bulan: Rp100,000,000.00

Bulan ke-3:
  Persentase laba: 1.0%
  Laba bulan ini: Rp1,000,000.00
  Modal akhir bulan: Rp101,000,000.00

Bulan ke-4:
  Persentase laba: 1.0%
  Laba bulan ini: Rp1,010,000.00
  Modal akhir bulan: Rp102,010,000.00

Bulan ke-5:
  Persentase laba: 6.0%
  Laba bulan ini: Rp6,120,600.00
  Modal akhir bulan: Rp108,130,600.00

Bulan ke-6:
  Persentase laba: 6.0%
  Laba bulan ini: Rp6,487,836.00
  Modal akhir bulan: Rp114,618,436.00

Bulan ke-7:
  Persentase laba: 6.0%
  Laba bulan ini: Rp6,877,106.16
  Modal akhir bulan: Rp121,495,542.16

Bulan ke-8:
Bulan ke-7:
  Persentase laba: 6.0%
  Laba bulan ini: Rp6,877,106.16
  Modal akhir bulan: Rp121,495,542.16

Bulan ke-8:
  Persentase laba: 4.0%
  Laba bulan ini: Rp4,859,821.69
  Modal akhir bulan: Rp126,355,363.85

==================================================
HASIL AKHIR:
Total keuntungan selama 8 bulan: Rp26,355,363.85
Modal akhir setelah 8 bulan: Rp126,355,363.85
Return on Investment (ROI): 26.36%
```


# 💰 Tugas 3

Program ini mensimulasikan sistem ATM sederhana yang memungkinkan pengguna untuk melakukan tiga fungsi utama: tarik tunai, cek saldo, dan keluar dari sistem.

# 🔧 Bagian 1: Import Library dan Inisialisasi
```python

import sys

def atm_simulation():
    balance = 1000000

    import sys: Mengimpor modul system untuk menggunakan fungsi sys.exit()

    balance = 1000000: Set saldo awal sebesar Rp 1,000,000
```
# 📋 Bagian 2: Tampilan Awal
python
```python
print("Selamat datang di atm sederhana")
print(f"Saldo anda saat ini : Rp {balance:,.0f}")
```
Menampilkan pesan selamat datang dan saldo awal dengan format Rupiah.

# 🔄 Bagian 3: Loop Menu Utama
```python

while True:
    print("\nmenu Transaksi")
    print("1. Tarik Tunai")
    print("2. Cek saldo")
    print("3. Keluar")
```
Loop infinite yang akan terus menampilkan menu sampai pengguna memilih keluar.

# 💵 Bagian 4: Fitur Tarik Tunai (Opsi 1)
python
```python
if choice == '1':
    try:
        amount_to_withdraw = int(input("masukan jumlah penarikan: Rp "))
        
        # Validasi 1: Jumlah harus positif
        if amount_to_withdraw <= 0:
            print("Jumlah Penarikan harus lebih dari 0")
        
        # Validasi 2: Cek kecukupan saldo
        elif amount_to_withdraw > balance:
            print(f"Saldo tidak mencukupi. Saldo Anda: Rp {balance:,.0f}")
        
        # Jika validasi berhasil
        else:
            balance -= amount_to_withdraw
            print(f"Penarikan sebesar Rp {amount_to_withdraw:,.0f}")
            print("Penarikan Berhasil !")
            print(f"Saldo Anda sekarang : Rp {balance:,.0f}")
            
            # Cek jika saldo habis
            if balance == 0:
                print("Saldo Anda telah habis. Silahkan isi kembali")
                break
                
    except ValueError:
        print("input tidak valid. Harap masukan Angka.")
```

# Fitur Keamanan dalam Tarik Tunai:

    try-except: Menangani error jika input bukan angka

    Validasi jumlah: Harus > 0

    Cek saldo: Tidak boleh melebihi saldo tersedia

    Auto exit: Keluar otomatis jika saldo habis

# 📊 Bagian 5: Fitur Cek Saldo (Opsi 2)

```python

elif choice == '2':
    print(f"Saldo Anda saat ini: Rp {balance:,.0f}")
```
Sangat sederhana - hanya menampilkan saldo terkini.

# 🚪 Bagian 6: Fitur Keluar (Opsi 3)

```python

elif choice == '3':
    print("Terima kasih telah menggukan ATM kami.")
    sys.exit()

sys.exit() menghentikan program secara keseluruhan.
⚡ Bagian 7: Error Handling
python

else:
    print("Pilihan tidak valid. mohon masukan Angka 1/2/3")
```
Menangani input yang tidak valid selain 1, 2, atau 3.

# 🎪 Bagian 8: Menjalankan Program

```

if __name__ == "__main__":
    atm_simulation()
```
Memastikan program hanya berjalan ketika dieksekusi langsung (bukan diimport).
