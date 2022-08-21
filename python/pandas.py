# pandas:pandas is a python library used for working with data sets.it has functions
# for analysing,cleaning exploring,and manipulating data.
import pandas as pd
mydataset={
    'cars':['bmw','volvo','ford'],
    'passings':[3,7,2]

}
#myvar=pd.DataFrame(mydataset)
#print(myvar)

# pandas series: a pandas series is a colunmin a table.
# it is a one dimentional array holding any datatype.
import pandas as pd
a=[1,7,2]
myvar=pd.Series(a)
print(myvar)