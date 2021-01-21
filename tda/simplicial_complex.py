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
            if not t.contains(f):
                self.add(f)
        self.trie.add(s)


    def simplices(self):
        """
        return all simplices
        """
        return self.trie.nodes()


    def skeleton(self, k):
        """
        return the k-skeleton as a new simplicial complex
        """
        skel = SimplicialComplex()
        for s in self.simplices():
            if len(s) <= k+1:
                skel._add_unsafe(s)

        return skel
