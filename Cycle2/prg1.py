from math import factorial
def fact(n):
    return(factorial(n))

num = int(input("Enter Number: "))
f = fact(num)
print("Factorial of", num,"is: ",f )