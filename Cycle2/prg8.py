a = []
n = int(input("Size of the list: "))
for x in range(0, n):
    element = input("Enter word " + str(x + 1) + ": ")
    a.append(element)
print(a)
max1 = len(a[0])
temp = a[0]
for i in a:
    if len(i) > max1:
        max1 = len(i)
        temp = i
print("The word with the longest length is: ",temp)
