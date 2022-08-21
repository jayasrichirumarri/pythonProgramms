# printing the ASCII value of a character

ch= input('enter a charcter:')
print('the ASCII value of  ',ch ,'is',ord(ch))

# sum of squares of first n natural nos
def sqsum(n):
    sm=0
    for i in range(1,n+1):
        sm=sm+(i*i)
    return sm

n=4
print(sqsum(n))

# sum of cubes of first n natural nos
def cubesum(n):
    sm=0
    for i in range (1,n+1):
        sm=sm+(i*i*i)
    return sm

print(cubesum(5))

