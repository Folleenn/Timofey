# For10

N = int(input("Введите N: "))
S = 0
for i in range(1, N + 1):
    S += 1 / i
print(S)

# For11

N = int(input("Введите N: "))
S = 0
for i in range(N, 2 * N + 1):
    S += i ** 2
print(S)

# For12

N = int(input("Введите N: "))
P = 1
for i in range(1, N + 1):
    P *= 1 + i / 10
print(P)

# For13

N = int(input("Введите N: "))
S = 0
for i in range(1, N + 1):
    S += (-1) ** (i + 1) * (1 + i / 10)
print(S)

# For14

N = int(input("Введите N: "))
S = 0
for i in range(1, N + 1):
    S += 2 * i - 1
    print(S)

# For15

A = float(input("Введите A: "))
N = int(input("Введите N: "))
P = 1
for i in range(N):
    P *= A
print(P)

# For16

A = float(input("Введите A: "))
N = int(input("Введите N: "))
P = 1
for i in range(1, N + 1):
    P *= A
    print(P)

# For17

A = float(input("Введите A: "))
N = int(input("Введите N: "))
S = 1
P = 1
for i in range(1, N + 1):
    P *= A
    S += P
print(S)

# For18

A = float(input("Введите A: "))
N = int(input("Введите N: "))
S = 1
P = 1
for i in range(1, N + 1):
    P *= -A
    S += P
print(S)

# For19

N = int(input("Введите N: "))
P = 1.0
for i in range(1, N + 1):
    P *= i
print(P)

# For20

N = int(input("Введите N: "))
F = 1.0
S = 0.0
for i in range(1, N + 1):
    F *= i
    S += F
print(S)

# For21

N = int(input("Введите N: "))
F = 1.0
S = 1.0
for i in range(1, N + 1):
    F *= i
    S += 1 / F
print(S)

# For22

X = float(input("Введите X: "))
N = int(input("Введите N: "))
F = 1.0
P = 1.0
S = 1.0
for i in range(1, N + 1):
    P *= X
    F *= i
    S += P / F
print(S)

# For23

X = float(input("Введите X: "))
N = int(input("Введите N: "))
F = 1.0
P = X
S = X
for i in range(1, N + 1):
    F *= (2 * i) * (2 * i + 1)
    P *= X * X
    S += (-1) ** i * P / F
print(S)

# For24

X = float(input("Введите X: "))
N = int(input("Введите N: "))
F = 1.0
P = 1.0
S = 1.0
for i in range(1, N + 1):
    F *= (2 * i - 1) * (2 * i)
    P *= X * X
    S += (-1) ** i * P / F
print(S)

# For25

X = float(input("Введите X: "))
N = int(input("Введите N: "))
S = 0
for i in range(1, N + 1):
    S += (-1) ** (i + 1) * X ** i / i
print(S)

# For26

X = float(input("Введите X: "))
N = int(input("Введите N: "))
S = 0
for i in range(0, N + 1):
    S += (-1) ** i * X ** (2 * i + 1) / (2 * i + 1)
print(S)

# For27

X = float(input("Введите X: "))
N = int(input("Введите N: "))
S = X
P = X
for i in range(1, N + 1):
    P *= X * X
    for j in range(1, i + 1):
        P *= (2 * j - 1) / (2 * j)
    S += P / (2 * i + 1)
print(S)

# For28

X = float(input("Введите X: "))
N = int(input("Введите N: "))
S = 1.0
P = 1.0
for i in range(1, N + 1):
    P *= (2 * i - 3) * X / (2 * i)
    S += (-1) ** (i + 1) * P
print(S)

# For29

A = float(input("Введите A: "))
B = float(input("Введите B: "))
N = int(input("Введите N: "))
H = (B - A) / N
print(H)
for i in range(N + 1):
    X = A + i * H
    print(X)
    
# For30

A = float(input("Введите A: "))
B = float(input("Введите B: "))
N = int(input("Введите N: "))
H = (B - A) / N
print(H)
import math
for i in range(N + 1):
    X = A + i * H
    F = 1 - math.sin(X)
    print(F)

# For31

N = int(input("Введите N: "))
A = 2.0
for i in range(1, N + 1):
    A = 2 + 1 / A
    print(A)

# For32

N = int(input("Введите N: "))
A = 1.0
for i in range(1, N + 1):
    A = (A + 1) / i
    print(A)

# For33

N = int(input("Введите N: "))
A = 1
B = 1
print(A)
print(B)
for i in range(3, N + 1):
    C = A + B
    print(C)
    A = B
    B = C

# For34

N = int(input("Введите N: "))
A = 1.0
B = 2.0
print(A)
print(B)
for i in range(3, N + 1):
    C = (A + 2 * B) / 3
    print(C)
    A = B
    B = C

