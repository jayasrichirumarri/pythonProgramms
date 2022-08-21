# adding two numbers

num1=25
num2=30
sum=num1+num2
print('sum of {} and {} is {}'.format(num1,num2,sum))

# maximum of two numbers
def maximum(a,b):
    if a>=b:
        return a
    else:
        return b
result=maximum(5,6)
print(result)

# factirial of a number
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

result=fact(5)

print(result)

# using recursion finding factorial
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(6)
print(result)

# finding simple interest
def simint(p,t,r):
    print('the principal is',p)
    print('the time period is',t)
    print('the rate of interest is',r)
    si=p*t*r/100
    return si
result=simint(10,3,2)
print(result)

# finding compound interest
def compint(p,r,t):
    amount=p*(pow((1+r/100),t))
    ci=amount-p
    print('compound interest is',ci)
compint(1000,10,2)

# area of a circle
def circle(r):
    PI=3.142
    Area=PI*(r*r)
    return Area

result=circle(5)
print(result)

# finding prime no in given interval
lower=0
upper=100
print("print the prime no b/w ",lower,"and",upper,"are:")
for j in range(lower,upper+1):
    if j>1:
        for i in range(2,j):
            if j%i==0:
              break
        else:
            print(j)

# check whether the given no is prime or not
nums=int(input('enter a number:'))
if nums>1:

   for i in range(2,nums):
        if nums%i==0:
            print('not a prime')
            break
   else:
    print('prime')
else:
    ('not a prime ')

# finding the nth fibonacci number
def fib(n):
    if n<=0:
        print('incorrect output')
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))

# another way
def fib(n):
   if n==0:
       return 0
   elif n==1:
       return 1
   else:
       return fib(n-1)+fib(n-2)

print(fib(8))

#finding first 10 fibonacci series
def fib(n):
   if n==0:
       return 0
   elif n==1:
       return 1
   else:
       return fib(n-1)+fib(n-2)
for i in range(2,10):

   print(fib(i))