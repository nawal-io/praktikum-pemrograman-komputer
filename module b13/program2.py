import luas2d

def menu():
    print("\nPilih Bentuk 2D")
    print()
    print("1. Persegi Panjang")
    print("2. Lingkaran")
    print("3. Segitiga")
    print("4. Keluar")

def baca_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            if nilai <= 0:
                print("Nilai harus lebih besar dari 0!")
                continue
            return nilai
        except ValueError:
            print("Input harus berupa angka!")

def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = baca_angka("Masukkan Panjang : ")
    l = baca_angka("Masukkan Lebar : ")
    luas = luas2d.luas_persegi_panjang(p, l)
    print("Luas Persegi Panjang adalah {:.2f}".format(luas))

def lingkaran():
    print("Menghitung Luas Lingkaran")
    r = baca_angka("Masukkan Jari-Jari : ")
    luas = luas2d.luas_lingkaran(r)
    print("Luas Lingkaran adalah {:.2f}".format(luas))

def segitiga():
    print("Menghitung Luas Segitiga")
    a = baca_angka("Masukkan Alas : ")
    t = baca_angka("Masukkan Tinggi : ")
    luas = luas2d.luas_segitiga(a, t)
    print("Luas Segitiga adalah {:.2f}".format(luas))

def coba_lagi():
    print()
    jawab = input("Coba lagi [Y/N]? ").upper()
    return jawab == "Y"

def main():
    while True:
        menu()
        pilihan = input("Pilihan> ")

        if pilihan == "1":
            persegi()
        elif pilihan == "2":
            lingkaran()
        elif pilihan == "3":
            segitiga()
        elif pilihan == "4":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Pilihan tidak valid!")
            continue

        if not coba_lagi():
            print("Terima kasih, program selesai.")
            break

if __name__ == "__main__":
    main()