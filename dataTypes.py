# Data Types in python 

# Numeric Types : Int, float, complex
# Integers: Whole numbers without a decimal point. Example: 1, 2, 3, -4, 0
integer_num = 10
print(integer_num)
# print("integer number: ",int(input("Enter a integer number: ")))

# float: Number with decimal
float_num = 10.5
print(float_num, "is comes under ",type(float_num))
print("Converting integer_num'10' into a float ",float(integer_num))

'''
complex number: pairs of floating-point numbers (real and imaginary parts) or
via built-in language types that handle the arithmetic automatically.
'''
# Python uses the built-in "complex" type or the j suffix.

print(complex(integer_num))
print(complex(float_num))

#  SEQUENCE TYPES 
# List  
''' List : List is a data type used to store collections of data, and it is ordered, changeable,
 and allow duplicate values.
- List items are indexed, the first item has index[0], the second item has index[1]...
- Ordered means items have defined order, and that order will not chnage.
    if you add new items to a list, the new items will be placed at the end of the list.
- Changeable: means that we can change, add, and remove items in a list after it has been created.
- Allow Duplicates: Since lists are indexed, list can have items with the same value.
    '''

mylist = [1,2,3,'we','are','good']
print(mylist)
print(mylist[1])
print(mylist[3:])
mylist[5] = "genious"
for i in mylist:
    print(i)

'''
To add items into list use 
.append(value) method to add an item to the end.
.insert(index,value) method to insert an item at the specified index.
.extend(another list name) method to append elements from another list to the current list
'''

mylist.append("boy")
print(mylist)

mylist.insert(0,5)
print(mylist)

anotherList = [0,1,2,3]
mylist.extend(anotherList)
print(mylist)

'''
To remove item use
.remove(value) method to removes the specified item.
.pop(index) method to removes the specified index.
del mylist[index] keyword also removes the specified index.
del myList keyword also del list completely,also remove esistent of list.
clear() method empties the list. List still remains, but it has no content.
'''

mylist.remove("boy")
print(mylist)
mylist.pop(0)
print(mylist)
del mylist[9]
print(mylist)
# del mylist
# print(mylist)

mylist.clear()
print(mylist)

'''
List methods
- append()
- clear()
- copy()
- count()
- extend()
- index()
- insert()
- pop()
- remove()
- reverse()
- sort()
'''

# Tuples
'''
Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and "unchangeable". Allow duplicate items.
'''
mytuple= (1,2,3,"i","am","")
print(mytuple)

print(mytuple[1])
'''
Unpack tuple
'''
fruits = ("apple","banana")
(green,yellow) = fruits
print(green)
print(yellow)
'''
Tuple Method
- count()
- index()
'''

# MAPPING TYPES
# Dictionary
'''
Dictionary are used to store data values in key:value pairs. 
    And can be referred to by using the key name
A dictionary is a collection which is ordered,changeable and do not allow duplicates.

'''

mydict = {
    1:"one",
    2:"two",
    3:"three"
}

print(mydict)
print(mydict[2])
x = mydict.get(1)
print(x)
print(mydict.keys())
print(mydict.values())
print(mydict.items()) # return as tuple
print(1 in mydict) # check key is present or not.
mydict.update({4:"four"}) # add items 
print(mydict)
mydict[5] = "five"
mydict[3]="THREE" # change value
print(mydict)

'''
Methods in Dictionary
- clear()
- copy()
- fromkeys()
- get()
- items()
- keys()
- pop()
- popitem()
- setdefault()
- update()
- values()
'''