import math

pilihan = 1
r = 7

print("pilihan:")
print("1. hitung keliling lingkaran")
print("2. hitung luas lingkaran")
print("pilihan yang dipakai:", pilihan)
print("jari-jari:", r)

if pilihan == 1:
    keliling = 2 *math.pi * r
    print("keliling lingkaran:", round (keliling, 2))
elif pilihan  == 2:
    luas = math.pi * r ** 2
    print("luas lingkaran:", round (luas, 2))
else:
    print("pilihan tidak valid")