# Linear Algebraic Systems Methods
# Naive Gauss Elimination


# ****Naive because we're assuming that A never has 0 on the diagonal****
# If A does have a 0 on diagonal: Division by 0: WILL FAIL

import numpy as np 

A = np.array([[1,2,3],[4,5,6],[1,8,5]])
b = np.array([[4],[7],[1]])
x = np.array([[0.0],[0.0],[0.0]])
print('The A matrix is:\n',A)
print('The b array is:\n',b)


# Forward Elimination
for k in range(b.size-1):               # row number to be subtracted
    for i in range((k+1),b.size):       # row number to subtract k from 
        factor = (A[i][k])/(A[k][k])
        for j in range(b.size):         # column number to be added/sub-ed from
            A[i][j] = A[i][j] - (factor*(A[k][j]))
        b[i] = b[i] - (factor*(b[k]))   # subtraction on RHS of sys.
print('A matrix is now: \n',A)
print('b vector is now: \n',b)


# Back Substitution
for i in range((b.size-1),-1,-1):       # (start,stop,step)
    sum = float(b[i])
    #print('i and j are: ',i,j,'right here',sum)
    for j in range((i+1),b.size):
        sum -= (float(A[i][j])*float(x[j]))
        #print('i and j are: ',i,j,'sum is now: ',sum)
    #print('A_ii is: ',A[i][i])
    inter = sum/float(A[i][i])
    #print('inter is: ',inter)
    x[i] = inter #sum/float(A[i][i])
    #print('x is right now: \n',x)

print('x vector answer is now: \n',x)
