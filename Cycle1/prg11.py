a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))
if a>c and a>b:
    print(a," is the biggest")
elif b>c and b>a:
    print(b," is the biggest")
else:
    print(c," is the bigest")