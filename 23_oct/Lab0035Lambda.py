
#Create a Lambda expression to triple power 2**3 a number


x=int(input("Enter number : "))
triple=lambda x : x**3

print(f'Cube of {x} is : {triple(x)}')