from .trie import Trie
from .simplex import boundary

class SimplicialComplex():
    """
    Simplicial complex which uses Trie for storage
    """

    def __init__(self):
        self.trie = Trie()


    def _add_unsafe(self, s):
        """
        add simplex without checking boundaries
        """
        self.trie.add(s)


    def add(self, s):
        """
        add simplex, as well as any missing boundaries
        """
        for f in boundary(s):
            # iterate over faces to make sure they are added
            if not self.trie.contains(f):
                self.add(f)
        self.trie.add(s)


    def simplices(self, k=None):
        """
        return simplices
        k (optional): dimension of simplices

        if k is None, returns all simplices
        otherwise, returns simplices of dimension k
        """
        spxs = self.trie.nodes()
        if k is None:
            return spxs
        else:
            return [s for s in spxs if len(s) == k+1]


    def skeleton(self, k):
        """
        return the k-skeleton as a new simplicial complex
        """
        skel = SimplicialComplex()
        for s in self.simplices():
            if len(s) <= k+1:
                skel._add_unsafe(s)

        return skel
