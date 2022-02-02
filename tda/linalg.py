from functools import reduce

class f2vector():
    """
    class to hold a vector over F2
    represented by non-zero indices
    """
    def __init__(self, nzinds=[]):
        self.nzinds = sorted(nzinds)

    def pivot(self):
        """
        index of last nonzero entry

        returns -1 if no nonzeros
        """
        if len(self.nzinds) > 0:
            return self.nzinds[-1]
        else:
            return -1

    def nnz(self):
        """
        number of nonzeros in vector
        """
        return len(self.nzinds)

    def __add__(self, other):
        """
        add two vectors
        """
        # trivial cases
        if other.nnz() == 0:
            return self
        if self.nnz() == 0:
            return other

        newnz = []

        i = 0
        j = 0
        while i < self.nnz() and j < other.nnz():
            if self.nzinds[i] < other.nzinds[j]:
                newnz.append(self.nzinds[i])
                i += 1
            elif self.nzinds[i] > other.nzinds[j]:
                newnz.append(other.nzinds[j])
                j += 1
            else:
                i += 1
                j += 1

        while i < self.nnz():
            newnz.append(self.nzinds[i])
            i += 1

        while j < other.nnz():
            newnz.append(other.nzinds[j])
            j += 1

        return f2vector(newnz)

    def __str__(self):
        return "f2vector: " + str(self.nzinds)

    def __getitem__(self, i):
        if i in self.nzinds:
            return 1
        else:
            return 0




class f2matrix():
    """
    list of list matrix
    """
    def __init__(self, m=0, n=0, cols=None):
        self.m = m
        self.n = n
        if cols is None:
            self.cols = [f2vector() for _ in range(n)]
        else:
            self.cols = cols

    def print(self):
        print("{} x {} f2matrix:".format(self.m, self.n))
        for i in range(self.m):
            for j in range(self.n):
                print(self.cols[j][i], end=' ')
            print()

    def __getitem__(self, args):
        if isinstance(args, int):
            j = args
            return self.cols[j]
        elif len(args) == 2:
            i, j = args
            return self.cols[j][i]
        else:
            raise AssertionError("Can use more than 2 indices!")

    def __setitem__(self, j, data):
        if not isinstance(j, int):
            raise AssertionError("Only supports column assignment!")
        else:
            self.cols[j] = data

    def __mul__(self, other):
        """
        product of 2 f2matrices
        """
        if self.n != other.m:
            raise AssertionError("incompatible dimensions!")
        pass

    def nnz(self):
        """
        number of non-zeros
        """
        return reduce(lambda x, y: x+y, [c.nnz() for c in self.cols])


    def is_zero(self):
        return self.nnz() == 0


    def pivots(self):
        """
        return set of pivots
        """
        pivs = set()
        for c in self.cols:
            if c.pivot() != -1:
                pivs.add(c.pivot())

        return pivs