# For35

N = int(input("Введите N: "))
A = 1
B = 2
C = 3
print(A)
print(B)
print(C)
for i in range(4, N + 1):
    D = C + B - 2 * A
    print(D)
    A = B
    B = C
    C = D

# For36

N = int(input("Введите N: "))
K = int(input("Введите K: "))
S = 0.0
for i in range(1, N + 1):
    S += i ** K
print(S)

# For37

N = int(input("Введите N: "))
S = 0.0
for i in range(1, N + 1):
    S += i ** i
print(S)

# For38

N = int(input("Введите N: "))
S = 0.0
for i in range(1, N + 1):
    S += i ** (N - i + 1)
print(S)

# For39

A = int(input("Введите A: "))
B = int(input("Введите B: "))
for i in range(A, B + 1):
    for j in range(i):
        print(i, end=" ")
print()

# For40

A = int(input("Введите A: "))
B = int(input("Введите B: "))
K = 1
for i in range(A, B + 1):
    for j in range(K):
        print(i, end=" ")
    K += 1
print()

# While10

N = int(input("Введите N: "))
K = 0
while 3 ** (K + 1) < N:
    K += 1
print(K)

# While11

N = int(input("Введите N: "))
K = 0
S = 0
while S < N:
    K += 1
    S += K
print(K)
print(S)

# While12

N = int(input("Введите N: "))
K = 0
S = 0
while S + K + 1 <= N:
    K += 1
    S += K
print(K)
print(S)

# While13

A = float(input("Введите A: "))
K = 0
S = 0
while S <= A:
    K += 1
    S += 1 / K
print(K)
print(S)

# While14

A = float(input("Введите A: "))
K = 0
S = 0
while S + 1 / (K + 1) < A:
    K += 1
    S += 1 / K
print(K)
print(S)

# While15

P = float(input("Введите P: "))
S = 1000
K = 0
while S <= 1100:
    S += S * P / 100
    K += 1
print(K)
print(S)

# While16

P = float(input("Введите P: "))
S = 10
Day = 10
K = 1
while S <= 200:
    Day += Day * P / 100
    S += Day
    K += 1
print(K)
print(S)

# While17

N = int(input("Введите N: "))
while N > 0:
    print(N % 10)
    N //= 10

# While18

N = int(input("Введите N: "))
Count = 0
S = 0
while N > 0:
    S += N % 10
    Count += 1
    N //= 10
print(Count)
print(S)

# While19

N = int(input("Введите N: "))
Reverse = 0
while N > 0:
    Reverse = Reverse * 10 + N % 10
    N //= 10
print(Reverse)

# While20

N = int(input("Введите N: "))
Found = False
while N > 0:
    if N % 10 == 2:
        Found = True
    N //= 10
print(Found)

# While21

N = int(input("Введите N: "))
Found = False
while N > 0:
    if N % 10 % 2 != 0:
        Found = True
    N //= 10
print(Found)

# While22

N = int(input("Введите N: "))
K = 2
Simple = True
while K * K <= N:
    if N % K == 0:
        Simple = False
    K += 1
print(Simple)

# While23

A = int(input("Введите A: "))
B = int(input("Введите B: "))
while B != 0:
    A, B = B, A % B
print(A)

# While24

N = int(input("Введите N: "))
A = 1
B = 1
Found = False
while A <= N:
    if A == N:
        Found = True
    C = A + B
    A = B
    B = C
print(Found)

# While25

N = int(input("Введите N: "))
A = 1
B = 1
while A <= N:
    C = A + B
    A = B
    B = C
print(A)

# While26

N = int(input("Введите N: "))
A = 1
B = 1
while B != N:
    C = A + B
    A = B
    B = C
print(A)
print(A + B)

# While27

N = int(input("Введите N: "))
A = 1
B = 1
K = 2
while B != N:
    C = A + B
    A = B
    B = C
    K += 1
print(K)

# While28

E = float(input("Введите E: "))
A1 = 2.0
K = 1
while True:
    A2 = 2 + 1 / A1
    K += 1
    if abs(A2 - A1) < E:
        break
    A1 = A2
print(K)
print(A1)
print(A2)

# While29

E = float(input("Введите E: "))
A1 = 1.0
A2 = 2.0
K = 2
while True:
    A3 = (A1 + 2 * A2) / 3
    K += 1
    if abs(A3 - A2) < E:
        break
    A1 = A2
    A2 = A3
print(K)
print(A2)
print(A3)

# While30

A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
CountA = 0
CountB = 0
while A >= C:
    A -= C
    CountA += 1
while B >= C:
    B -= C
    CountB += 1
Count = 0
while CountA > 0:
    Count += CountB
    CountA -= 1
print(Count)
