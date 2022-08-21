dict={'name':'navin','lapi':'dell','cpu':'i5','ram':16}
print(dict)
print(dict.keys())
print(dict.values())
#getting the value by using index
print(dict['name'])
#getting the value by using get() method
print(dict.get('cpu'))
#deleting the value
dict.pop('ram')
print(dict)
#to know the type of a dictionary
print(type(dict))
#we can add different datatypes
dict1={
    'name':'jayasri',
    'roll_no':21,
    'age':25,
    'brand':'dell',
    'ram':16,
    'chargable':True,
    'colors':['red','green','blue']
}
print(dict1)
x=dict1.items()
print(x)
#updating dictionary
dict1['ram']=24
print(dict1)
#we use another function update()
dict1.update({'cpu':'i5'})
print(dict1)
#to empty dictionary we use clear
dict.clear(dict)
print(dict)