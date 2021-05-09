import numpy as np

print("Kalkulator matriks 3x3")
print("  ==================")
print("      | a b c |")
print("      | d e f |")
print("      | g h i | \n")

print("Operasi yang tersedia: Determinan & Invers")
ops = str(input("Masukkan operasi: "))

baris = int(input("Masukkan jumlah baris: "))
kolom = int(input("Masukkan jumlah kolom: "))
while(True):
    print("Masukkan angka sesuai urutan diatas (gunakan spasi)")
    angka = list(map(int, input().split()))
    matrix = np.array(angka).reshape(baris, kolom)
    print(matrix, "\n")
    if ops == "Determinan" or "determinan":
        print(np.linalg.det(matrix))
        lagi = str(input("Lagi? (y/n) "))
        if lagi != "y":
            print("Terimakasih")
            break
    elif ops == "Invers" or "invers":
        print(np.linalg.inv(matrix))
        lagi = str(input("Lagi? (y/n) "))
        if lagi != "y":
            print("Terimakasih")
            break