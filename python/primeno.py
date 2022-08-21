
num=7

for i in range(2,num):
    if num%i==0:
        print('not prime')
    else:
        print('prime')

# by using for each loop we get the proper output
nums=7

for i in range(2,nums):
    if nums%i==0:
        print('not prime')


else:
    print('prime')

# printall the prime nos in an given interval
lower = 1
upper = 100
print("prime no's between", lower, "and", upper, "are:" )
for j in range(lower, upper+1):
    if j>1:
        for i in range(2, j):
            if (j % i) == 0:
                break
        else:
            print(j)


# using while loop
num = int(input('please enter a number:'))
i = 2
flag = 0
while i<num:
    if num%i == 0:
        flag = 1
        print(num,'is NOT A prime number!')
    i=i+1
if flag == 0:
            print(num,'is a prime number!')