import math

x = float(input("Napisz liczba 1: "))
y = float(input("Napisz liczba 2: "))
print("Co musiłem zrobic z tym? (dodawanie(1)/odejmowanie(2)/mnożenie(3)/dzielenie(4)/potęgowanie(5)")
z = int(input())
if z == 1:
    c = x+y
elif z == 2:
    c = x-y
elif z == 3:
    c = x*y
elif z == 4 and y == 0:
    print("Jest niepoprawne")
    exit()
elif z == 4:
    c = x/y
elif z == 5:
    c = x**y
else:
    print("Nie jest poprawne")
    exit()
print(c)