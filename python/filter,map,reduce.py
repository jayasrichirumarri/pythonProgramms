# filter:filter(function,iterable)
# by using lambda
nums=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(lambda a:a%2==0,nums))
print(evens)


# by using function
def is_even(a):
    return a%2==0
num=[11,12,13,14,15,16,17,8]
evens=list(filter(is_even,num))
print(evens)

# map:map(function,iterable)
# by using function
def double(n):
    return n*2
nums=[1,2,3,4,5,6,8,7,9]
doubles=list(map(double,nums))
print(doubles)

# by using lambda
nums=[1,2,3,4,5,6,8,7,9]
doubles=list(map(lambda n:n*2,nums))
print(doubles)

# reduce:to use reduce we import reduce from functools
# reduce(fuction,iterable)
# by using function
from functools import reduce
def sum(a,b):
    return a+b
no=[7,6,5,4,3,2,1]
sum=reduce(sum,no)
print(sum)

#by using lambda
no=[7,6,5,4,3,2,1]
sum=reduce(lambda a,b:a+b,no)
print(sum)



