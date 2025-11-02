# Modal awal
modal_awal = 100000000  # 100 juta rupiah
modal_sekarang = modal_awal

# Persentase laba per bulan (dalam desimal)
# Bulan 1: 0% (belum laba)
# Bulan 2: 0% (belum laba)
# Bulan 3: 1% (0.01)
# Bulan 4: Laba bulan ke-3 berlanjut (1% atau 0.01)
# Bulan 5: Meningkat 5% (dari bulan sebelumnya, jadi 1% + 5% = 6% atau 0.06)
# Bulan 6: Laba bulan ke-5 berlanjut (6% atau 0.06)
# Bulan 7: Laba bulan ke-5 berlanjut (6% atau 0.06)
# Bulan 8: Penurunan 2% (dari bulan sebelumnya, jadi 6% - 2% = 4% atau 0.04)

persentase_laba_per_bulan = [0, 0, 0.01, 0.01, 0.06, 0.06, 0.06, 0.04]

print("=== SIMULASI INVESTASI 8 BULAN ===\n")
print(f"Modal awal: Rp{modal_awal:,.2f}\n")

# Simulasi selama 8 bulan
total_keuntungan = 0
for bulan in range(8):
    laba_bulan_ini = modal_sekarang * persentase_laba_per_bulan[bulan]
    total_keuntungan += laba_bulan_ini
    modal_sekarang += laba_bulan_ini  # Laba ditambahkan ke modal
    
    print(f"Bulan ke-{bulan + 1}:")
    print(f"  Persentase laba: {persentase_laba_per_bulan[bulan]*100:.1f}%")
    print(f"  Laba bulan ini: Rp{laba_bulan_ini:,.2f}")
    print(f"  Modal akhir bulan: Rp{modal_sekarang:,.2f}")
    print()

# Menampilkan hasil akhir
print("=" * 50)
print("HASIL AKHIR:")
print(f"Total keuntungan selama 8 bulan: Rp{total_keuntungan:,.2f}")
print(f"Modal akhir setelah 8 bulan: Rp{modal_sekarang:,.2f}")
print(f"Return on Investment (ROI): {(total_keuntungan/modal_awal)*100:.2f}%")
