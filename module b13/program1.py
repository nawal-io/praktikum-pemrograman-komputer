import kuadrat

def main():
    # Input koefisien dari keyboard
    try:
        a = int(input('Masukkan a: '))
        b = int(input('Masukkan b: '))
        c = int(input('Masukkan c: '))
    except ValueError:
        print('Input harus berupa angka bulat!')
        return

    # Validasi: a = 0 bukan persamaan kuadrat
    if a == 0:
        print('Nilai a tidak boleh 0 pada persamaan kuadrat!')
        return

    # Hitung diskriminan memakai fungsi dari modul
    d = kuadrat.hitung_diskriminan(a, b, c)
    print('Diskriminan (D) =', d)

    # Cari akar memakai fungsi dari modul
    hasil = kuadrat.cari_akar(a, b, c)
    if hasil is None:
        print('Persamaan tidak memiliki akar real (D < 0)')
    else:
        x1, x2 = hasil
        print('Solusinya adalah {0} dan {1}'.format(x1, x2))

if __name__ == "__main__":
    main()