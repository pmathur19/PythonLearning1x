# 1. Use the ternary operator to find the maximum of three numbers entered by the user.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

max1 = (a if a > b and a > c else b if b > c else c)
print("Maximum of ", a, b, c, "is :", max1)