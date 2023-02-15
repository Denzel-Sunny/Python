
list = []
n = int(input('enter the size of the list: '))
for i in range(0,n):
    a = str(input("enter the names: "))
    list.append(a)
print(list)
count = 0
for word in list:
    for char in word:
        if (char == 'a') or (char == 'A'):
            count = count+1

print("the number of a in the list is: ",count)