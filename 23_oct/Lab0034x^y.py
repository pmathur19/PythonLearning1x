#Create a Function with a Parameter which can do x^y

x=int(input("Enter x : "))
y=int(input("Enter y : "))

def calculate(x,y):
    return x^y

cal=calculate(x,y)
print(f'{x}^{y} is : {cal}')

#with Lambda as well
power = lambda x,y: x^y
print(power(x,y))