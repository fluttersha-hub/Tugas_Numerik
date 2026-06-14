# AMISHA_F5512510003

print("\n========== SOAL 11.1 ==========")

a = [0, -0.4, -0.4]
b = [0.8, 0.8, 0.8]
c = [-0.4, -0.4, 0.0]
d = [41.0, 25.0, 105.0]
n = 3

for i in range(1, n):
    m = a[i] / b[i-1]
    b[i] -= m * c[i-1]
    d[i] -= m * d[i-1]

x = [0.0] * n
x[n-1] = d[n-1] / b[n-1]
for i in range(n-2, -1, -1):
    x[i] = (d[i] - c[i] * x[i+1]) / b[i]

print(f"x1 = {x[0]:.4f}")
print(f"x2 = {x[1]:.4f}")
print(f"x3 = {x[2]:.4f}")


print("\n========== SOAL 11.2 ==========")

def mat_mul(A, B):
    n = len(A)
    C = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
            - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))

def inv3(A):
    d = det3(A)
    C = [[0.0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            minor = [[A[r][c] for c in range(3) if c != j]
                                for r in range(3) if r != i]
            C[i][j] = ((-1)**(i+j)) * (minor[0][0]*minor[1][1] - minor[0][1]*minor[1][0])
    inv = [[C[j][i]/d for j in range(3)] for i in range(3)]
    return inv

A = [[0.8, -0.4, 0],
    [-0.4, 0.8, -0.4],
    [0, -0.4, 0.8]]

Ainv = inv3(A)
print("Invers [A]:")
for row in Ainv:
    print([round(v, 6) for v in row])

I = mat_mul(A, Ainv)
print("Verifikasi A * A^-1 = I:")
for row in I:
    print([round(v, 4) for v in row])


print("\n========== SOAL 11.3 ==========")

a = [0, -0.020875, -0.020875, -0.020875]
b = [2.01475, 2.01475, 2.01475, 2.01475]
c = [-0.020875, -0.020875, -0.020875, 0.0]
d = [4.175, 0.0, 0.0, 2.0875]
n = 4

for i in range(1, n):
    m = a[i] / b[i-1]
    b[i] -= m * c[i-1]
    d[i] -= m * d[i-1]

T = [0.0] * n
T[n-1] = d[n-1] / b[n-1]
for i in range(n-2, -1, -1):
    T[i] = (d[i] - c[i] * T[i+1]) / b[i]

for i, t in enumerate(T):
    print(f"T{i+1} = {t:.6f}")


print("\n========== SOAL 11.4 ==========")

A = [[6, 15, 55],
    [15, 55, 225],
    [55, 225, 979]]
n = 3

L = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        s = sum(L[i][k] * L[j][k] for k in range(j))
        if i == j:
            L[i][j] = (A[i][i] - s) ** 0.5
        else:
            L[i][j] = (A[i][j] - s) / L[j][j]

# Hitung L * L^T
LT = [[L[j][i] for j in range(n)] for i in range(n)]
result = mat_mul(L, LT)
print("Verifikasi [L][L]^T (harus = A):")
for row in result:
    print([round(v, 4) for v in row])

print("\n========== SOAL 11.5 ==========")

A = [[6, 15, 55],
    [15, 55, 225],
    [55, 225, 979]]
b = [152.6, 585.6, 2488.8]
n = 3

L = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        s = sum(L[i][k] * L[j][k] for k in range(j))
        if i == j:
            L[i][j] = (A[i][i] - s) ** 0.5
        else:
            L[i][j] = (A[i][j] - s) / L[j][j]

y = [0.0]*n
for i in range(n):
    y[i] = (b[i] - sum(L[i][j]*y[j] for j in range(i))) / L[i][i]

x = [0.0]*n
for i in range(n-1, -1, -1):
    x[i] = (y[i] - sum(L[j][i]*x[j] for j in range(i+1, n))) / L[i][i]

print(f"a0 = {x[0]:.6f}")
print(f"a1 = {x[1]:.6f}")
print(f"a2 = {x[2]:.6f}")


print("\n========== SOAL 11.6 ==========")

A = [[8, 20, 15],
    [20, 80, 50],
    [15, 50, 60]]
b = [50.0, 250.0, 100.0]
n = 3

L = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        s = sum(L[i][k] * L[j][k] for k in range(j))
        if i == j:
            L[i][j] = (A[i][i] - s) ** 0.5
        else:
            L[i][j] = (A[i][j] - s) / L[j][j]

print("Matriks L:")
for row in L:
    print([round(v, 6) for v in row])

y = [0.0]*n
for i in range(n):
    y[i] = (b[i] - sum(L[i][j]*y[j] for j in range(i))) / L[i][i]

x = [0.0]*n
for i in range(n-1, -1, -1):
    x[i] = (y[i] - sum(L[j][i]*x[j] for j in range(i+1, n))) / L[i][i]

print(f"x1 = {x[0]:.6f}")
print(f"x2 = {x[1]:.6f}")
print(f"x3 = {x[2]:.6f}")


print("\n========== SOAL 11.7 ==========")

A = [[9, 0, 0],
    [0, 25, 0],
    [0, 0, 4]]
n = 3

L = [[0.0]*n for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        s = sum(L[i][k] * L[j][k] for k in range(j))
        if i == j:
            L[i][j] = (A[i][i] - s) ** 0.5
        else:
            L[i][j] = (A[i][j] - s) / L[j][j]

print("Matriks L:")
for row in L:
    print([round(v, 4) for v in row])
print("Untuk matriks diagonal, L juga diagonal dengan elemen = sqrt(A[i][i])")


print("\n========== SOAL 11.8 ==========")

lam = 1.2
es = 5.0
x1, x2, x3 = 0.0, 0.0, 0.0

print(f"{'Iter':>4} | {'x1':>10} | {'x2':>10} | {'x3':>10}")
print("-" * 45)

for i in range(1, 100):
    x1_old, x2_old, x3_old = x1, x2, x3

    x1 = lam * ((41 + 0.4*x2) / 0.8) + (1-lam) * x1_old
    x2 = lam * ((25 + 0.4*x1 + 0.4*x3) / 0.8) + (1-lam) * x2_old
    x3 = lam * ((105 + 0.4*x2) / 0.8) + (1-lam) * x3_old

    e1 = abs((x1-x1_old)/x1)*100 if x1 != 0 else 100
    e2 = abs((x2-x2_old)/x2)*100 if x2 != 0 else 100
    e3 = abs((x3-x3_old)/x3)*100 if x3 != 0 else 100

    print(f"{i:>4} | {x1:>10.4f} | {x2:>10.4f} | {x3:>10.4f}")

    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi!")
        break

print(f"x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")


print("\n========== SOAL 11.9 ==========")

es = 5.0
c1, c2, c3 = 0.0, 0.0, 0.0

print(f"{'Iter':>4} | {'c1':>10} | {'c2':>10} | {'c3':>10}")
print("-" * 45)

for i in range(1, 100):
    c1_old, c2_old, c3_old = c1, c2, c3

    c1 = (3800 + 3*c2 + c3) / 15
    c2 = (1200 + 3*c1 + 6*c3) / 18
    c3 = (2350 + 4*c1 + c2) / 12

    e1 = abs((c1-c1_old)/c1)*100 if c1 != 0 else 100
    e2 = abs((c2-c2_old)/c2)*100 if c2 != 0 else 100
    e3 = abs((c3-c3_old)/c3)*100 if c3 != 0 else 100

    print(f"{i:>4} | {c1:>10.4f} | {c2:>10.4f} | {c3:>10.4f}")

    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi!")
        break

print(f"c1={c1:.4f}, c2={c2:.4f}, c3={c3:.4f}")


print("\n========== SOAL 11.10 ==========")

es = 5.0
c1, c2, c3 = 0.0, 0.0, 0.0

print(f"{'Iter':>4} | {'c1':>10} | {'c2':>10} | {'c3':>10}")
print("-" * 45)

for i in range(1, 200):
    c1_old, c2_old, c3_old = c1, c2, c3

    c1 = (3800 + 3*c2_old + c3_old) / 15
    c2 = (1200 + 3*c1_old + 6*c3_old) / 18
    c3 = (2350 + 4*c1_old + c2_old) / 12

    e1 = abs((c1-c1_old)/c1)*100 if c1 != 0 else 100
    e2 = abs((c2-c2_old)/c2)*100 if c2 != 0 else 100
    e3 = abs((c3-c3_old)/c3)*100 if c3 != 0 else 100

    print(f"{i:>4} | {c1:>10.4f} | {c2:>10.4f} | {c3:>10.4f}")

    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi!")
        break

print(f"c1={c1:.4f}, c2={c2:.4f}, c3={c3:.4f}")


print("\n========== SOAL 11.11 ==========")

es = 5.0
x1, x2, x3 = 0.0, 0.0, 0.0

print(f"{'Iter':>4} | {'x1':>10} | {'x2':>10} | {'x3':>10} | {'e1(%)':>8} | {'e2(%)':>8} | {'e3(%)':>8}")
print("-" * 75)

for i in range(1, 100):
    x1_old, x2_old, x3_old = x1, x2, x3

    x1 = (27 - 2*x2 + x3) / 10
    x2 = (-61.5 + 3*x1 - 2*x3) / -6
    x3 = (-21.5 - x1 - x2) / 5

    e1 = abs((x1-x1_old)/x1)*100 if x1 != 0 else 100
    e2 = abs((x2-x2_old)/x2)*100 if x2 != 0 else 100
    e3 = abs((x3-x3_old)/x3)*100 if x3 != 0 else 100

    print(f"{i:>4} | {x1:>10.6f} | {x2:>10.6f} | {x3:>10.6f} | {e1:>8.4f} | {e2:>8.4f} | {e3:>8.4f}")

    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi!")
        break

print(f"x1={x1:.6f}, x2={x2:.6f}, x3={x3:.6f}")


print("\n========== SOAL 11.12 ==========")

es = 5.0

print("(a) Tanpa relaksasi:")
x1, x2, x3 = 0.0, 0.0, 0.0
for i in range(1, 100):
    x1_old, x2_old, x3_old = x1, x2, x3
    x1 = (3 + x2 + x3) / 6
    x2 = (40 - 6*x1 - x3) / 9
    x3 = (50 + 3*x1 - x2) / 12
    e1 = abs((x1-x1_old)/x1)*100 if x1 != 0 else 100
    e2 = abs((x2-x2_old)/x2)*100 if x2 != 0 else 100
    e3 = abs((x3-x3_old)/x3)*100 if x3 != 0 else 100
    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
        break

print("(b) Dengan relaksasi lambda=0.95:")
lam = 0.95
x1, x2, x3 = 0.0, 0.0, 0.0
for i in range(1, 100):
    x1_old, x2_old, x3_old = x1, x2, x3
    x1 = lam*(3 + x2 + x3)/6 + (1-lam)*x1_old
    x2 = lam*(40 - 6*x1 - x3)/9 + (1-lam)*x2_old
    x3 = lam*(50 + 3*x1 - x2)/12 + (1-lam)*x3_old
    e1 = abs((x1-x1_old)/x1)*100 if x1 != 0 else 100
    e2 = abs((x2-x2_old)/x2)*100 if x2 != 0 else 100
    e3 = abs((x3-x3_old)/x3)*100 if x3 != 0 else 100
    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
        break


print("\n========== SOAL 11.13 ==========")

es = 5.0

print("(a) Tanpa relaksasi:")
x1, x2, x3 = 0.0, 0.0, 0.0
for i in range(1, 100):
    x1_old, x2_old, x3_old = x1, x2, x3
    x1 = (-20 - x2 + 2*x3) / -8
    x2 = (-38 - 2*x1 + x3) / -6
    x3 = (-34 + 3*x1 + x2) / 7
    e1 = abs((x1-x1_old)/x1)*100 if x1 != 0 else 100
    e2 = abs((x2-x2_old)/x2)*100 if x2 != 0 else 100
    e3 = abs((x3-x3_old)/x3)*100 if x3 != 0 else 100
    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
        break

print("(b) Dengan relaksasi lambda=1.2:")
lam = 1.2
x1, x2, x3 = 0.0, 0.0, 0.0
for i in range(1, 100):
    x1_old, x2_old, x3_old = x1, x2, x3
    x1 = lam*((-20 - x2 + 2*x3)/-8) + (1-lam)*x1_old
    x2 = lam*((-38 - 2*x1 + x3)/-6) + (1-lam)*x2_old
    x3 = lam*((-34 + 3*x1 + x2)/7) + (1-lam)*x3_old
    e1 = abs((x1-x1_old)/x1)*100 if x1 != 0 else 100
    e2 = abs((x2-x2_old)/x2)*100 if x2 != 0 else 100
    e3 = abs((x3-x3_old)/x3)*100 if x3 != 0 else 100
    if e1 < es and e2 < es and e3 < es:
        print(f"Konvergen setelah {i} iterasi: x1={x1:.4f}, x2={x2:.4f}, x3={x3:.4f}")
        break


print("\n========== SOAL 11.14 ==========")
print("Slope 1 dan -1 -> Gauss-Seidel tidak konvergen (berosilasi):")

x1, x2 = 0.0, 0.0
for i in range(1, 11):
    x1 = 3 - x2
    x2 = x1 - 1
    print(f"Iterasi {i}: x1={x1:.4f}, x2={x2:.4f}")
print("-> Nilai berosilasi, tidak konvergen.")


print("\n========== SOAL 11.15 ==========")

def cek_konvergen(nama, fn, x_init, max_iter=30, es=5.0):
    x = list(x_init)
    for i in range(1, max_iter+1):
        x_old = x[:]
        x = fn(x)
        errs = [abs((x[j]-x_old[j])/x[j])*100 if x[j] != 0 else 100 for j in range(len(x))]
        if all(e < es for e in errs):
            print(f"  {nama}: KONVERGEN di iterasi {i}, x={[round(v,4) for v in x]}")
            return
    print(f"  {nama}: TIDAK KONVERGEN setelah {max_iter} iterasi")

def set_one(x):
    return [(12 - 3*x[1] - x[2])/8,
            (5 - 2*x[0] + x[2])/4,
            (1 + 6*x[0])/7]

def set_two(x):
    return [7 - x[1] - 5*x[2],
            (4 - x[0] + x[2])/4,
            (4 - 3*x[0] - x[1])/-1]

def set_three(x):
    return [(7 - 3*x[1] - 5*x[2])/2,
            (-3 + 2*x[0] + 5*x[2])/4,
            (1 - 2*x[1])/-1]

cek_konvergen("Set One", set_one, [0,0,0])
cek_konvergen("Set Two", set_two, [0,0,0])
cek_konvergen("Set Three", set_three, [0,0,0])


print("\n========== SOAL 11.16 ==========")

def gauss_elim(A, b):
    n = len(b)
    M = [A[i][:] + [b[i]] for i in range(n)]
    for col in range(n):
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]
        for row in range(col+1, n):
            if M[col][col] == 0:
                continue
            f = M[row][col] / M[col][col]
            for k in range(col, n+1):
                M[row][k] -= f * M[col][k]
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        x[i] = (M[i][n] - sum(M[i][j]*x[j] for j in range(i+1, n))) / M[i][i]
    return x

print("(a) 3x3:")
A_a = [[14, 9, 4], [9, 16, 9], [4, 9, 25]]
b_a = [14, 29, 50]
x_a = gauss_elim(A_a, b_a)
print(f"x = {[round(v,6) for v in x_a]}")

print("(b) 4x4:")
A_b = [[1,4,9,16],[4,9,16,25],[9,16,25,36],[16,25,36,49]]
b_b = [30, 54, 86, 126]
try:
    x_b = gauss_elim(A_b, b_b)
    print(f"x = {[round(v,4) for v in x_b]}")
except ZeroDivisionError:
    print("Matriks singular, tidak bisa diselesaikan.")


print("\n========== SOAL 11.17 ==========")
print("Sistem nonlinear: f=4-y-2x^2=0, g=8-y^2-4x=0")
print("Dicari dengan Newton-Raphson 2D:")

def solve_nonlinear(x0, y0):
    x, y = float(x0), float(y0)
    for _ in range(100):
        f  =  4 - y - 2*x**2
        g  =  8 - y**2 - 4*x
        df_dx, df_dy = -4*x, -1.0
        dg_dx, dg_dy = -4.0, -2*y
        det = df_dx*dg_dy - df_dy*dg_dx
        if abs(det) < 1e-12:
            return None
        dx = (-f*dg_dy + g*df_dy) / det
        dy = (-df_dx*g + dg_dx*f) / det
        x += dx
        y += dy
        if abs(dx) < 1e-10 and abs(dy) < 1e-10:
            break
    if abs(4 - y - 2*x**2) < 1e-6 and abs(8 - y**2 - 4*x) < 1e-6:
        return (round(x,4), round(y,4))
    return None

solusi = []
for x0 in [-2, -1, 0, 1, 2]:
    for y0 in [-4, -1, 0, 2, 3]:
        s = solve_nonlinear(x0, y0)
        if s and s not in solusi:
            solusi.append(s)

for s in solusi:
    print(f"  x={s[0]}, y={s[1]}")


print("\n========== SOAL 11.18 ==========")

A = [[4,3,2],[1,3,1],[2,1,3]]
b = [960.0, 510.0, 610.0]
x = gauss_elim(A, b)
print(f"Transistors = {x[0]:.2f}")
print(f"Resistors   = {x[1]:.2f}")
print(f"Chips       = {x[2]:.2f}")


print("\n========== SOAL 11.19 ==========")
print("Hilbert matrix 10x10 diselesaikan dengan Gauss Elimination:")

n = 10
H = [[1/(i+j+1) for j in range(n)] for i in range(n)]
b = [sum(H[i]) for i in range(n)]

x = gauss_elim(H, b)
max_err = max(abs(x[i] - 1.0) for i in range(n))
print(f"Solusi (seharusnya semua = 1), max error = {max_err:.4e}")
print("(Hilbert matrix sangat ill-conditioned, error besar adalah normal)")


print("\n========== SOAL 11.20 ==========")
print("Vandermonde matrix 6x6, x=[4,2,7,10,3,5]:")

xv = [4, 2, 7, 10, 3, 5]
n = 6
V = [[xv[i]**(n-1-j) for j in range(n)] for i in range(n)]
b = [sum(V[i]) for i in range(n)]

x = gauss_elim(V, b)
max_err = max(abs(x[i] - 1.0) for i in range(n))
print(f"Solusi (seharusnya semua = 1), max error = {max_err:.4e}")


print("\n========== SOAL 11.21 ==========")

A = [[2, 1], [5, 3]]
n = len(A)
I = [[1 if i==j else 0 for j in range(n)] for i in range(n)]
Aug = [A[i] + I[i] for i in range(n)]

print("Aug = [A | I]:")
for row in Aug:
    print(row)
print("Cara numpy: Aug = np.hstack([A, np.eye(len(A))])")


print("\n========== SOAL 11.22 ==========")
# 50 = 5x3 - 7x2 ->  0x1 - 7x2 + 5x3 = 50
# 4x2 + 7x3 + 30 = 0 ->  0x1 + 4x2 + 7x3 = -30
# x1 - 7x3 = 40 - 3x2 + 5x1 -> -4x1 + 3x2 - 7x3 = 40

A = [[0, -7, 5], [0, 4, 7], [-4, 3, -7]]
b = [50.0, -30.0, 40.0]
x = gauss_elim(A, b)
print(f"x1 = {x[0]:.4f}")
print(f"x2 = {x[1]:.4f}")
print(f"x3 = {x[2]:.4f}")

print("Transpose [A]^T:")
AT = [[A[j][i] for j in range(3)] for i in range(3)]
for row in AT:
    print(row)


print("\n========== SOAL 11.23 ==========")
print(f"{'n':>4} | {'Gauss Elim':>12} | {'Thomas Alg':>12}")
print("-" * 35)
for n in range(2, 21):
    gauss = int((2/3)*n**3 + n**2 - (2/3)*n)
    thomas = 8*(n-1) + 1
    print(f"{n:>4} | {gauss:>12} | {thomas:>12}")


print("\n========== SOAL 11.24 ==========")

def thomas_algorithm(a, b, c, d):
    n = len(d)
    b = b[:]
    d = d[:]
    for i in range(1, n):
        m = a[i] / b[i-1]
        b[i] -= m * c[i-1]
        d[i] -= m * d[i-1]
    x = [0.0]*n
    x[n-1] = d[n-1] / b[n-1]
    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i]*x[i+1]) / b[i]
    return x

