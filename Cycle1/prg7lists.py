A = []
B = []
n = int(input("enter the size of the list: "))
print("enter the integers: ")
for i in range(0,n):
    A.append(int(input()))
print(A)
m = int(input("enter the size of the list: "))
print("enter the integers: ")
for i in range(0,m):
    B.append(int(input()))
print(B)
if len(A) == len(B):
    print("the lists are of the same length")
else:
    print("lists are not of the same length")

if sum(A) == sum(B):
    print("sum of the list is the same")
else:
    print("sum is not equal")

def common_member(A, B):
    result = [i for i in A if i in B]
    return result
print("The common elements in the two lists are: ")
print(common_member(A, B))
