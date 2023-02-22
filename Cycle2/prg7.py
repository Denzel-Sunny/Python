string = input("Enter string: ")

if string[-3:] == 'ing':
    print(string + 'ly')
else:
    print(string + 'ing')
