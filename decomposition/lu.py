import numpy as np
def decomposition_lu(A): # A is square matrix
    n = len(A)
    # Init : L with 1 in diagonal, U with 0
    L = np.eye(n) 
    U = np.zeros((n,n))
    for i in range(n):
        # Calculation  rows i of U
        for k in range(i,n):
            s1 = sum(L[i][j]*U[j][k] for j in range(i))
            U[i][k] = A[i][k] - s1
        
        # Calculation L
        for k in range(i+1, n):
            s2 = sum(L[k][j]*U[j][i] for j in range(i))
            if U[i][i] == 0:
                raise ValueError("Zero pivot encountered")
            L[k][i] = (A[k][i] - s2)/U[i][i]
    return L,U