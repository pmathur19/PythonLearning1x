#Bitwise Operators
'''
&  	AND 	Sets each bit to 1 if both bits are 1 	x & y|
OR 	Sets each bit to 1 if one of two bits is 1 	x | y
^ 	XOR 	Sets each bit to 1 if only one of two bits is 1 	x ^ y
~ 	NOT 	Inverts all the bits 	~x
<< 	Zero fill left shift.Shift left by pushing zeros in from the right and let the leftmost bits fall off 	x << 2
>> 	Signed right shift .Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off 	x >> 2
'''
a =5
print(a^6)
print(~a)   # -6
b =11
print(b << 2)   #44
print(b>>2)     #2