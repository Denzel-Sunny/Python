print("Area of a Square")
n = int(input("Enter the lenght of side of the square: "))
Area_square = lambda n: n*n
print("Area of the square:  \n",Area_square(n))

print("Area of a Rectangle")
l = int(input("Length of Rectangle: "))
b = int(input("Breadth of Rectangle: "))
Area_rectangle = lambda l, b : l*b
print("Area of the rectangle:  \n",Area_rectangle(l,b))

print("Area of a Triangle")
s = int(input("Base of Triangle: "))
h = int(input("Height of Triangle: "))
Area_triangle = lambda s, h : (s*h)/2
print("Area of the triangle:  \n",Area_triangle(s,h))