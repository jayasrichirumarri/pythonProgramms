# recursion:function calling it self is called recursion.
def examp(n):
    if n==5:
        return 'hello'
    return 'hi'
    examp()
examp(5)


def fact(n):

    if n==0:
        return 1
    return n*fact(n-1)




result=fact(5)
print(result)