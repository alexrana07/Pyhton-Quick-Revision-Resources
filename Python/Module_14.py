"""
8. What is a while Loop?
ans:A while loop runs as long as a condition is True.
Best when the number of iterations is not known.
"""

#Syntax of while Loop
"""while condition:
    statement"""

#1. Example: Print Numbers from 1 to 5
i = 1

while i <= 5:
    print(i)
    i += 1

#2. Example: Countdown Program
count = 5

while count > 0:
    print(count)
    count -= 1

print("Done!")

#3. Infinite Loop (Important Concept ⚠️)
while True:
    print("Hello")

#Runs forever unless stopped manually.
