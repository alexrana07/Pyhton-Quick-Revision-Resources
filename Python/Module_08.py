"""
1.What is tuple?
ans:A tuple is a collection (data structure) used in programming to store multiple values in a single variable.
Key characteristics of a tuple
Ordered - items have a fixed position (index-based)
Immutable - values cannot be changed after creation
Allows duplicates
Can store different data types together

2.A tuple is created by placing values inside parentheses (), separated by commas.

1. Creating a tuple (Python)
t = (1, 2, 3)

2. Tuple without parentheses (comma matters)
t = 1, 2, 3
Still a tuple because of the comma

3. Single-element tuple (important!)
t = (5,)
Not a tuple:
t = (5)   # This is just an integer

4. Empty tuple
t = ()

5. Tuple with different data types
t = (10, "apple", 3.14, True)

6. Creating a tuple using tuple() constructor
t = tuple([1, 2, 3])     # from list
t = tuple("hello")      # from string → ('h','e','l','l','o')

"""

#Tuples are immutable, so they have very few methods.

#1. count() - Returns how many times a value appears.
t = (1, 2, 2, 3)
t.count(2)   # 2

#2. index() - Returns the index of the first occurrence of a value.
t = (10, 20, 30)
t.index(20)   # 1


#Tuple Operations:

#1. Accessing Elements (Indexing)
t = (10, 20, 30)
t[0]      # 10
t[-1]     # 30

#2. Slicing
t = (1, 2, 3, 4, 5)
t[1:4]    # (2, 3, 4)

#3. Concatenation (+)
t1 = (1, 2)
t2 = (3, 4)
t1 + t2   # (1, 2, 3, 4)

#4. Repetition (*)
t = (1, 2)
t * 3     # (1, 2, 1, 2, 1, 2)

#5. Membership (in, not in)
t = (10, 20, 30)
20 in t        # True
40 not in t    # True

#6. Length (len())
t = (1, 2, 3)
len(t)   # 3    

#7. Converting Tuple to List (to modify)
t = (1, 2, 3)
l = list(t)
l.append(4)
t = tuple(l)

#10. Tuple Packing
t = 1, 2, 3

"""
meaning:
Python automatically packs the values 1, 2, and 3
It puts them together into one tuple
That tuple is stored in variable t"""

#11. Tuple Unpacking
a, b, c = (10, 20, 30)

"""
meaning:
The tuple (10, 20, 30) is on the right side
Python unpacks the tuple
Each value is assigned to a separate variable
Step-by-step:
Tuple Value	Variable
10	a
20	b
30	c

"""

#12. Built-in Functions Used with Tuples

#min()	
min((3,1,2))	#1

#max()	
max((3,1,2))	#3
#sum()	
sum((1,2,3))	#6

#sorted()	
sorted((3,1,2))	#[1,2,3]

#tuple()	
tuple([1,2])	#(1,2)

#any()	
any((0,1,0))	#True

#all()	
all((1,2,3))	#True