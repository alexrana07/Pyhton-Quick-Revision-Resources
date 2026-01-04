"""
1. What is File Handling?
ans:File handling allows a Python program to:
Create files
Read data from files
Write data into files
Append data to files

In simple words:
File handling is used to store data permanently.

2. Why Do We Need Files?
ans:Variables store data temporarily
Files store data permanently

Useful for:
Student records
Reports
Logs
Data storage

3. Basic Steps of File Handling
Open a file
Perform operation (read / write / append)
Close the file

4. File Modes
Mode	Meaning
r	Read
w	Write (creates new file / overwrites)
a	Append
r+	Read and write
w+	Write and read
a+	Append and read
"""

#1. Basic Steps of File Handling
'''
Open a file
Perform operation (read / write / append)
Close the file
'''
#Syntax:
file = open("filename", "mode")

#2. Writing to a File
file = open("student.txt", "w")
file.write("Welcome to Python File Handling")
file.close()

#Creates file if it does not exist
#Overwrites existing content

#3. Reading from a File
file = open("student.txt", "r")
content = file.read()
print(content)
file.close()

#4. Append to a File
file = open("student.txt", "a")
file.write("\nThis line is appended")
file.close()

#Old data is safe
#New data is added at the end

#5. Using with Statement (Best Practice ✅)
with open("student.txt", "r") as file:
    print(file.read())

#Automatically closes the file
#Cleaner and safer

#5. Reading Line by Line
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

#6. Writing Multiple Lines
lines = ["Python\n", "File Handling\n", "Revision Notes\n"]

with open("notes.txt", "w") as file:
    file.writelines(lines)

#7. File Handling with Functions
def save_message(msg):
    with open("msg.txt", "a") as file:
        file.write(msg + "\n")

save_message("Hello Students")

'''
Files are used for permanent storage
open() is used to open a file
Always close a file or use with
Modes decide file operation
'''

