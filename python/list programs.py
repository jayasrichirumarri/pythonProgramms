def lst(nlst):
    size=len(nlst)
    temp=nlst[0]
    nlst[0]=nlst[size-1]
    nlst[size-1]=temp
    return nlst
nlst=[12,23,34,45]
print(lst(nlst))

# find the length of the list
lst=[12,3,4,5,6,7,8]
result=len(lst)
print(result)

# check if element exist in list or not
if 9 in lst:
    print(True)
else:
    print(False)

# clearing a list
lst.clear()
print(lst)

# finding the sum of the list
lst=[9,8,7,6,5]
result=sum(lst)
print(result)

# multiplying all elements in the list
def mul(lst):
    n=1
    for i in lst:
        n=n*i
    return n
lst=[9,8,7,6,5]
print(mul(lst))

# reversing a list
lst=[2,4,5,3,4,5,6]
lst.reverse()
print(lst)
print(min(lst))
print(max(lst))

# program to print even no in a list
lst=[12,13,14,15,16,56,35,23,34]
for i in lst:
    if i%2==0:
        print(i)

 # program to print odd no in a list
    lst = [12, 13, 14, 15, 16, 56, 35, 23, 34]
    for i in lst:
        if i % 2 != 0:
            print(i)





