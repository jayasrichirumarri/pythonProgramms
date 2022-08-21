# writing one file data in another file

f=open('anotherfile','r')



f1 = open('file','w')
for i in f:
    f1.write(i)

f1 = open('file','r')
