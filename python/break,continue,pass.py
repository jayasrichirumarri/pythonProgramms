# break: if we want to jump out of the block we use break
# the remaining stmts also not printed

for i in range(5):
    if i==3:
        break
    print('hello',i)


# continue: it will skip the further exicution only.it will not jump out of the block
# it skip remaining stmts only


for i in range(5):
    if i == 3:          # here if i becomes 3 in that case that stmt can not be exicuted
                        # but the loop is continued remaining 4 and 5 can be exicuted
        continue
    print('hi', i)


# pass: if there is no code in a block we get an error.to overcome that problem we use pass
# some cases we dont know wt can we write in a block so we simply say pass


#for i in range(5):
 #   if i == 3:     # hwre we get an error

# instead of placing an empty block we say pass

for i in range(5):
    if i == 3:
       pass


# break:

av=5
x=int(input('enter how many candies you want:'))
i=1
while i<=x:
    if i>av:
        print('out of stock')
        break
    print('candy')
    i+=1
print('bye')


# continue:

for i in range(1,101):
    if i%3==0:
        continue
    print(i)
print('bye')


# pass:

def func():
    pass