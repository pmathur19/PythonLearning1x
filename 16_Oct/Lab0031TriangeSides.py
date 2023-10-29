# Write a program that classifies a triangle based on its side lengths.

# Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).

# Use an if-else statement to classify the triangle.

L1=float(input("Enter side1 : "))
L2=float(input("Enter side2 : "))
L3=float(input("Enter side3 : "))

if L1==L2==L3:
    print(" triangle is equilateral")
elif L1==L2 or L2==L3 or L1==L3:
    print(" triangle is isosceles")
else:
    print(" triangle is scalene")