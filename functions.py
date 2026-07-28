def fun1():
    print("Function Creation")

fun1()

def fun2(a,b):
    print(a+b)
fun2(4,5)


# *args is Arbitrary arguments
def fun3(*args):
    a=0
    for i in args:
        a +=i
    print(a)

fun3(1,2,3,4)

# **kwargs keyword argument pass

def fun4(**krgs):
    print("First Name: "+ krgs['fname'])
    print("Last Name: "+ krgs['lname'])

fun4(fname="Harsh",lname="Prasad")
