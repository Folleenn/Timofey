'''#Begin1
a = float(input('Сторона квадрата: '))
P = 4 * a
print('Периметр = ', P)'''

'''#Begin2
a = float(input('Сторона квадрата: '))
S = a ** 2
print('Площадь = ', S)'''

'''#Begin3
a = float(input())
b = float(input())
S = a * b
P = 2 * (a+b)
print(f'Площадь = ', {S}, 'Периметр = ', {P})'''

'''#Begin4
d = float(input())
pi = 3.14
L = pi * d
print('Длина = ', L)'''

'''#Begin5
a = float(input())
V = a ** 3
S = 6 * (a ** 2)
print(f'Объём = ', V, 'площадь = ',)'''

'''#Begin6
a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print(f"Обьем: {V}, Площадь: {S}")'''

'''#Beging7
R = int(input("Введите радиус: "))
L = 2 * 3.14 * R
S = 3.14 * R**2
print(f"Длина: {L}, Площадь: {S}")'''

'''#beginig8
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
ab = (a + b)/2'''

'''#beginig9
a = float(input("Введите неотрицательное число a: "))
b = float(input("Введите неотрицательное число b: "))
a >= 0 and b >= 0
ab = (a * b) ** 0.5'''

'''#Begin10
a = float(input())
b = float(input())
a != 0 and b != 0
c = a ** 2 + b ** 2
d = a ** 2 - b ** 2
e = (a ** 2) * (b ** 2)
f = (a ** 2) / (b ** 2)
print(f'Сумма квадратов = ', c, 'разность квадратов = ', d, 'произведение квадратов = ', e, 'частное квадратов = ', f,)'''

'''#Begin11
a = float(input())
b = float(input())
a != 0 and b != 0
c = a ** 2 + b ** 2
d = a ** 2 - b ** 2
e = (a ** 2) * (b ** 2)
f = ((a ** 2) ** 0.5) / ((b ** 2) ** 0.5)
print(f'Сумма квадратов = ', c, 'разность квадратов = ', d, 'произведение квадратов = ', e, 'частное модулей = ', f,)'''

'''#Begin12
a = float(input('Первый катет: '))
b = float(input('Второй катет: '))
c = (a ** 2 + b ** 2) ** 0.5
P = a + b + c
print('Гипотенуза = ', c)
print('Периметр = ', P)'''

'''#Begin13
R1 = float(input('Введите R1: ')) 
R2 = float(input('Введите R2: '))

S1 = 3.14 * R1 * R1
S2 = 3.14 * R2 * R2
S3 = S1 - S2

print("Площадь первого круга:", S1)
print("Площадь второго круга:", S2)
print("Площадь кольца:", S3)'''

'''#Begin14
L = float(input("Введите длину окружности: "))

R = L / (2 * 3.14)
S = 3.14 * R * R

print("Радиус:", R)
print("Площадь:", S)'''

'''#Begin15
S = float(input("Введите площадь круга: "))

R = (S / 3.14) ** 0.5
D = 2 * R
L = 2 * 3.14 * R

print("Диаметр:", D)
print("Длина окружности:", L)'''

'''#Begin15
x1 = float(input('Введите x1: ')) 
x2 = float(input('Введите x2: '))
print("Расстояние:", abs(x2 - x1))'''

'''#Begin16
A = float(input('Введите A: ')) 
B = float(input('Введите B: '))
C = float(input('Введите C: '))

AC = abs(C - A)
BC = abs(C - B)

print("AC:", AC)
print("BC:", BC)
print("AC + BC:", AC + BC)'''

'''#Begin17
A = float(input('Введите A: ')) 
B = float(input('Введите B: '))
C = float(input('Введите C: '))

AC = abs(C - A)
BC = abs(B - C)

print("Произведение AC * BC:", AC * BC)'''

'''#Begin17
x1 = float(input('Введите x1: ')) 
y1 = float(input('Введите y2: '))
x2 = float(input('Введите x1: ')) 
y2 = float(input('Введите x2: '))

distance = ((x2 - x1)  2 + (y2 - y1)  2) ** 0.5

print("Расстояние:", distance)'''

'''#Begin18
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

AC = abs(C - A)
BC = abs(B - C)

print("Произведение AC * BC:", AC * BC)'''

'''#Begin19
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

a = abs(x2 - x1)
b = abs(y2 - y1)

print("Периметр:", 2 * (a + b))
print("Площадь:", a * b)'''

'''#Begin20
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))

distance = ((x2 - x1)  2 + (y2 - y1)  2) ** 0.5

print("Расстояние:", distance)'''

