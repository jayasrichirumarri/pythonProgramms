# global variables: variables that are created outside of a function is called global variables.
# global variables can be used in both inside or outside of a function.

x='hello'                      # global variable
def update():
    print(x)                   # using inside the function

update()


x='hello'                      # global variable
def update():

    x='hi'                     # local variable

update()
print(x)                   # using outside the function

# local variables can be used inside the function only
# we can not use outside the function

x='hello'                      # global variable
def update():

    x='hi'                     # local variable
    print(x)                   # local variable using inside the function
update()
print(x)


x='hello'                      # global variable
def update():

    y='hi'                     # local variable
    print(x)
update()
#print(y)                       # local variable using outside the function(here we get an error)


# by using "global" keyword we can solve the above problem means to create a global
# variable inside a function ,we can use global keyword.

def my_func():
    global x
    x = 'awesome'
my_func()
print(x)

# also we can change the value of global variable inside the function ,refer to the variable by using global

x='fantastic'
def my_func():
    global x
    x = 'awesome'
my_func()
print(x)

# another example
a=10
def func():
    global a
    a=15
    print('in func',a)
func()
print('out func',a)

# global function

a=10
print(id(a))
def something():
    a=9
    x=globals()['a']
    print(id(a))
    print('in func',a)
something()
print('outside of func',a)

# changing global variables with global function

a=10
print(id(a))
def something():
    a=9
    x=globals()['a']=15
    print(id(a))
    print('in func',a)
something()
print('outside of func',a)



