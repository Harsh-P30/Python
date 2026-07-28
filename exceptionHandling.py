a = int(input("Enter a numbser: "))

try:
    for i in range(1,11):
        print(f'{a} X {i} = {a*i}')
except TypeError:
    print(f'Not a integer: {TypeError}')
else:
    print("all good")

finally:
    print("good")