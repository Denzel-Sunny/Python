import graphics
from graphics import circle,rectangle
from graphics.tdgraphics import cuboid,sphere

radius =  int(input("radius of circle: "))
print("Area of circle is : ",circle.area_circle(radius))
print("Area of circle is : ",circle.perimeter_circle(radius))

length = int(input("length of rectangle: "))
width = int(input("width of rectangle: "))
print("Area of a Rectangle with length and width is : ",rectangle.area_rec(length, width))
print("Permeter of a Rectangle with length and width is : ",rectangle.perimeter_rec(length, width))


l = int(input("length of cuboid: "))
b = int(input("breadth of cuboid: "))
h = int(input("height of cuboid: "))
print("Area of a  cuboid with length,width,height is : ",cuboid.area_cuboid(l, b, h))
print("Permeter of a cuboid with length,width,height is : ",cuboid.perimeter_cuboid(l, b, h))

radius = int(input("radius of sphere: "))
print("Area of a sphere with radius is : ",sphere.area_sphere(radius))
print("Permeter of a sphere with radius  is ",sphere.perimeter_sphere(radius))