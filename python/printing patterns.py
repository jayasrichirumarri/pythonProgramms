i=1
while i<=4:
    print('#',end='')
    i+=1
    j=1
    while j<=4:
        print('#',end='')
        j+=1
    print()

i = 1
while i <= 4:
    print('#', end='')
    i += 1
    j = 1
    while j <i-1:
        print('#', end='')
        j += 1
    print()

i = 1
while i <= 4:
    print('#', end='')
    i += 1
    j = 1
    while j <=4-i:
        print('#', end='')
        j += 1
    print()


#using for loop
for i in range(4):
    for j in range(4):
        print('#',end='')
    print()


for i in range(4):
    for j in range(i+1):
        print('#',end='')
    print()


for i in range(4):
    for j in range(4-i):
        print('#',end='')
    print()