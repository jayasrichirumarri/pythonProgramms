# inner class
# creating object of inner class inside the outer class
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
    def show(self):
        print(self.name,self.rollno)
    class Laptop:
        def __init__(self):
             self.brand='hp'
             self.ram=16
             self.cpu='i5'
s1=Student('navin',21)
s2=Student('jony',31)
s1.show()
lap1=s1.Laptop()
lap2=s2.Laptop()
print(id(lap1))
print(id(lap2))

# creating object of inner class outside the outer class

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def show(self):
        print(self.name,self.rollno)

    class Laptop:
        def __init__(self,brand,cpu,ram):
             self.brand='dell'
             self.cpu='i5'
             self.ram=16
        def show(self):
            print(self.brand,self.cpu,self.ram)
s1=Student('navin',25)
s2=Student('roj',27)
s1.Laptop.show()
s2.Laptop.show()
lap=Student.Laptop()









