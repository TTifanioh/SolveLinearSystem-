import numpy as np
def decomposition_qr(A):
    n, m = A.shape
    Q = np.zeros((n, m))
    R = np.zeros((m, m))

    for j in range(m):
        v = A[:,j].astype(float) # Current vector column
        for i in range(j):
            R[i,j] = np.dot(Q[:,i],A[:,j])
            v = v - R[i,j]*Q[:,i]

        R[j][j] = np.linalg.norm(v)
        if R[j,j] == 0:
            # Case of a non-inversible matrix
            Q[:,j]=v
        else:
            Q[:,j] = v / R[j,j]
    return Q,R