#Fibonacci Series

first,second=0,1
upto=int(input('Enter the series number upto which you wish to see: '))
for i in range(upto):
    if i ==0 or i==1:
        print(i, end=' ')
    else:
        third=first+second
        print(third, end=' ')
        first=second
        second=third