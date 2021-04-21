import math
import matplotlib.pyplot as plt
import numpy as np

# Input Angka
a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
c = int(input("masukkan c: "))

# Kalkulasi diskriminan
dis = b*b -4*a*c

# kalkulasi persamaan
if dis > 0:
    print((-b + math.sqrt(dis))/2*a)
    print((-b - math.sqrt(dis))/2*a)

if dis < 0:
    print("Akar-akar imaginer!")