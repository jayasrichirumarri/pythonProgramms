# methods are 3 types

#1.instance method:it work with objects
class Student:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
s1=Student(34,24,54)
s2=Student(35,65,46)
print(s1.avg())
print(s2.avg())

#these are two type
#1.accessor method
#2.mutator method

def get_m1(self):    #getting the value(accessor)
    return self.m1
def set_m1(self,value):    #setting the new value(mutator)
    set.m1=value



#2.class method:it work with class variables

class Student:
    school="telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
    @classmethod       #decorator
    def info(cls):      #class method
        return cls.school
s1=Student(23,45,54)
s2=Student(24,76,47)
print(s1.avg)
print(Student.info())


#3.static method
@staticmethod
def info():
    print('this is student class in abc')
    Student.info()





