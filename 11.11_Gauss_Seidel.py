# Soal 11.11 - Gauss-Seidel Method

print("=" * 60)
print("SOAL 11.11")
print("=" * 60)
print("Use the Gauss-Seidel method to solve the following system")
print("until the percent relative error falls below εs = 5%")
print()
print("  10x1 +  2x2 -  x3 =  27")
print("  -3x1 -  6x2 + 2x3 = -61.5")
print("    x1 +   x2 + 5x3 = -21.5")
print("=" * 60)
print()

# Toleransi error
es = 5  # 5%

# Nilai awal semua = 0
x1 = 0
x2 = 0
x3 = 0

print("Iterasi | x1         | x2         | x3         | Error x1(%) | Error x2(%) | Error x3(%)")
print("-" * 95)

for i in range(1, 100):
    x1_lama = x1
    x2_lama = x2
    x3_lama = x3

    # Isolasi tiap variabel dan update pakai nilai terbaru
    x1 = (27 - 2*x2 + x3) / 10
    x2 = (-61.5 + 3*x1 - 2*x3) / -6
    x3 = (-21.5 - x1 - x2) / 5

    # Hitung error relatif (%)
    e1 = abs((x1 - x1_lama) / x1) * 100 if x1 != 0 else 100
    e2 = abs((x2 - x2_lama) / x2) * 100 if x2 != 0 else 100
    e3 = abs((x3 - x3_lama) / x3) * 100 if x3 != 0 else 100

    print(f"   {i:2d}   | {x1:10.6f} | {x2:10.6f} | {x3:10.6f} | {e1:11.4f} | {e2:11.4f} | {e3:11.4f}")

    # Stop kalau semua error sudah di bawah 5%
    if e1 < es and e2 < es and e3 < es:
        print(f"\nKonvergen setelah {i} iterasi!")
        break

print(f"\nHasil akhir:")
print(f"x1 = {x1:.6f}")
print(f"x2 = {x2:.6f}")
print(f"x3 = {x3:.6f}")

print(f"\nVerifikasi (substitusi balik):")
print(f"10x1 + 2x2 -  x3 = {10*x1 + 2*x2 - x3:.4f}  (seharusnya  27)")
print(f"-3x1 - 6x2 + 2x3 = {-3*x1 - 6*x2 + 2*x3:.4f}  (seharusnya -61.5)")
print(f"  x1 +  x2 + 5x3 = {x1 + x2 + 5*x3:.4f}  (seharusnya -21.5)")