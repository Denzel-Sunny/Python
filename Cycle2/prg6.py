str = str(input("Enter string: "))

freq = {}
for i in str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("frequeny of all chararcters in string: ")
print(freq)
