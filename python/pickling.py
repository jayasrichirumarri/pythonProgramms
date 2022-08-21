# to do pickling and unpickling we use  the module pickle.
# it provides a powerful algorithm for serialization and de-serialization of python object structure.
# pickling is the process where the python object structure is converted into byte stream and
# unpickling is the process where the byte stream is converted back into python object.
# if we convert python object (like dictionaries ,list) into byte stream is called pickling.
# if we convert that byte stream into python object is called unpickling.
# there are also known as serialization and de-serialization .

# pickling
import pickle
mylist=['hello','python']
f=open('pickle.txt','wb')
pickle.dump(mylist,f)
f.close()

# unpickling
f1=open('pickle.txt','rb')
result=pickle.load(f1)
print(result)

