def statistik(daftar):
    nilai_min = min(daftar)
    nilai_max = max(daftar)
    rata_rata = sum(daftar) / len(daftar)

    return nilai_min, nilai_max, rata_rata

data = [80, 90, 75, 85, 95]
hasil = statistik(data)

print("Nilai minimum:", hasil[0])
print("Nilai maksimum:", hasil[1])
print("Rata-rata:", hasil[2])