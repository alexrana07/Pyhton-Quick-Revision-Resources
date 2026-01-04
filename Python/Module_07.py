"""
1.What is list?
ans:A list is used to store multiple values in one variable.
It keeps items in order and you can change them anytime.
Example (Python): fruits = ["apple", "banana", "mango"]
note:list is mutable.

a list can be created in a few simple ways. Here are the most common and easy methods:
1.Using square brackets [] (most common)
example:
my_list = [1, 2, 3, 4]

2.Creating an empty list
example:
empty_list = []
Creates a list with no elements

3.Using the list() constructor
example:
my_list = list((10, 20, 30))
Converts values into a list

4.Creating a list from a string
example:
chars = list("Python")
Output:
['P', 'y', 't', 'h', 'o', 'n']

5.Using range() to create a list
example:
numbers = list(range(1, 6))
Output:
[1, 2, 3, 4, 5]


"""
#create simple list
numbers = [10, 20, 30, 40]

#all important list functions

#1. append() – Add one item at the end
numbers.append(50)
print(numbers)
#Output:[10, 20, 30, 40, 50]

#2. insert() – Add item at specific position
numbers.insert(1, 15)
print(numbers)
#Output:[10, 15, 20, 30, 40, 50]

#Explanation:
#Adds 15 at index 1.

#3. extend() – Add multiple items
numbers.extend([60, 70])
print(numbers)
#Output:[10, 15, 20, 30, 40, 50, 60, 70]

#4. remove() – Remove specific value
numbers.remove(20)
print(numbers)
#Output:[10, 15, 30, 40, 50, 60, 70]

#Explanation:
#Removes the first occurrence of 20.

#5. pop() – Remove item by index
numbers.pop()
print(numbers)
#Output:[10, 15, 30, 40, 50, 60]

#Explanation:
#Removes the last element.

#6. sort() – Arrange in ascending order
numbers.sort()
print(numbers)

#Output:[10, 15, 30, 40, 50, 60]

#7. reverse() – Reverse the list
numbers.reverse()
print(numbers)
#Output:[60, 50, 40, 30, 15, 10]

#8. count() – Count number of occurrences
print(numbers.count(30))
#Output:1

#Explanation:
#Counts how many times 30 appears.

#9. index() – Find position of item
print(numbers.index(40))
#Output:2

#Explanation:
#Returns the index position of 40.

#10. copy() – Copy the list
new_list = numbers.copy()
print(new_list)
#Output:[60, 50, 40, 30, 15, 10]

#Explanation:
#Creates a new list with same elements.


#11. Built-in Functions

#len() – Total elements
print(len(numbers))
#Output: 6

#max() – Largest value
print(max(numbers))
#Output:60

#min() – Smallest value
print(min(numbers))
#Output:10

#sum() – Total of elements
print(sum(numbers))
#Output:205

#12. clear() – Remove all elements
numbers.clear()
print(numbers)
#Output:[]

#Explanation:
#Deletes all items from the list.

