# Python Inheritance
'''
Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class: is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.
'''

class Parent:
    def __init__(self,name,age):
        self.name= name
        self.age = age

    def printInfo(self):
        print(f'{self.name} {self.age}')

class Child(Parent):
    def __init__(self, Parent,name):
        super().__init__(Parent.name, Parent.age)
        self.name = name

    def printInfo(self):
        print(f'my name {self.name}')

p1 = Parent('Ganesh',45)
p1.printInfo()

c1 = Child(p1,'harsh')
c1.printInfo()