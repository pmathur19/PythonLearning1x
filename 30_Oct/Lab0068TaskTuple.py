#Find the maximum and minimum elements in a tuple.

my_tuple = (15, 8, 25, 36, 42, 10)
my_tuple_list = list(my_tuple)
my_tuple_list.sort()

print("Maximum number in tuple is :",my_tuple_list[-1])
print("Minimum number in tuple is :",my_tuple_list[0])


#Find the intersection and union of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set3 = set1.intersection(set2)
print("intersection of set1 and set2 ", set3)
set4 = set1.union(set2)
print("union of set1 and set2 ", set4)


#Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
my_list = list(set(my_list))
print("List without any duplicates ", my_list)