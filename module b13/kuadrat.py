import math

def hitung_diskriminan(a, b, c):
    """Menghitung diskriminan D = b^2 - 4ac"""
    return (b**2) - (4 * a * c)

def cari_akar(a, b, c):
    """Mengembalikan (x1, x2) jika D >= 0, atau None jika tidak ada akar real"""
    d = hitung_diskriminan(a, b, c)
    if d < 0:
        return None
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    return x1, x2