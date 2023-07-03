
# Create a package named shape that contains two modules: rectangle and circle.
# In the rectangle module, define a function area(width, height) that calculates and returns the area of a rectangle given its width and height.
# In the circle module, define a function area(radius) that calculates and returns the area of a circle given its radius.
# Write a separate Python program that imports both modules from the shape package and uses their respective functions to calculate the areas of a rectangle and a circle with user-provided dimensions.
# 



import circle_module as c
import rectangle_module as r

length=int(input("enter the length of the rectangle "))

breadth=int(input("enter the breadth of the rectangle "))

print("Area of rectangle is ",r.area(length,breadth))

radius=int(input("enter the radius of circle "))

print("Area of circle is ",c.area(radius))


