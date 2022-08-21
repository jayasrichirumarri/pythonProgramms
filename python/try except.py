# errors are three types
#compile time error
#run time error
#logical error
# we can handle errors by using try stmt
# try: test a block of code for errors
# except: handle the errors
# else: exicute code when there is no error
# finally: exicute the code regardless of the result of the try and except blocks.
# this block will get exicuted if we dont get error as well as if we get error.
# raise: to throw an exception if a condition occurs we use "raise" keyword

a=5
b=2
try:
    print(a/b)

except Exception:
    print('hey, you cannot divide a no by zero')
print('bye')


a=5
b=0
try:
    print(a/b)

except Exception:
    print('hey, you cannot divide a no by zero')
print('bye')


a=5
b=2
try:
    print('resource open')
    print(a/b)
    print('resource closed')

except Exception as e:
    print('hey, you cannot divide a no by zero')
print('bye')


a=5
b=2
try:
    print('resource open')
    print(a/b)


except Exception as e:
    print('hey, you cannot divide a no by zero')
    print('resource closed')
print('bye')


a=5
b=0
try:
    print('resource open')
    print(a/b)


except Exception as e:
    print('hey, you cannot divide a no by zero')
    print('resource closed')
print('bye')

a=5
b=0
try:
    print('resource open')
    print(a/b)


except Exception as e:
    print('hey, you cannot divide a no by zero')


finally:
    print('resource closed')



a = 5
b = 2
try:
    print('resource open')
    print(a / b)


except Exception as e:
        print('hey, you cannot divide a no by zero')

finally:
        print('resource closed')




#dealing with different errors
a=5
b=2
try:
    print('resource open')
    print(a/b)
    k=int(input('enter a number'))
    print(k)
except ZeroDivisionError as e:
    print('you cannot divide a no by zero',e)
except ValueError as e:
    print('invalid input',e)
except Exception as e:
    print('something went wrong',e)
finally:
    print('resource closed')


# raise keyword:

x="hello"
if not type(x) is int:
    raise TypeError('only integer are allowed')
