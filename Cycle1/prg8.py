a=str(input("enter the string: "))
for i in range(1,len(a)):
    if(a[i]==a[0]):
        b=a[0]+a[1:].replace(a[i],'$')
print(b)


