#!/usr/bin/python

import bisect
from hashlib import md5

class ConsistentHashRing(object):
    """Implement a consistent hashing ring."""

    def __init__(self, debug=False):
        """Create a new ConsistentHashRing.

        :param replicas: number of replicas.

        """
        self._numnodes = 0
        self._keys = []
        self._nodes = {}
        self._debug = debug

    def _hash(self, key):
        """Given a string key, return a hash value."""
        val  = long(md5(key).hexdigest(), 16)
        if(self._debug):
            print 'in _hash key: ', key, " val: ", val
        return val

    def addnode(self, nodename, node):
        """Add a node, given its name.

        The given nodename is hashed
        """
        hash_ = self._hash(nodename)
        if hash_ in self._nodes:
            raise ValueError("Node name %r is "
                "already present" % nodename)
        self._nodes[hash_] = node
        bisect.insort(self._keys, hash_)
        self._numnodes += self._numnodes
        if(self._debug):
            print 'in addnode nodename:', nodename, " node:", node, " hash_:", hash_, " self_keys: ", self._keys, " self_nodes: ", self._nodes

    def _delnode(self, nodename):
        """Remove a node, given its name."""
        hash_ = self._hash(nodename)
        if hash_ not in self._nodes:
            raise ValueError("Node name %r is "
                "not present" % nodename)
        del self._nodes[hash_]
        index = bisect.bisect_left(self._keys, hash_)
        del self._keys[index]
        self._numnodes -= self._numnodes

        if(self._debug):
            print 'in delnode nodename:', nodename, " hash_:", hash_, " self_keys: ", self._keys, " self_nodes: ", self._nodes

    def getnode(self, key):
        """Return a node, given a key.

        The node with a hash value nearest
        but not less than that of the given
        name is returned.   If the hash of the
        given name is greater than the greatest
        hash, returns the lowest hashed node.

        """
        hash_ = self._hash(key)
        start = bisect.bisect(self._keys, hash_)
        if start == len(self._keys):
            start = 0

        if(self._debug):
            print 'in getnode key:', key, " hash_:", hash_, " self._nodes[self._keys[start]]: ", self._nodes[self._keys[start]]

        # following line is nothing but self._keys[hash_]
        return self._nodes[self._keys[start]]

'''
if __name__ == '__main__':
    import random
    consistentHashRing = ConsistentHashRing(False)
    consistentHashRing.addnode("1", "127.0.0.1:5001")
    consistentHashRing.addnode("2", "127.0.0.1:5002")
    consistentHashRing.addnode("3", "127.0.0.1:5003")
    d = {}
    for i in xrange(1, int(1e6)):
         v = consistentHashRing.getnode(str(random.randint(1, 1e10)))
         if v not in d:
             d[v] = 1
         d[v] += 1

    print 'hello!'
    print d
'''
