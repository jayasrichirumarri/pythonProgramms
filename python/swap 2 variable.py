#using temparary variable
a=4
b=5
temp=a
a=b
b=temp
print(a)
print(b)
#traditional methodrot_two()tworoattion method
a=4
b=5
a,b=b,a
print(a)
print(b)
#using another method
a=4
b=5
a=a+b
b=a-b
a=a-b
print(a)
print(b)