
# Enter input string
a=input("Enter string:")
# Declare an empty string variable
b = (a[::-1]) # Slicing the entire string and the taking step -1, start at the end and end when nothing is left
print(b)
print("Reversed string:", b)
if a!= b:
    print(f"The string is not a palindrome")
else:
    print(f'The string is a palindrome')


def pal_checker(a):
        a_len = int(len(a))
        print(a_len - 1)
        x = (a[::-1])
        print(x)
        return x


a = input("enter the string\n")
z = pal_checker(a)
if a == z:
  print(f"{a} is palindrome")
else:
  print(f"{a} is not palindrome")



