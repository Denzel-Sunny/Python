def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))



"""
str = input("Enter the string: ")

str_list = list(str.split(" "))
print(str_list)
str_set = list(set(str_list))

for word in str_set:
    print(word, " = ", str_list.count(word))
    
   
"""

"""string = input("Enter a long string : ")
search = input("Enter searchble string : ")
string=string.split(" ")
count=0
for i in string:
    if(i == search):
        count=count+1
print(count)"""
