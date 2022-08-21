# lambda is an ananymous function means function without name

# normal function
def squre(a):
    result=a*a
    print(result)
squre(6)


# lambda for above function
# we can pass any no of arguments but it should be one expression only
# when we want a function for short term period in projects these functions are used

f=lambda a:a*a
result=f(6)
print(result)

f=lambda a,b,c:a+b-c
result=f(2,3,4)
print(result)
