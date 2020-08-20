import numpy as np

mylist = [[1,2,3],[4,5,6]]
myarray = np.array(mylist)
#by that i converted the list to array ==> 2D array

print(("Matrix : %s") % str(myarray))
# or we can use ==> print("Matrix : {0}".format(myarray))

print(("Matrix dimension is : %s") % str(myarray.shape))
#as we know -shape- give us the matrix 's dimentions

print(("First row : %s") % str(myarray[0]))

print(("Last row : %s") % str(myarray[-1]))

print(("First row last column : %s") % str(myarray[0,2]))

print(("Third column : %s") % str(myarray[:,2]))