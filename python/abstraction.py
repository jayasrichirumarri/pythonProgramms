# Abstract class: a class which will have abstract methods called abstract class.
# abstract method: method with declaration but not the definition is called abstract method.
# means method does not have a body.
# A.C will have at least one abstract method.
# we cannot create object of abstract class.
# python by default cannot support abstract classes.
# but we can import a module to work with abstract classes i.e.,ABC MODULE(abstract base classes).
# normal class and method
class Computer:
    def process(self):
        print('its running')


c1=Computer()
c1.process()

# normal class only with method declaration
class Computer:
    def process(self):
        pass


com=Computer()
com.process()

# using abstract class
#from abc import ABC,abstractmethod
#class Computer(ABC):                     # IN THIS class we get an error because we cannot create object forabstract class.
 #   @abstractmethod
  #  def process(self):
   #     pass


#com=Computer()

from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):        # here we get an error because we compalsary define the abstract method
    def process(self):
       pass                     # method without the body


lap=Laptop()


from abc import ABC,abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
       print('its working')


lap=Laptop()
lap.process()
