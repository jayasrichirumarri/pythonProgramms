# __init__() constructor:
#if we create the object of subclass it will first try to find the init of subclass it is not found then it will call init of super class

#if there is no init in B

class A:
    def __init__(self):
        print('in A init')


class B(A):
    def feature(self):
        print("it is feature of B")


a1=A()                                             #creating object of A

# if we create object of B

b1=B()



# if we put init in A and B

class A:
    def __init__(self):
        print('in A init')


class B(A):
    def __init__(self):                           #creating in B init
        print('in B init')
    def feature(self):
        print("it is feature of B")


a1 = A()  # creating object of A

b1=B()


# super()
# if in both A and B there is init then to call A init in B we super()

class A:
    def __init__(self):
        print('in A init')


class B(A):
    def __init__(self):                           #creating in B init
        super().__init__()
        print('in B init')


    def feature(self):
        print("it is feature of B")


a1 = A()  # creating object of A

b1=B()



#MRO:(METHOD RESOLUTION ORDER)
# if we use super in child sub class
# In mro the exicution is from left to right so only class X and Z  are exicuted
#x(left) z(middle) y(right)


class X:
    def __init__(self):
        print('in X init')

    def feature1(self):
        print("it is feature of X")


class Y:
    def __init__(self):                           #creating in B init

        print('in Y init')

    def feature2(self):
        print("it is feature of Y")


class Z(X,Y):
    def __init__(self):
        super().__init__()
        print("in Z init")
    def feature3(self):
       super().feature2()


z1=Z()

#we can also call other  methods with super()
z1.feature1()
z1.feature3()


