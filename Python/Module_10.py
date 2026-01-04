"""
1.What is set?
ans:a set is a built-in data type used to store a collection of unique elements.
Key characteristics of a set:
Unordered → items have no fixed position
No duplicates → repeated values are automatically removed
Mutable → you can add or remove elements
Unindexed → you can't access elements by index like set[0]
"""

#1️. Creating a Set
s = {1, 2, 3}

s = set([1, 2, 2, 3])
# Output: {1, 2, 3}
"""
Unique values
Unordered
Mutable
"""

# 2.Set Methods (ALL IMPORTANT ONES)

# add() - Adds one element to the set.
s = {1, 2}
s.add(3)
print(s)   #{1, 2, 3}

#update() - Adds multiple elements.
s = {1, 2}
s.update([3, 4, 5])
print(s)    # {1, 2, 3, 4, 5}

#remove() - Removes an element (error if not found).
s = {1, 2, 3}
s.remove(2)
#Error if element does not exist:
s.remove(10) 

#discard() - Removes an element (NO error if not found).
s = {1, 2, 3}
s.discard(10)   # No error

#pop() - Removes and returns a random element.
s = {1, 2, 3}
x = s.pop()
print(x)
print(s)

#clear() - Removes all elements.
s = {1, 2, 3}
s.clear()
print(s)   # set()

# 3.Set Operations Methods

#a.union() - Combines elements from both sets.
A = {1, 2}
B = {2, 3}

A.union(B)
# {1, 2, 3}

#Shortcut:
A | B

#b.intersection() - Common elements only.
A.intersection(B)
# {2}

#Shortcut:
A & B

#c.difference() - Elements in A but not in B.
A.difference(B)
# {1}
#Shortcut:
A - B

#d.symmetric_difference() - Elements not common to both.
A.symmetric_difference(B)
# {1, 3}

#Shortcut:
A ^ B

# 4.Built-in Functions Used With Sets

#len()
s = {1, 2, 3}
len(s)   # 3

#max() / min()
s = {5, 2, 9}
max(s)   # 9
min(s)   # 2

#sum()
s = {1, 2, 3}
sum(s)   # 6

#sorted() - Returns a sorted list (not a set).

sorted({3, 1, 2})
# [1, 2, 3]

# 5.Membership Test
s = {1, 2, 3}
2 in s     # True
10 in s    # False



