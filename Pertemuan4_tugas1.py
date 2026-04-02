hari = int(input("Masukkan jumlah hari: "))

tahun = hari // 365
sisa_hari = hari % 365

bulan = sisa_hari // 30
hari = sisa_hari % 30

print("Tahun :", tahun)
print("Bulan :", bulan)
print("Hari  :", sisa_hari)