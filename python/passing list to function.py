def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
lst = [20,25,30,35,40,45,50,55,60,69]
even, odd = count(lst)
print('even: {} and odd: {}'.format(even,odd))