# in oops there are two types of variables
# 1.instance variables
# 2.class variables
# 1.instance variables:if we define a variable inside the __init__ it becomes instance variable.
# namespaces: namespace is an area where you can crate and store the object/variable
# these are two types
# class namespace:in this we store all class variables
# instance namespace: in this we store all instance variables

class Car:
    def __init__(self):
        self.mill=10               # instance variable
        self.com='bmw'             # instance variable


c1= Car()
c2=Car()
print(c1.mill,c1.com)
print(c2.mill,c2.com)

# in this if we change one object it can not affect on the other object

class Car:

    def __init__(self):
        self.mill=10               # instance variable
        self.com='bmw'             # instance variable


c1= Car()
c2=Car()
c1.mill=8
print(c1.mill,c1.com)
print(c2.mill,c2.com)

# 2.class variables(static): if we define a variable  outside the __init__ and inside the class it is the class variable.

class Car:

    wheels=4                             # class variable

    def __init__(self):
        self.mill = 10                   # instance variable
        self.com = 'bmw'                 # instance variable

c1 = Car()
c2 = Car()

c1.mill = 8

print(c1.mill, c1.com,c1.wheels)
print(c2.mill, c2.com,c2.wheels)

# if we change the wheels it will change in both the objects

class Car:

    wheels=4                             # class variable

    def __init__(self):
        self.mill = 10                   # instance variable
        self.com = 'bmw'                 # instance variable

c1 = Car()
c2 = Car()

c1.mill = 8
Car.wheels=5

print(c1.mill, c1.com,c1.wheels)
print(c2.mill, c2.com,c2.wheels)


