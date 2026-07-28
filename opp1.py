# Python classes and object
# Almost everything in python is a object, with properties and method.

# class Person:
#     name = " Harsh" # class property
#     occupation = "Software Engineer"
#     becam = "Billionaire"
#     def info(self):   # method
#         print(f'{self.name} is a {self.occupation}')

# a = Person() # creating object using class Person
# print(a.name)
# a.info()
'''
All methods must have self as the first parameter.


'''

# __ini__ method in opps
'''
All classes have a built-in method called __inti__(),
which is always executed when the class is being initiated.
The __inti__() method is used to assign values to object propoerties, or
to perform operations that are necessary when the object is being created.
The __init__() method is called automatically every time 
   the class is being used to create a new object.
'''

class Person:
    def __init__(self,name,age):
        self.name = name # instance property
        self.age = age

p1 = Person("Harsh",21)
print(p1.name)
print(p1.age)
print(f'name is {p1.name} and age {p1.age}')

'''
self parameter is a refeerence to the current instance of the class.
it is used to access properties and methods that belong to the class.
While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
'''