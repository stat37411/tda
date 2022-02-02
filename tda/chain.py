import numpy as np
from .linalg import f2vector, f2matrix
from .simplex import boundary
from .simplicial_complex import SimplicialComplex
from .filtration import Filtration
from .reduction import reduce

class f2chain_complex():
    def __init__(self, bdry=[]):
        self.bdry = bdry
        #self.check_boundary()

    def __getitem__(self, i):
        return self.bdry[i]

    def __setitem__(self, i, data):
        while len(self.bdry) < i+1:
            self.bdry.append(f2matrix())
        self.bdry[i] = data

    def maxdim(self):
        return len(self.bdry) - 1

    def reduce(self):
        """
        Perform reduction algorithm on each boundary matrix in chain complex
        """
        for B in self.bdry:
            reduce(B)


    def hdim(self, k):
        """
        calculate homology in dimension k
        """
        self.reduce()
        # find zero columns which are not pivots one dimension up
        ct = 0
        if k < self.maxdim():
            Bk = self.bdry[k]
            Bk1_pivs = self.bdry[k+1].pivots()

            for j in range(Bk.n):
                if Bk[j].nnz() == 0:
                    if j not in Bk1_pivs:
                        ct += 1
        else:
            Bk = self.bdry[k]
            for j in range(Bk.n):
                if Bk[j].nnz() == 0:
                    ct += 1

        return ct

    def check_boundary(self):
        for i in range(len(self.bdry)-1):
            if not (self.bdry[i]*self.bdry[i+1]).is_zero():
                raise AssertionError("composition of boundary maps must be zero")


class filtered_f2chain_complex(f2chain_complex):
    def __init__(self, bdry=[], vals=[]):
        self.bdry = bdry
        self.vals = vals
        #self.check_boundary()

    def __getitem__(self, i):
        return self.bdry[i], self.vals[i]

    def __setitem__(self, i, data):
        while len(self.bdry) < i+1:
            self.bdry.append(f2matrix())
            self.vals.append([])
        self.bdry[i] = data[0]
        self.vals[i] = data[1]

    # def maxdim(self):
    #     return len(self.bdry) - 1
    #
    # def reduce(self):
    #     """
    #     Perform reduction algorithm on each boundary matrix in chain complex
    #     """
    #     for B in self.bdry:
    #         reduce(B)


    def barcode(self, k):
        """
        calculate homology in dimension k
        """
        self.reduce()
        # find zero columns which are not pivots one dimension up
        bars = []
        if k < self.maxdim():
            Bk = self.bdry[k]
            Bk1 = self.bdry[k+1]

            for j in range(Bk.n):
                if Bk[j].nnz() == 0:
                    found_death = False
                    for j2 in range(Bk1.n):
                        if Bk1[j2].pivot() == j:
                            bars.append([self.vals[k][j], self.vals[k+1][j2]])
                            found_death = True
                            break
                    if not found_death:
                        bars.append([self.vals[k][j], np.inf])

        elif k == self.maxdim():
            Bk = self.bdry[k]
            for j in range(Bk.n):
                if Bk[j].nnz() == 0:
                    bars.append([self.vals[k][j], np.inf])

        return bars







def f2_boundary_vec(spx, Xk1):
    """
    compute the boundary of a simplex

    inputs:
        spx: k-simplex
        Xk1: list of k-1 simplices
    """
    inds = []
    for f in boundary(spx):
        for i, s in enumerate(Xk1):
            if s == f:
                inds.append(i)

    return f2vector(sorted(inds))


def f2_boundary(X, k):
    """
    k-dimensional boundary matrix of simplicial complex X
    """
    if k == 0:
        n = len(X.simplices(k))
        return f2matrix(0, n)
    else:
        Xk1 = X.simplices(k-1)
        Xk = X.simplices(k)
        m = len(Xk1)
        n = len(Xk)
        cols = []
        for s in Xk:
            cols.append(f2_boundary_vec(s, Xk1))
        return f2matrix(m, n, cols)

def f2chain_functor(X, k):
    """
    obtain a chain complex from a simplicial complex X up to dimension k
    """
    if isinstance(X, Filtration):
        C = filtered_f2chain_complex()
        for i in range(k+1):
            C[i] = f2_boundary(X, i), X.vals[i]
        return C

    elif isinstance(X, SimplicialComplex):
        C = f2chain_complex()
        for i in range(k+1):
            C[i] = f2_boundary(X, i)
        return C

    else:
        raise RuntimeError("Only supports Filtrations or SimplicialComplexes")
