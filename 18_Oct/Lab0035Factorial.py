#Factorial

number=int(input('Enter the number: '))
output=1
for i in range(1,number+1):
    output*=i
print(f'Factorial of {number} is: {output}')