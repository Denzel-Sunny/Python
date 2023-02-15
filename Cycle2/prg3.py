list = []
N = int(input("Size of list: "))
for i in range(0, N):
    print("enter elements: ")
    list.append(int(input()))
print(list)

Sum = sum(list)
print("Sum of elements =", Sum)
