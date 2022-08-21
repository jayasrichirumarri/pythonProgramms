#sample function
def fun(): #function defination
    print("hello world")
fun()   #function calling
#we can call that function for any time to print hello world
fun()
fun()

#adding two numbers
def adding(x,y):
    z=x+y
    print(z)
adding(5,6)

#return:it is returning something if we dont want to exicute that function
def adding(x,y):
    z=x+y
    return z
result=adding(5,6)

print(result)


#returning two values
def mul_div(a,b):
    c=a*b
    d=a/b
    return c,d
result=mul_div(6,7)
print(result)


#function arguments
def arg(x):
    x=4
    print(x)
arg(8)


def arg(x):
    x=4
    print(x)
result=arg(8)
print(result)


def arg(x):
    x=4
    print(x)
result=7
arg(result)
print(result)

def arg(x):
    print(id(x))
    x=4
    print(x)
a=7
print(id(a))
arg(a)
print(a)


def arg(x):
    print(id(x))
    x=4
    print(id(x))
    print(x)
a=7
print(id(a))
arg(a)
print(id(a))
print(a)








