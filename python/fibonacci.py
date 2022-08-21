def fib(n):

    a=0
    b=1

    if n==1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(10)


# another way

def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return f(n-1)+f(n-2)

for i in range(0,11):
    print(f(i))

