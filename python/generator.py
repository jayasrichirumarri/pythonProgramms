# in iterator we use iter and next functions
# instead of using both we use generators with hte help of "yield" keyword
# in functions we use return stmt but it returns only one value
# instead of return we use yield but it can be use for any no of times

def topten():
    return 5                 # using return


values=topten()
print(values)



def topten():
    yield 5                 # using yield


values=topten()
print(values)
print(values.__next__())



def topten():
    yield 1                 # using yield
    yield 2
    yield 3
    yield 4
    yield 5


values=topten()

print(values.__next__())
print(values.__next__())
for i in values:
    print(i)


# print perfect square of top10

def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1


values=topten()
for i in values:
    print(i)




