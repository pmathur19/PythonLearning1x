# Create a function that calculates the sum of the digits of a positive integer.


def add_dig(a,num_len):
    x=0
    for i in range(0, num_len):
        x = int(a[i]) + int(x)
    return x

a= input("Enter any number\n")
num_len = int(len(a))
x= add_dig(a,num_len)
print(f"sum of digits in {a} is {x}")




def sum1(num1):
    res = 0
    for num in num1:
        res = res + int(num)
    return res


num1 = input("Enter the number\n")
print(sum1(num1))
