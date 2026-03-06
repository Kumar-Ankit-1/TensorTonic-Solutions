import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    rows = len(A)
    cols = len(A[0]) if rows > 0 else 0
    new_arr = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(len(A)):
        for j in range(len(A[i])):
            new_arr[j][i]=(A[i][j])
    return np.array(new_arr)