a = [0, -0.4, -0.4]
b = [0.8, 0.8, 0.8]
c = [-0.4, -0.4, 0.0]
d = [41.0, 25.0, 105.0]
hasil = thomas_algorithm(a, b, c, d)
print("Duplikasi Example 11.1:")
for i, v in enumerate(hasil):
    print(f"  x{i+1} = {v:.4f}")


print("\n========== SOAL 11.25 ==========")

def cholesky_solve(A, b):
    n = len(b)
    L = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k]*L[j][k] for k in range(j))
            if i == j:
                L[i][j] = (A[i][i] - s) ** 0.5
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]
    y = [0.0]*n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j]*y[j] for j in range(i))) / L[i][i]
    x = [0.0]*n
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - sum(L[j][i]*x[j] for j in range(i+1, n))) / L[i][i]
    return x

A = [[6,15,55],[15,55,225],[55,225,979]]
b = [152.6, 585.6, 2488.8]
x = cholesky_solve(A, b)
print("Duplikasi Example 11.2:")
print(f"  a0={x[0]:.4f}, a1={x[1]:.4f}, a2={x[2]:.4f}")


print("\n========== SOAL 11.26 ==========")

def gauss_seidel(A, b, es=5.0, max_iter=100, lam=1.0):
    n = len(b)
    x = [0.0]*n
    for it in range(1, max_iter+1):
        x_old = x[:]
        for i in range(n):
            sigma = sum(A[i][j]*x[j] for j in range(n) if j != i)
            x_new = (b[i] - sigma) / A[i][i]
            x[i] = lam*x_new + (1-lam)*x_old[i]
        errs = [abs((x[i]-x_old[i])/x[i])*100 if x[i] != 0 else 100 for i in range(n)]
        if all(e < es for e in errs):
            print(f"  Konvergen setelah {it} iterasi!")
            return x
    return x

