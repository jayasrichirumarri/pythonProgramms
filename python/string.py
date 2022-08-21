#string creation
x='navin'
print(x)
print(type(x))
print(id(x))
#indexing
print(x[3])
print(x[1:])
print(x[:6])
#length of the string
print(len(x))
#multiline strings
y="""assining string to a variable"""
print(y)
#we cannot chnag ethe value of string strings are immutable

#x[2:4]='my'
#print(x)
z=x+' '+'youtube'
print(z)
#looping through the string
for i in z:
    print(i)

#if
if 'navin' in z:
    print('yes')
