# when we are giving user input value of type integer but it takes
# that value as a string.

x=input('enter 1st number')
y=input('enter 2nd number')
z=x+y
print(z)

# so we use int() to overcome that problem


x=int(input('enter 1st number'))
y=int(input('enter 2nd number'))
z=x+y
print(z)

#another way is


x=input('enter 1st number')
a=int(x)
y=input('enter 2nd number')
b=int(y)
z=a+b
print(z)

# for charecters

ch=input('enter a charecter')
print(ch[0])
print(ch[1])
print(ch[2])
print(ch)

# we can evaluate an expression with input function

result=eval(input('enter an expression'))
print(result)

# finding the cube of a number

x=int(input('enter a number :'))
z=x*x*x
print(z)

import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=x+y
print(z)
