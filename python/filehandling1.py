# file handling:python has several functions for creating,reading,updating,and deleting files
# to work with files we use open() function
# the open() function takes two parameters
# 1.filename and 2.mode
# to open a file there are 4 methods
# "r":read -default value.opens file for reading .if there is no file for reading it gives an error.
# "a":Append-opens a file for appending,if does not exist it create new file.
# "w":Write-opens a file for writing,creates the file if it does not exist.
# "x":create-creates the specified file,returns an error if the file exists.

# there are two types of files.
# 1.text files-"t"
# 2.binary files-"b"

# to open a file for reading
f=open('mydata','r')
print(f)
# to read data from a file
# print(f.read())
# it is used to read data line by line
print(f.readline())
# to get the first 5 characters
print(f.read(5))
# to print all lines in a file
for i in f:
    print(i)
# to closing a file we use

f.close()

# write to an existing file
f1=open('file','w')
f1.write('hello world')

# to add something to the existing file we use append
f1=open('file','a')        # if we use 'w' instead of 'a' it will overwrite the data in file and repalce it with new data
f1.write('good evening')
f1=open('file','r')
print(f1)

# creating a new file
# f2=open('mifile','x')
# print(f2)

# deleting files
# to delete file we import 'os' module
# and run its using os.remove() function
import os
# os.remove('abc')

# check if file exist or not
if os.path.exists('abc'):
    os.remove('abc')
else:
    print('file does not exist')

# deleting a folder
os.rmdir('myfolder')


