import numpy as np

# Aturan Cosinus

a = int(input("Masukkan a: "))
b = int(input("Masukkan b: "))
alpha = int(input("Masukkan sudut c: "))

x = np.deg2rad(alpha)
c = np.sqrt((b*b)+(a*a)-(2*b*a* np.cos(x)))

print (c, "cm")

