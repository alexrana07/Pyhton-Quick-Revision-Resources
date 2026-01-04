"""
1. What is String?
ans: A string is a data type in Python.It is used to store text such as letters, words, or sentences.

2.How to Write a String in Python:
Single Quotes ' '
example:
text = 'Hello'

Double Quotes " "
example:
text = "Hello"

Triple Quotes ''' ''' or """ """
Used for long text or multiple lines.
example:
text = '''Hello
Welcome to Python'''

Triple Quotes are used for:
Write multiple lines
Write paragraphs
Write comments or documentation


3.Strings Can Contain
Letters → "Python"
Numbers → "123"
Symbols → "@#!"
Spaces → "Hello World"

"""


# 1.indexing in String : Indexing means accessing characters in a string using position numbers.

text = "Python"

"""
ach character has an index number.

Index	P	y	t	h	o	n
+ve	    0	1   2	3	4   5
-ve	   -6  -5  -4  -3  -2  -1


Indexing starts at 0
Negative indexing starts at -1
Used to get single character
String characters cannot be changed
"""

#Positive Indexing : Starts from 0 (left to right).
print(text[0])   # P
print(text[2])   # t
print(text[5])   # n


#Negative Indexing : Starts from -1 (right to left).
print(text[-1])  # n
print(text[-3])  # h

#Check Character:
char = text[1]
print(char)   # y

# 2.String Slicing : Slicing means cutting a part of a string.
"""
Syntax:
string[start : end]

start → where slicing begins (included)
end → where slicing stops (not included)

start is included
end is excluded
index starts from 0
negative index allowed
"""

#Basic Slicing:
print(text[0:4])   # Pyth
print(text[1:5])   # ytho
print(text[2:6])   # thon

#Slice from Start:
print(text[:3])    # Pyt

#Slice till End
print(text[3:])    # hon

#Negative Index Slicing
print(text[-4:-1]) # tho
print(text[-3:])   # hon

#Full String
print(text[:])     # Python


# 3.String Operations in Python : String operations are used to work with and manipulate strings.
#Example:
a = "Hello"
b = "World"

#a. Concatenation (Join strings)
print(a + b)        # HelloWorld
print(a + " " + b) # Hello World

#b. Repetition (Repeat string)
print(a * 3)   # HelloHelloHello

#c. Length of String
print(len(a))  # 5

#d. Membership Operators
print("H" in a)        # True
print("x" not in a)   # True

#e. Comparison of Strings
print("apple" == "apple")   # True
print("apple" != "Apple")   # True
print("a" > "b")            # False

# 4.String methods:
text = "Python"

#Case Conversion
text.lower()        # 'python'
text.upper()        # 'PYTHON'
text.title()        # 'Python'
text.capitalize()  # 'Python'
text.swapcase()    # 'pYTHON'
text.casefold()    # 'python'

#Searching & Checking
text.find("y")      # 1
text.rfind("o")     # 4
text.index("P")     # 0
text.count("o")     # 1
text.startswith("Py")   # True
text.endswith("on")     # True

#Character Type Checks
text.isalpha()      # True
text.isalnum()      # True
text.islower()      # False
text.isupper()      # False
text.istitle()      # True
text.isascii()      # True

#Modifying & Replacing
text.replace("Py", "My")   # 'Mython'
text.removeprefix("Py")   # 'thon'
text.removesuffix("on")   # 'Pyth'

#Alignment & Padding
text.center(10)    # '  Python  '
text.ljust(10)     # 'Python    '
text.rjust(10)     # '    Python'
text.zfill(10)     # '0000Python'

#Splitting & Joining
text.split("t")        # ['Py', 'hon']
"-".join(text)         # 'P-y-t-h-o-n'

