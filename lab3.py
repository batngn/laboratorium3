a=int(input("Napisz 1 liczbę "))
b=int(input("Napisz 2 liczbę "))
if (a>b):
    print(b)
    while(a>b):
        b=b+1
        print(b)
elif (a<b):
    print(a)
    while(b>a):
        a=a+1
        print(a)

elif a == b:
    print(a)
else: exit()




