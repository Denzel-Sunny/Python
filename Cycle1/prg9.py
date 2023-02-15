a = str(input("enter the string: "))
start = a[0]
end = a[-1]
b = end + a[1:-1] + start
print(b)