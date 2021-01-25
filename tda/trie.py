class Trie():
    """
    Trie class for lists/tuples, or any ordered data type (can slice)
    """

    def __init__(self):
        self.children = dict()

    def __setitem__(self, key, val):
        """
        can store data at a node on the trie
        """
        if len(key) == 0:
            self.data = val
        else:
            if not key[0] in self.children:
                self.children[key[0]] = Trie()

            self.children[key[0]][key[1:]] = val

    def __getitem__(self, key):
        """
        retrieve data from a node on the trie
        """
        if len(key) == 0:
            return self.data
        else:
            return self.children[key[0]][key[1:]]

    def contains(self, key):
        """
        check if trie contains node for this word
        """
        if len(key) == 0:
            return True
        elif key[0] in self.children:
            return self.children[key[0]].contains(key[1:])
        else:
            return False

    def add(self, key):
        """
        add a key to the trie
        """
        if len(key) > 0:
            if not key[0] in self.children:
                self.children[key[0]] = Trie()

            self.children[key[0]].add(key[1:])

    def nodes(self):
        """
        return a list of nodes
        this is done using a depth-first iteration over the trie
        """
        w = []
        for c in self.children.keys():
            w.append((c,))
            for wc in self.children[c].nodes():
                w.append((c,) + wc)

        return w
