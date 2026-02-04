import numpy as np
def decomposition_cholesky(A):
    n = len(A)
    L = np.zeros((n,n)) # Init L matrix

    for i in range (n):
        for j in range(i+1):
            s = sum(L[i][k]*L[j][k] for k in range(j))

            if i == j: # Diagonal element
                val = A[i][i] - s
                if val <= 0:
                    raise ValueError("Error, the matrix is not defined positive.")
                L[i][j] = np.sqrt(val)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - s))
    return L