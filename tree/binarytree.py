#!/usr/bin/env python

"""----------------------------------------------------------------------------
binarytree.py

A binary tree is a tree, the abstract data type, with a invariant that each
node has at most two child nodes. The root node is the only node in a tree
without a parent.
----------------------------------------------------------------------------"""


class Binarytree:


    class Node:
        """Inner class to represent nodes in tree."""
        
        
        def __init__(self, left=None, right=None):
            self.root = None
            self.val = val
            self.left = left
            self.right = right
            self.N


    def __init__(self):
        """Initialize empty binary tree."""
        pass


    def size(self):
        """Return size based on node's N property."""
        if self.root == None:
            return 0
        return self.root.N


    def get(self, key):
        """Get value based on key."""
        pass


    def _put(self, key, val):
        """Add key-value pair. Recursively return each subtree's root."""
        pass


    def put(self, key, val):
        """Recursively delegate to private _put(). Return void."""
        self.root = _put(key, val)
        
