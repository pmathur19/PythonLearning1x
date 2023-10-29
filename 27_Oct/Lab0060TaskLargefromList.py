






## Write a Python program to find the largest number in a list
a=[3,7,9,1,6,9,22,17]
max_number=max(a)
print(f"The largest number in the list is:{max_number}")

#Write a Python program to find the smallest number in a list.
a=[3,7,9,1,6,9,22,17]
min_number=min(a)
print(f"The largest number in the list is:{min_number}")

print("-----------------------------------------------------------------------")



list1 = [10,1,2,3,5,8]
list1.sort()
print("the smallest number in the list", list1[0])
print("the largest number in the list", list1[len(list1)-1])

x = 0
for i in range(0,len(list1)):
    x = x + list1[i]
y = 1
for i in range(0,len(list1)):
    y = y * list1[i]

print("the sum of numbers in list",x)
print("the product of numbers in list",y)