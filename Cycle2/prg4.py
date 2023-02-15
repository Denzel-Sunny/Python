n1 = int(input("Enter the first 4 digit number:"))
n2 = int(input("Enter the last 4 digit number:"))
list1 = []
for i in range(n1, n2):
    for j in range(32, 100):
        if i == j * j:
            string = str(i)
            if int(string[0]) % 2 == 0 and int(string[1]) % 2 == 0 and int(string[2]) % 2 == 0 and int(
                    string[3]) % 2 == 0:
                list1.append(i)
print(list1)