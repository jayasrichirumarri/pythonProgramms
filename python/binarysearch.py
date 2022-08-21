# in binary search all the values are sorted
# if search value is smaller then change upper bound
# if search value is bigger then change lower bound and mid becomes new lower bound

pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:          # l=lower bound,u=upper bound
        mid=(l+u)//2     # integer division
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:

           if list[mid]<n:
                l=mid
           else:
               u=mid

list=[23,54,6,5,7,5,7557,3,76,8,5776,36,54]

n=36
if search(list,n):
    print('found at',pos+1)
else:
    print('not found')
