# inputan total jumlah belanja

total = int(input("total belanjaan: "))
if total == 100:
    bayar = total - (total*0.1) + 2
elif total == 200:
    bayar = total - (total*0.15) + 2
elif total > 250:
    bayar = total - (total*0.2) + 2
elif total ==0:
    bayar= 2
else:
    bayar=total +2

print("kamu membayar sejumlah:", bayar)

