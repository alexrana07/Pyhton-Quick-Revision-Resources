"""
1.What is operators?
ans:operators are symbols or keywords used to perform operations on values or variables (called operands).

2.types of operators in python:
Arithmetic Operators
Comparison (Relational) Operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators
"""

# 1.Arithmetic Operators : An arithmetic operator in Python is used to do math calculations.
a = 5
b = 2

print(a + b) #Addition : 5 + 2 = 7
print(a - b) #Subtraction : 5 - 2 = 3
print(a / b) #Division : 5 / 2 = 2.5
print(a * b) #Multiplication : 5 * 2 = 10
print(a % b) #Modulus : 5 % 2 = 1
print(a // b) #Floor Division : 5 // 2 = 2
print(a ** b) #Exponent : 5 ** 2 = 25

# 2.Comparison (Relational) Operators : A comparison operator is used to compare two values. The result is always True or False.
print(a == b) #Equal to : 5 == 2 → False
print(a != b) #Not equal : 5 != 2 → True
print(a > b) #Greater than : 5 > 2 → True
print(a < b) #Less than : 5 < 2 → False
print(a >= b) #Greater or equal : 5 >= 2 → True
print(a <= b) #Less or equal : 5 <= 2 → False

# 3.Assignment Operators : An assignment operator is used to give a value to a variable or change its value.Logical Operators
a += b   # a = a + b → 5 + 2 = 7
a -= b   # a = a - b → 5 - 2 = 3
a *= b   # a = a * b → 5 * 2 = 10
a /= b   # a = a / b → 5 / 2 = 2.5
a //= b  # a = a // b → 5 // 2 = 2
a %= b   # a = a % b → 5 % 2 = 1
a **= b  # a = a ** b → 5 ** 2 = 25

# 4.Logical Operators : Logical operators are used to connect conditions and give a result as True or False.
#AND operator (and)
print(a > 3 and b < 3)   # both true = True

#OR operator (or)
print(a > 4 or b < 3)    # one true = True

#NOT operator (not)
print(not(a > 3))       # opposite result = False

# 5.Bitwise Operators : Used to work with binary numbers.
# &	AND
# `	`
# ^	XOR
# ~	NOT
# <<	Left shift
# >>	Right shift

# 6.Membership Operators : Used to test if a value exists in a sequence.
# in :- 'a' in 'apple' → True
# not in :- 5 not in [1,2,3] → True

# 7.Identity Operators : Used to compare memory location.
# is :- x is y
# is not :- x is not y


