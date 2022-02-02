from .linalg import f2vector, f2matrix

def reduce(B):
    """
    performs reduction algorithm on matrix B
    """
    p2c = dict() # pivot to column map
    for j in range(B.n):
        while(B[j].nnz() > 0):
            piv = B[j].pivot()
            j2 = p2c.get(piv, -1)
            if j2 == -1:
                p2c[piv] = j
                break
            else:
                B[j] = B[j] + B[j2]
    return B
