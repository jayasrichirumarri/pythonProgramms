# inheritance:one class inherits features of  the other class
# it is 3 types
# 1.single level inheritance
class A:                     #parent class
    def feature1(self):
        print('feature 1')

    def feature2(self):
        print('feature 2')


class B(A):                  #child class of A
    def feature3(self):
        print('feature 3')

    def feature4(self):
        print('feature 4')


a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()


# 2.multilevel inheritance
class A:                                #parent class
    def feature1(self):
        print('feature 1')

    def feature2(self):
        print('feature 2')


class B(A):                                   #child class of A and perent for C
    def feature3(self):
        print('feature 3')

    def feature4(self):
        print('feature 4')

a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()
b1.feature1()
b1.feature2()


class C(B):                                 #child class of B
    def feature5(self):
        print('feature 5')

    def feature6(self):
        print('feature 6')


c1=C()
c1.feature5()
c1.feature6()
c1.feature1()
c1.feature3()
c1.feature2()
c1.feature4()



# 3.multiple inheritance



class A:
    def feature1(self):
        print('feature 1')

    def feature2(self):
        print('feature 2')


a1=A()
a1.feature1()
a1.feature2()


class B:
    def feature3(self):
        print('feature 3')

    def feature4(self):
        print('feature 4')


b1=B()
b1.feature3()
b1.feature4()


class C(A,B):                                   # child class of A and B
    def feature5(self):
        print('feature 5')

    def feature6(self):
        print('feature 6')


c1=C()
c1.feature5()
c1.feature6()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()


