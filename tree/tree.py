class Tree:
    """Abstract base class representing a tree structure"""

    # ------------------ nested Position class --------------
    class Position:
        """An abstraction representing the location of a single element"""

        def element(self):
            """Return the element stored at this position"""
            raise NotImplementedError("Must be implemented by sub class")

        def __eq__(self, other):
            """Return true if other Position represent the same location"""
            raise NotImplementedError("Must be implemented by sub class")

        def __ne__(self, other):
            """Return true if other does not represent the same location
            """
            return not (self == other)

    # -----abstract method that concrete subclass must support------

    def root(self):
        """Return Position representing the tree's root (or None if empty)
        """
        raise NotImplementedError("Must be implemented by sub class")

    def parent(self, p):
        """Return the Position representing p's parent (or None if p is root)
        """
        raise NotImplementedError("Must be implemented by sub class")

    def num_children(self, p):
        """Return the number of children that Position p has.
        """
        raise NotImplementedError("Must be implemented by sub class")

    def children(self, p):
        """Generate an iteration of Positions representing p's children
        """
        raise NotImplementedError("Must be implemented by sub class")

    def __len__(self):
        """Return the total number of elements in the tree
        """
        raise NotImplementedError("Must be implemented by sub class")

    # ------ concrete methods implemented in this class----------
    def is_root(self, p):
        """Return True if Position p represents the root of the tree
        """
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """Return true if the tree is empty
        """
        return len(self) == 0
