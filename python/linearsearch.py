# in linear search there is no sorting of vlaues

pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False

list=[5,8,4,6,9,2]
n=4
if search(list,n):
    print('found at:',pos+1)
else:
    print('not found')

# there is a problem with linear search
# if the list size is increases the searching process also increases