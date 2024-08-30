from math import *

userIn = int(input("Enter a number"))

for x in range (1, (userIn+1)):
    if (userIn%x) == 0:
        print (x)



        '''
        factorList = [] //this is a list or an array
        x= int(input("Enter a number: "))
        for x in range (1, (userIn+1)):
            if (userIn%x) == 0:
                factorList.append(a)
        print("The factors of ", x, " are: ", factorList)
        '''
