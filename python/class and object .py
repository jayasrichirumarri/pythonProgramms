# class:a class is a collection of objects or it is the blueprint of objects.
# object:objects are an instance of a class.objects are the real world entities.

class Computer:      #Computer is the class
    def config(self):
        print("16,'i5',dell")
comp1=Computer()    # comp1 is object
comp2=Computer()    # comp2 is an object

# to call function we use twotypes
# using class to call function by passing object

Computer.config(comp1)
Computer.config(comp2)

# using object to call function
comp1.config()
comp2.config()
print(type(comp1))



 def config(self,name):
     self.name=name
        print(self.name)

comp1=Computer()    # comp1 is object
comp2=Computer()    # comp2 is an object
