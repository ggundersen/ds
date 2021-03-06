#!/usr/bin/env python

"""----------------------------------------------------------------------------
hashtable.py

A hash table is a data structure that implements an associative array, mapping
keys to values. A hash function efficiently generates indices from the keys
added to the hash table. When a hash function produces the same index from two
distinct keys, the event is called a "collision."

Hashing is a good example of a space-time tradeoff. With infinite space, we
could use each key as an index in a large array. This is prohibitive since the
number of possible keys is large. With infinite time, we could not worry about
collisions, hashing to the same index and sequentially searching.

Hashtable uses separate chaining with lists to resolve collisions.
----------------------------------------------------------------------------"""

from collections import namedtuple


Pair = namedtuple('Pair', ['key', 'val'])


class Hashtable:

    def __init__(self):
        """Initialize empty hashtable."""
        self.N = 0
        self.a = [[]]

    def _size(self):
        """Return number of key-value pairs in the hash table for testing."""
        return self.N
        
    def _hash(self, val, mod):
        """Return hash code after ensuring it is positive and within range."""
        return abs(hash(val)) % mod

    def _resize(self, lim):
        """Resize internal array. Return void."""
        temp = [[] for _ in range(lim)]
        for chain in self.a:
            for pair in chain:
                self._put(temp, pair.key, pair.val, lim, True)
        self.a = temp

    def _put(self, lst, key, val, mod, is_copy):
        """Add key to lst argument. Return void."""
        idx = self._hash(key, mod)
        chain = lst[idx]
        if len(chain) == 0:
            chain.append(Pair(key, val))
            if not is_copy:
                self.N += 1
        else:
            not_added = True
            for i, pair in enumerate(chain):
                if pair.key == key:
                    not_added = False
                    chain[i] = Pair(key, val)  # Overwrite previous value
                    break
            if not_added:
                chain.append(Pair(key, val))
                if not is_copy:
                    self.N += 1

    def put(self, key, val):
        """Check key type and list size and then delegate to private put().
        Return void."""
        if type(key) is not int and type(key) is not str:
            raise TypeError('Keys must be integers or strings.')
        if len(self.a) == self.N:
            self._resize(2 * self.N)
        self._put(self.a, key, val, len(self.a), False)

    def get(self, key):
        """Return value stored at the index of hashed key."""
        chain = self.a[self._hash(key, len(self.a))]
        for pair in chain:
            if pair.key == key:
                return pair.val
        return None
