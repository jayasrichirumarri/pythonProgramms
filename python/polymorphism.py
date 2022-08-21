# polymorphism:
# poly means many morphism means forms
#there are 4 ways of implementing polymorphism
#duck typing
#operator overloading
#method overloading
#method overriding
#1.duck typing:

class Pycharm:
    def execute(self):
        print('compiling')
        print('running')


class Myeditor:
    def execute(self):
        print('spell check')
        print('convention')
        print('compiling')
        print('running')


class Laptop:
    def code(self,ide):
        ide.execute()


ide=Pycharm()
ide=Myeditor()
lap1=Laptop()
lap1.code(ide)


