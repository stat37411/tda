from .simplex import boundary

class Filtration():
    def __init__(self):
        self.spxs = [[]]
        self.vals = [[]]

    def _add_unsafe(self, spx, t):
        """
        add simplex
        """
        spx_dim = len(spx) - 1
        while len(self.spxs) < len(spx):
            self.spxs.append([])
            self.vals.append([])
        self.spxs[spx_dim].append(spx)
        self.vals[spx_dim].append(t)

    def contains(self, spx):
        """
        return True if contains simplex
        """
        spx_dim = len(spx) - 1
        if len(spx) == 0:
            return True
        if len(self.spxs) < len(spx):
            return False
        return (spx in self.spxs[spx_dim])

    def simplices(self, k):
        """
        return simplices in dimension k
        """
        return self.spxs[k]

    def add(self, spx, t):
        if self.contains(spx):
            return
        for face in boundary(spx):
            # recurse on faces
            self.add(face, t)
        self._add_unsafe(spx, t)
