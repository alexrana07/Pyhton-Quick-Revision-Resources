"""
1.What is Type Casting?
ans:Type casting is the process of converting one data type into another data type in a program manually.

In simple words:
Type casting means changing the type of data from one form to another.

2.Why Do We Need Type Casting?
We need type casting when:
We want to perform operations on different data types
We need data in a specific format
We want correct results in calculations

3.Real-Life Example 

Think of water:
Water can be ice, liquid, or steam
Same substance, different forms

Similarly:
Data can be integer, float, or string
Same value, different data types

4.What is type-Conversion?
ans:Type conversion is the process of changing one data type into another. 
It can be automatic when the system converts the data type by itself,
which is called implicit type conversion, 
or manual when the programmer converts it explicitly.

Example: Integer to Float
a = 10      # int
b = 2.5     # float
c = a + b
print(c)

Output:
12.5

Explanation:
a is integer
b is float
Computer converts a to float automatically

Result is float

Important Note:

This will NOT work automatically:

a = "10"
b = 5
print(a + b)
Because string cannot be automatically converted to integer.
"""

#Type Casting Functions:

#1. int() – Convert to Integer
#Example:
x = 10.7
y = int(x)
print(y)

#Output: 10
#Converts float to integer (decimal part removed)

#2. float() – Convert to Float
#Example:
a = 5
b = float(a)
print(b)

#Output:5.0
#Converts integer to float

#3. str() – Convert to String
#Example:
age = 18
print("Age is " + str(age))

#Output: Age is 18
#Converts number to string

#4.bool() – Convert to Boolean
#Example:
print(bool(1))
print(bool(0))

#Output:
True
False

#1 → True
#0 → False

