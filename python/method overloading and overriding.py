# method overloading:
# in a class if there is two methods with same name but different parameters it is called method over loading
# in python there is no method overloading it does not support method overloading
#class Student:

 #   def avg(a,b):
  #      print('avg1')

   # def avg(a,b,c):
    #    print('avg2')


#a1=Student()
#b1=Student()
#a1.avg(2,3)
#b1.avg(2,3,5)


# method overriding:
# if we have two methods with same and same parameters but in different class
# in inheritance if one class having the method and in other class also having the same method and same
# parameters in that case the child class overrides the parent class. this is caLLED METHOD OVERRID
# normal inheritance:

class A:
    def feature(self):
        print('it is the feature of A')


class B(A):
    pass


b1=B()
b1.feature()

# applying method overriding:


class A:
    def feature(self):
        print('it is the feature of A')


class B(A):
    def feature(self):
        print('feature of B')

a1=A()
b1 = B()
b1.feature()     #here B override the A





