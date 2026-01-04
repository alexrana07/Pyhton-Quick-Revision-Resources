"""
1.What is input in Python?
ans:input() is a built-in function in Python used to take input from the user.
example:
name = input("Enter your name: ")
print("Hello", name)

2.What is Type Casting in Python?
ans:Type casting means converting one data type into another.
Done manually by the programmer
Happens explicitly
Uses built-in functions

example:
age = input("Enter age: ")   # string
age = int(age)              # string → integer

3.What is Type Conversion?
ans:Type conversion is the process in which Python automatically converts one data type into another when needed.
Done automatically
No programmer involvement
Also called implicit conversion

example:
x = 10      # int
y = 2.5     # float
z = x + y   # int is automatically converted to float

"""

# input
name = input("Enter your name: ")
print("Hello", name)

#type casting
age = input("Enter age: ")   # string
age = int(age)              # string → integer

#type conversion
x = 10      # int
y = 2.5     # float
z = x + y   # int is automatically converted to float



