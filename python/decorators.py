# using decorators we can add extra features to the existing function
# normal function

def div(a,b):
    print(a/b)


div(2,4)

# using decorators

def div(a,b):
    print(a/b)

def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
            return func(a,b)
    return inner
div=smart_div(div)
div(2,4)
