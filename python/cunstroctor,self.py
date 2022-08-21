# the constructor internally calls the init method we dont want call it seperately

class Computer:
    def __init__(self):
        print('hello world')
c1=Computer()     #it is the constructor


#here we cannot use any method
class Computer:
    def __init__(self):
        self.name='navin'
        self.age=28
c1=Computer()
c2=Computer()
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

#here we are using update method
class Computer:
    def __init__(self):
        self.name='navin'
        self.age=28
    def update(self):
        self.age=26
c1=Computer()
c2=Computer()
c1.update()
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

#self is referring to the object
#it is an instance of a class or an object
#it helps todifferentiate b/w the methods and attributes of a class with local varisbles

#how to compare one object with oher object
#here we are giving same age
class Computer:
    def __init__(self):
        self.name='navin'
        self.age=28
    def compare(self,other):

        if self.age==other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()
if c1.compare(c2):
    print('they are same')
else:
    print('they are different')

#we are giving different age
class Computer:
    def __init__(self):
        self.name = 'navin'
        self.age = 28

    def compare(self, other):
        self.age=26
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()
if c1.compare(c2):
    print('they are same')
else:
    print('they are different')


#compare is not a builtin function or method



