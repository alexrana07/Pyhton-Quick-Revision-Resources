"""
1. What is a Conditional Statement?
ans:A conditional statement is used to make decisions in a program.
It allows a program to:
Check a condition
Execute different code based on True or False
In simple words:
Conditional statements help the program decide what to do.
"""

'''
Python has four main conditional statements:
1.if
2.if-else
3.if-elif-else
4.ested if
'''
#1. if Statement Syntax:
'''if condition:
    statement'''

#Example:
age = 20

if age >= 18:
    print("You are eligible to vote")

#Executes only if the condition is True

#2. if–else Statement
'''Syntax:
if condition:
    statement_if_true
else:
    statement_if_false'''

#Example:
num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#3. if–elif–else Statement - Used when there are multiple conditions.

'''Syntax:
if condition1:
    statement1
elif condition2:
    statement2
else:
    statement3'''

#Example:
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

#4. Nested if Statement - An if inside another if.

#Example:
age = 22
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")

#Logical Operators

#Example:
age = 19
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")

#Mini Project: Student Result System
'''Description:
This program:
Takes student marks
Decides Pass or Fail
Assigns grade
Uses conditional statements'''

#Code:
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "Fail"

print("\n--- Student Result ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)

