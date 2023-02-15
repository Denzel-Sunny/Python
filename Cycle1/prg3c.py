string = input("Enter string:")
vowels=0
newlist=[]
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
           newlist.append(i)
print("the vowels are:",newlist)