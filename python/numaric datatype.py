#integer type
x=4
print(x)
print(type(x))
print(id(x))
#float type
y=3.4
print(y)
print(type(y))
print(id(y))
#complex type
z=5+6j
print(z)
print(type(z))
print(id(z))
#boolean type
i=23
j=45
bool=i>j
bool1=i<j
print(bool)
print(bool1)
print(type(bool))
print(int(True))
print(int(False))

#type conversion
#converting all types to int
a=int(y)
print(a)
#b=int(z)
#print(b)#we can not convert complex to int
#converting all types to float
p=float(x)
print(p)
#q=float(z) we can not convert float to complex
#print(q)
#converting all types to complex
s=complex(x)
print(s)
r=complex(y)
print(r)
#to check if an object is an iteger or not
x=200
print(isinstance(x,int))
