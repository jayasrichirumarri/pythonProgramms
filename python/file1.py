# to open a file
f=open('mydata','r')
print(f)
# to fetch the data
print(f.read())
# to read one line of data
print(f.readline())
print(f.readline())
print(f.readline())
# if we wnat to print some charecters in a line
print(f.readline(3))



f=open('files','r')
print(f)
print(f.readline(),end='')
print(f.readline())
print(f.readline(4))
# to write someting in a file
# if we dont have any file with abc name but we try to write a file then it automatically creates anew abc file.
f=open('abc','w')
print(f)

# to write something in a file
#.write('hello world')
# if we want to add some more information
#.write('frnds')
# if we wANT TO ADD some more infermation
f.write('adhbfhlsfd')    #but we last the reamining information to over come this problem
# we use append
f=open('abc','a')
f.write('djnoeprfreofnvfeofnvoef')

# to place one file data in another file
f1=open('anotherfile','r')
print(f1.read())
for data in f1:
    print(data)

f2=open('file','w')
for data in f1:
     f2.write(data)