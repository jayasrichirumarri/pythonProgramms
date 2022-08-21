 # init method in class

class Computer:
   def __init__(self):
         print("init")

   def config(self):
        print("16,'i5',dell")
comp1=Computer()    # comp1 is object
comp2=Computer()    # comp2 is an object
comp1.config()
comp2.config()

#variables in init

class Computer:
   def __init__(self,name,age,city):
       self.name=name
       self.age=age
       self.city=city
   def config(self):
        print(self.name,self.age,self.city)
comp1=Computer('jai',25,'hyd')    # comp1 is object
comp2=Computer('sam',27,'bglr')    # comp2 is an object
comp1.config()
comp2.config()