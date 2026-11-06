nomor = input("masukkan nomor pendaftaran : ")
adm = input("masukkan hasil tes administrasi jika (lolos/tidak): ")
if adm=="lolos":
    rikkes = input("masukkan hasil tes rikkes (lolos/tidak): ")
    if rikkes=="lolos":
        jas = input ("masukkan nilai tes jas (lolos/tidak): ")
        if jas=="lolos":
            psi = input("masukkan hasil tes psi (lolos/tidak): ")
            if psi=="lolos":
                print("LOLOS TNI")
            else:
                print("TIDAK LOLOS PSIKOLOGI INI")
        else:
            print("TIDAK LOLOS JASMANI INI")
    else:
        print("TIDAK LOLOS RIKKES INI")
else:
    print("TIDAK LOLOS ADMINISTRASI INI")