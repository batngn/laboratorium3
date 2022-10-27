x=int(input("Ile masz lat: "))
if x < 4:
    y = 0
elif x <= 18:
    y = 10
else:
    y = 20

print("Bilet kosztuje ",y," zł")
