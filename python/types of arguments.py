#arguments are two types 1.formal,2.actual
#when we define arguments those are formal arguments
#when we call arguments those are actual arguments


def examp(x,y):    #here x,y are the formal arguments
    z=x+y
    print(z)
examp(4,5)             #here 4,5 are the actual arguments


#actual arguments are 5 types
#1.positi0n arguments

def person(name,age):
    print(name)
    print(age)
person('navin',26)   #here we can not change the position

#2.keyworded arguments

def person(name,age):
    print(name)
    print(age)
person(name='navin',age=26)    #here we use name and age as the keywords


#3.default arguments

def person(name,age=28):   #here the age is by defult given as 28
    print(name)
    print(age)
person('navin')


#variable length arguments
def adding(x,y):    #we do not use any v.l.a
    z=x+y
    print(z)
adding(5,6)

def adding(x,*y):
    print(x)
    print(y)
adding(5,6,7,8,9)



#def adding(x,*y):
    #z=x+y
    #print(x)
    #print(y)
    #print(z)
#adding(5,6,7,8,9)  #her ewe get an error

def adding(x,*y):
    for i in y:
        z=x+i
        print(z)
    print(y)
    print(x)
adding(5,6,7,8,9)


#5.keyworded variable length arguments
def person(name,*data):
    print(name)
    print(data)
person('navin','mumbai',28,83748543)  #here we dont know wt is 28,mumbai,59454595485 so we us k.v.l.a


def person(name,**data):
    print(name)
    print(data)
person('navin',city='mumbai',age=28,mob_no=83748543)     #here we use keywords


#use for loop
def person(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person('navin',city='mumbai',age=28,mob_no=83748543)
