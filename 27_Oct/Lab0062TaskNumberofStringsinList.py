#5. Write a Python program to count the number of strings in a list where
# the string length is 2 or more and the first and last character are the same.

Lst = ["priy","mathm","sauras","teeth","troll","pic","else"]
count = 0
for x in Lst:

    if len(x) >= 2 and x[0] == x[-1]:
        count = len(x)

print(count)