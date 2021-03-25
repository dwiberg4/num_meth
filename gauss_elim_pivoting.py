# Linear Algebraic Systems Methods
# Gauss Elimination with Pivoting (Non-Naive)

# Can now handle if A DOES have a 0 on diagonal
# Because of pivoting, program will not fail.


import numpy as np 

A = np.array([[1,2,3],[4,5,6],[1,8,5]])
b = np.array([[4],[7],[1]])
n = b.size
x = np.zeros((n,1))
print('The A matrix is:\n',A)
print('The b array is:\n',b)
print('The x array is:\n',x)

er = 0
tol = 0.00001

def guass_(a,b,n,x,tol,er):
    s = np.zeros((n,1))
    er = 0
    for i range(n):
        s[i] = abs(A[i][1])
        for j in range(1,n):
            if (abs(A[i][j]) > s[i]):
                s[i] = (abs(A[i][j]))
    (a,b,er) = eliminate(a,)
x = gauss_(A,b,n,x,tol,er)