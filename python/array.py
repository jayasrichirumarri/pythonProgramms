from array import *

#array can not support multidimentional array it support only single dimentional arrays
arr=array('i',[1,2,3,4,5])
print(arr)

val=array('i',[1,-2,3,5,6])
print(val)

# to get address and no of values present in an array
result=val.buffer_info()
print(result)

# to reverse the array values
val.reverse()
print(val)

# printing array values one by one
for i in val:
    print(i)
# another wAY when we know the length of the array
for i in range(5):
    print(val[i])

# getting the perticular valueby index
print(val[0])
print(val[1])
print(val[2])
print(val[3])

# for charecters
vals=array('u',['a','e','i','o','u'])
print(vals)
for i in vals:
    print(i)

# creating new array by using old array
newArray=array(val.typecode,(a for a in val))
print(newArray)

# if we square a in newarray
newArray=array(val.typecode,(a*a for a in val))
print(newArray)

#printing values 1 by 1in new array
for i in newArray:
    print(i)



# taking array values from user
arr=array('i',[])
n=int(input('enter the length of the array'))
for i in range(n):
    x=int(input('enter the next value'))
    arr.append(x)
print(arr)



