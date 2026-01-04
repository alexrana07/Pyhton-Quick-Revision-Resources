"""
1. What is a for Loop?
ans:A for loop is used to iterate over a sequence such as:

list
tuple
string

range of numbers

Best when the number of iterations is known.

"""

#Syntax of for Loop
'''for variable in sequence:
    statement'''

#1. Example: Print Numbers from 1 to 5
for i in range(1, 6):
    print(i)

#Output:
1
2
3
4
5

#2. Example: Loop through a String
name = "Python"

for ch in name:
    print(ch)

#3. Example: Sum of Numbers
total = 0

for i in range(1, 6):
    total = total + i

print("Sum:", total)

#4. for Loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished")

#else executes after loop ends normally.
