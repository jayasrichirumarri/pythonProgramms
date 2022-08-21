a=34
b=65

#simple if
if a<b:
    print("b is greater tha a")

#if else
a=43
b=54
if a<b:
    print('b is greater than a')
else:
    print('a is greater than b')

# nested if
a=33
r=a%2
if r==0:
    print('even')
    if a>35:
        print('great')
    else:
        print('small')
else:
    print('odd')
print('bye')

#if elif else
x=5
if x==1:
    print('one')
elif x==2:
    print('two')
elif x==3:
    print('three')
elif x==4:
    print('four')
if x==5:
    print('five')
else:
    print('wrong input')

#short hand if
a=2
b=3
if a<b:print('b is greater')

#short hand if else(ternary operator)
a=3
b=5
print('a is greater') if a>b else print('b is greater')

#if we want to put our if stmt empty we use pass stmt to avoid an error
if a>b:
    pass



a=45
b=43
c=65
if a>b and a>c:
    print('both conditions are true')
else:
    print('one condition is true')

    a = 45
    b = 43
    c = 65
    if a > b or a > c:
        print('both conditions are true')
    else:
        print('one condition is true')