'''#Begin21
x1 = float(input("Введите x1: "))
y1 = float(input("Введите y1: "))
x2 = float(input("Введите x2: "))
y2 = float(input("Введите y2: "))
x3 = float(input("Введите x3: "))
y3 = float(input("Введите y3: "))

a = ((x2 - x1)  2 + (y2 - y1)  2) ** 0.5
b = ((x3 - x2)  2 + (y3 - y2)  2) ** 0.5
c = ((x1 - x3)  2 + (y1 - y3)  2) ** 0.5

p = (a + b + c) / 2

print("Периметр:", a + b + c)
print("Площадь:", (p * (p - a) * (p - b) * (p - c)) ** 0.5)'''

'''#Begin22
A = float(input("Введите A: "))
B = float(input("Введите B: "))

T = A
A = B
B = T

print("A =", A)
print("B =", B)'''

'''#Begin23
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

T = A
A = C
C = B
B = T

print("A =", A)
print("B =", B)
print("C =", C)'''

'''#Begin24
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

T = A
A = B
B = C
C = T

print("A =", A)
print("B =", B)
print("C =", C)'''

'''#Begin25
x = float(input("Введите x: "))

y = 3 * x  6 - 6 * x  2 - 7

print("y =", y)'''

'''#Begin26
x = float(input("Введите x: "))

y = 4 * (x - 3)  6 - 7 * (x - 3)  3 + 2

print("y =", y)'''

'''#Begin27
A = float(input("Введите A: "))

A2 = A * A
A4 = A2 * A2
A8 = A4 * A4

print("A² =", A2)
print("A⁴ =", A4)
print("A⁸ =", A8)'''

'''#Begin28
A = float(input("Введите A: "))

A2 = A * A
A3 = A2 * A
A5 = A3 * A2
A10 = A5 * A5
A15 = A10 * A5

print("A² =", A2)
print("A³ =", A3)
print("A⁵ =", A5)
print("A¹⁰ =", A10)
print("A¹⁵ =", A15)'''

'''#Begin29
a = float(input("Введите угол в градусах: "))

radians = a * 3.14 / 180

print("Угол в радианах:", radians)'''

'''#Begin30
a = float(input("Введите угол в радианах: "))

degrees = a * 180 / 3.14

print("Угол в градусах:", degrees)'''

'''#Begin31
TF = float(input("Введите температуру в Фаренгейтах: "))

TC = (TF - 32) * 5 / 9

print("Температура в Цельсиях:", TC)'''

'''#Begin32
TC = float(input("Введите температуру в Цельсиях: "))

TF = TC * 9 / 5 + 32

print("Температура в Фаренгейтах:", TF)'''

'''#Begin33
X = float(input("Введите X: "))
A = float(input("Введите A: "))
Y = float(input("Введите Y: "))

price = A / X

print("Цена 1 кг:", price)
print("Цена Y кг:", price * Y)'''

'''#Begin34
X = float(input("Введите X: "))
A = float(input("Введите A: "))
Y = float(input("Введите Y: "))
B = float(input("Введите B: "))

price1 = A / X
price2 = B / Y

print("Цена 1 кг шоколадных конфет:", price1)
print("Цена 1 кг ирисок:", price2)
print("Во сколько раз шоколадные конфеты дороже:", price1 / price2)'''

'''#Begin35
V = float(input("Введите V: "))
U = float(input("Введите U: "))
T1 = float(input("Введите T1: "))
T2 = float(input("Введите T2: "))

S = V * T1 + (V - U) * T2

print("Пройденное расстояние:", S)'''

'''#Begin36
V1 = float(input("Введите V1: "))
V2 = float(input("Введите V2: "))
S = float(input("Введите S: "))
T = float(input("Введите T: "))

S = S + (V1 + V2) * T

print("Расстояние между автомобилями:", S)'''

'''#Begin37
V1 = float(input("Введите V1: "))
V2 = float(input("Введите V2: "))
S = float(input("Введите S: "))
T = float(input("Введите T: "))

S = abs(S - (V1 + V2) * T)

print("Расстояние между автомобилями:", S)'''

'''#Begin38
A = float(input("Введите A: "))
B = float(input("Введите B: "))

x = -B / A

print("x =", x)'''

'''#Begin39
A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))

D = B * B - 4 * A * C

x1 = (-B - D ** 0.5) / (2 * A)
x2 = (-B + D ** 0.5) / (2 * A)

print("Первый корень:", x1)
print("Второй корень:", x2)'''

'''#Begin40
A1 = float(input("Введите A1: "))
B1 = float(input("Введите B1: "))
C1 = float(input("Введите C1: "))
A2 = float(input("Введите A2: "))
B2 = float(input("Введите B2: "))
C2 = float(input("Введите C2: "))

D = A1 * B2 - A2 * B1

x = (C1 * B2 - C2 * B1) / D
y = (A1 * C2 - A2 * C1) / D

print("x =", x)
print("y =", y)'''
