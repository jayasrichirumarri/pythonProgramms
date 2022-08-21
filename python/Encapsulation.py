# Encapsulation: wrapping up of data is called encapsulation.
# means wrapping some information into a single entity.
# combining the methods and variables into a single place.
# by implementing the classes we can achieve the encapsulation.
# it provides security for data by protecting from the outside world.

# access modifiers:
# in python 3 types of AM
# PUBLIC:anywhere we use.
class A:
    def __init__(self,a,b):
        self.a=a                    # public variables
        self.b=b                    # public variables

    def process(self):
        print(self.a,self.b)


a1=A(10,20)
a1.process()

# private:only inside the class.here the variables are started with ('__')double underscore.ex:__a,__x

class A:
    def __init__(self,a,b):
        self.__a=a                        # private variables
        self.__b=b                        # private variables

    def process(self):
        print("a:",self.__a)
        print("b:",self.__b)


a1=A(10,20)

# print(a1.self.__a)                   # we can not call private variables directly
# print(a1.self.__b)                    # we can not call private variables directly
a1.process()


# protected:inside the class and its sub class.here the variables are started with ('_')single underscore.
# ex:_a,_x



# another example for public and private variables
class  Employee:
    company="tcs"              #public variables
    __group="tata"             #private variables

    def getDetails(self):
        self.name=input("Name:")
        self.__Salary=input(self.name + "'s" + "Salary: ")
        self.Programming=input('programming:')

    def Display(self):
        print('Name:',self.name)
        print('Salary: ',self.Salary)
        print('programming Name: ',self.Programming)

    def RevisedSalary(self):
        print('existing salary: ',self.__Salary)
        self.__Salary=600000
        print('Revised Salary: ',self.__Salary)


e=Employee()
e.getDetails()
#e.Display()
e.RevisedSalary()

# example for protected variables

class Shape:
    _length=10
    _width=20


class Circle(Shape):
    def __init__(self):
        print(self._length)
        print(self._width)

cr=Circle()





