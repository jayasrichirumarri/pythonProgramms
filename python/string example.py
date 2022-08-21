# finding length of the string
str='hello world'
print(len(str))

#another way
def len(str):
    counter=0
    for i in str:
        counter+=1
    return counter
str='hello world'
print(len(str))

str='this is python language'
s=str.split()
print(s)