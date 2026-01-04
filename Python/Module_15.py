"""
1. What are break and continue?
ans:break and continue are loop control statements.
They are used inside loops (for and while) to change the normal flow of a loop.


2.What is break?
ans:The break statement is used to immediately stop a loop.

When break is executed:
-The loop ends instantly
-Control moves outside the loop

3.What is continue?
ans:The continue statement skips the current iteration and moves to the next iteration of the loop.

When continue is executed:
Current iteration is skipped
Loop does not stop
Next iteration starts
"""

#1. break
'''
Syntax:
break
'''

#Example 1: Stop loop when number is found
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#Output
1
2
3
4

#Loop stops when i == 5

#Example 2: break in while loop
i = 1

while i <= 10:
    if i == 6:
        break
    print(i)
    i += 1

#Real-Life Example:
password = "python123"

while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access Granted")
        break

#Loop stops once correct password is entered


#2.continue
"""
Syntax:
continue
"""

#Example 1: Skip a number
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#Output
1
2
4
5

#Number 3 is skipped

#Example 2: continue in while loop
i = 0

while i < 5:
    i += 1
    if i == 2:
        continue
    print(i)

#Example 3: Print only odd numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
#Even numbers are skipped


# break and continue with Nested Loops

#break in nested loop
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)

#break stops only the inner loop

#continue in nested loop
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)

#Skips j == 2 only

