
#if some no's are divisible by 5
num=[10,18,25,36,20]
for i in num:
    if i%5==0:
        print(i)


#there is no no that is divisable by 5 we can not get an output
num=[12,18,29,36,28]
for i in num:
    if i%5==0:
        print(i)



#to exceed above problem we use for else loop

num = [12, 18, 29, 36, 28]
for i in num:
    if i % 5 == 0:
        print(i)
else:
    print('not found')


