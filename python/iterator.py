# to print a list of values one by one we use iterator
# by using index
nums=[1,2,3,4,5]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])
print(nums[4])

# by using for loop

nums=[1,2,3,4,5]
for i in nums:
    print(i)


# by using iterator

nums=[1,2,3,4,5]
it=iter(nums)
print(it.__next__())
print(it.__next__())
print(it.__next__())

# or we can use like below
print(next(it))
print(next(it))


# by using iter() and next() method

class TopTen:
    def __init__(self):
        self.num=1        #variable initialization

    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
values=TopTen()
for i in values:
    print(i)




