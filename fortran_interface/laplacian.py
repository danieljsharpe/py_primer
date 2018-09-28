'''
Python script acting as wrapper for calculating Laplacian (nabla^2) on a grid with Fortran
'''

import laplacian
import numpy as np

print laplacian.__doc__ # print subroutines, functions, modules with the file with modulefilename 'laplacian'
print laplacian.laplacian.laplac.__doc__ # syntax: modulefilename.modulenameinfile.subroutinenameinfile
# Note that if the module file did not contain the statement: "module laplacian", then the syntax would be more concise:
# modulefilename.subroutinenameinfile
#This second print statement contains the info on the subroutine laplac
#The first line indicates that the subroutine laplac is called from python by: out = laplac(mandatory args...,[optional args])
#The next lines print out info (dimensions, etc.) of mandatory args (here, first arg. with intent=in)
#The following lines print out info of optional args
#The final lines print out info on the variable that is returned by the Fortran subroutine. Note that this variable is listed
#as an argument to the Fortran subroutine, but is declared with intent=out. Note that this variable is not listed as an arg
#when calling from python

m = 5
n = 5

grid = np.asfortranarray(np.random.random([m, n]))
#Numpy arrays are not Fortran-contiguous by default (i.e. cannot be passed to Fortran); we must use this syntax
#Note that a python list of lists (e.g. [[float(j**2 + k**2) for j in range(0,3) for k in range(0,4)]) IS Fortran-contiguous
#Alternatively we could use the syntax:
# grid = np.array(x, order='Fortran')
# then using "grid.flags" shows us that the array has the property F_CONTIGUOUS : True

print grid
print type(grid)
print np.isfortran(grid) # boolean - check that array 'grid' is valid for use with Fortran

lap = laplacian.laplacian.laplac(grid, m, n)

print lap
print type(lap)
#Note Fortran always gives back a numpy array


#Note: executing with "time python laplacian.py" shows that the program runs damn fast!