A = [[15,-3,-1],[-3,18,-6],[-4,-1,12]]
b = [3800, 1200, 2350]
x = gauss_seidel(A, b)
print("Duplikasi Example 11.3:")
print(f"  c1={x[0]:.4f}, c2={x[1]:.4f}, c3={x[2]:.4f}")


print("\n========== SOAL 11.27 ==========")
print("Steady-state: 0 = D*d2c/dx2 - U*dc/dx - k*c")
print("D=2, U=1, k=0.2, c(0)=80, c(10)=20, dx=2")

D, U, k, dx = 2.0, 1.0, 0.2, 2.0
c0, c10 = 80.0, 20.0

a_c = D/dx**2 + U/(2*dx)
b_c = -2*D/dx**2 - k
c_c = D/dx**2 - U/(2*dx)

A = [[0.0]*4 for _ in range(4)]
b = [0.0]*4
for i in range(4):
    A[i][i] = b_c
    if i > 0:
        A[i][i-1] = a_c
    if i < 3:
        A[i][i+1] = c_c

b[0] -= a_c * c0
b[3] -= c_c * c10

c_int = gauss_elim(A, b)

x_vals = [0, 2, 4, 6, 8, 10]
c_vals = [c0] + c_int + [c10]

print(f"\n{'x':>5} | {'c':>10}")
print("-" * 20)
for xi, ci in zip(x_vals, c_vals):
    print(f"{xi:>5} | {ci:>10.4f}")


print("\n========== SOAL 11.28 ==========")

A = [
    [ 8, -2,  2,  0,  0],
    [-2,  9, -4, -1,  0],
    [-1, -3,  7, -1, -2],
    [ 0, -4, -2, 12, -5],
    [ 0,  0, -7, -3, 15]
]
b = [5.0, 2.0, 0.0, 1.0, 5.0]

x = gauss_elim(A, b)
print("Hasil:")
for i, v in enumerate(x):
    print(f"  x{i+1} = {v:.6f}")

print("Verifikasi Ax = b:")
for i in range(5):
    ax = sum(A[i][j]*x[j] for j in range(5))
    print(f"  baris {i+1}: {ax:.4f} (seharusnya {b[i]})")