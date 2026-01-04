"""
1. What is a Function?
ans:A function is a block of reusable code that performs a specific task.
In simple words:
A function helps us reuse code instead of writing it again and again.

2. Why Do We Use Functions?
ans:Functions help to:
Reduce code repetition
Improve readability
Make programs easier to understand
Divide big programs into small parts

3. Types of Functions in Python
Python has two main types of functions:
1.Built-in functions (already provided by Python)
Example: print(), len(), sum()
2.User-defined functions (created by the programmer)

4. Defining a Function
Syntax:
def function_name():
    statement


def → keyword to define a function
function_name → name of the function
() → parameters (if any)
Indentation is mandatory
"""

#Example: Simple Function
def greet():
    print("Hello, Student!")

greet()

#Output: Hello, Student!

#1. Function with Parameters
#Parameters - Parameters are values passed to a function.

#Example
def greet(name):
    print("Hello", name)

greet("Alex")
greet("Ravi")

#2. Function with Multiple Parameters
def add(a, b):
    print("Sum:", a + b)

add(10, 20)

#3. Return Statement
'''
What is return?
ans:The return statement:
Sends a value back from a function
Ends the function execution
'''

#Example
def square(num):
    return num * num

result = square(5)
print(result)

#4. Function with Conditional Statement
def check_pass(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"

print(check_pass(65))

#5. Function with Loop
def print_table(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

print_table(5)

#6. Default Parameters
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Alex")

#7. Keyword Arguments
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="Alex")
