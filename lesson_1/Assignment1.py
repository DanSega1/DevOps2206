# First Assignment for Python
# A
first = 7
second = 44.3
# print(first + second)
# print(first * second)
# print(first / second)
# print(second / first)

# B
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8

print(a + b + c)  # 32

# C
# Is there a difference between the two lines below? Why?
# name = "john"
# name = 'john'
"""
no, there are the same because the type of the variable is string we can choose
to use "" or ''. just be consistent in our code.
"""

# original
# my_number  = 5+5
# print("result is : "+my_number)
my_number = 5+5
# print("result is : "+int(my_number))

print("result is : "+str(my_number))
# the type of my_number is int and i change it to string

# D

x = 5
y = 2.36
print(x + int(y))
'''
the answer is 7 because i change the type of y to int,
and int is only the number before the point, to use the number after the
point i need to use float
'''
print(x + y)
print(type(x) and type(y))  # int and float

# Challenge
# fix the following code, without changing a or b
a = 8
b = "123"
'''
print(a+b)  will raise error because 'b' is string and 'a' is int
make b to int
'''
print(a + int(b))


