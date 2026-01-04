"""
1.What is dictionary?
ans:a dictionary is a built-in data type used to store data in key-value pairs.

2.What a Python dictionary looks like
student = {
    "name": "Alex",
    "age": 25,
    "course": "Python"
}

Keys → "name", "age", "course"
Values → "Alex", 25, "Python"

Key features of Python dictionaries:
Stored as key : value
Unordered (before Python 3.7), insertion-ordered (3.7+)
Keys are unique
Keys must be immutable (string, number, tuple)
Values can be any data type

"""

#create dictionary
student = {
    "name": "Alex",
    "age": 25,
    "course": "Python"
}

#1️. ACCESS OPERATIONS

#Access value by key
student["name"]

#Safe access (no error)
student.get("age")
student.get("grade", "Not Found")

#Add new key-value
student["city"] = "Delhi"

#Update existing key
student["age"] = 26

#Update multiple values
student.update({"age": 27, "course": "AI"})

#Remove by key
del student["course"]

#Remove and return value
student.pop("age")

#Remove last inserted item
student.popitem()

#Clear all items
student.clear()

#Check key exists
"name" in student

#Check value exists
"Alex" in student.values()


#2. BUILT-IN FUNCTIONS WITH DICTIONARY
len(student)
type(student)
str(student)
max(student)      # max key
min(student)      # min key
sorted(student)   # sorted keys
sum(student.values())

#3. DICTIONARY METHODS (ALL)

#clear() - Removes all items from the dictionary
student.clear()
#Output : {}

#2. copy() - Returns a shallow copy of the dictionary
student = {"name": "Alex", "age": 25}
new_student = student.copy()
#Output : {'name': 'Alex', 'age': 25}

#3. fromkeys(keys, value) - Creates a new dictionary from given keys
keys = ["name", "age"]
d = dict.fromkeys(keys, "NA")
#Output : {'name': 'NA', 'age': 'NA'}

#4. get(key, default) - Returns value of key (no error if key not found)
print(student.get("name"))
print(student.get("grade", "Not Found"))
#Output :Alex , Not Found

#5️. items() - Returns all key–value pairs as a view object
print(student.items())
#Output : dict_items([('name', 'Alex'), ('age', 25), ('course', 'Python')])

#6️. keys() - Returns all keys
print(student.keys())
#Output : dict_keys(['name', 'age', 'course'])

#7️. values() - Returns all values
print(student.values())
#Output : dict_values(['Alex', 25, 'Python'])

#8️. pop(key, default) - Removes specified key and returns its value
value = student.pop("age")
print(value)
print(student)
#Output 25 , {'name': 'Alex', 'course': 'Python'}

#9️. popitem() - Removes and returns the LAST inserted item
item = student.popitem()
print(item)
print(student)
#Output : ('course', 'Python'),{'name': 'Alex'}

#10. setdefault(key, default) - Returns value if key exists, else inserts key with default value
student.setdefault("grade", "A")
print(student)
#Output : {'name': 'Alex', 'age': 25, 'course': 'Python', 'grade': 'A'}

#1️1. update(other_dict) - Updates dictionary using another dictionary
student.update({"age": 26, "city": "Delhi"})
print(student)
#Output : {'name': 'Alex', 'age': 26, 'course': 'Python', 'city': 'Delhi'}
