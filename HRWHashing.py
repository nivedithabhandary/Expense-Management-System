#!/usr/bin/python

import bisect
from hashlib import md5

class HRWHashRing(object):
    """Implement a HRW hashing ring."""

    def __init__(self, debug=False):
        """Create a new HRWHashRing.

        :param weight: To assign new weight to every node

        """
        self._numnodes = 0
        self._keys = []
        self._nodes = {}
        self._weight = {}
        self._debug = debug

    def _hashweight(self, key, node):
        val = long(md5(key+node).hexdigest(), 16)
        if(self._debug):
            print 'in _hashweight node: ', node, " val: ", val
        return val & 0xffffffff

    def addweight(self, key):
        nodes = self._nodes.values()
        for node in nodes:
            nodeweight = self._hashweight(key, node)
            self._weight[node] = nodeweight
        if(self._debug):
            print 'in addweight nodeweights:',self._weight


    def addnode(self, nodename, node):
        """Add a node, given its name."""
        self._nodes[nodename] = node
        bisect.insort(self._keys, nodename)
        self._numnodes += self._numnodes
        if(self._debug):
            print 'in addnode nodename:', nodename, " node:", node, " self_keys: ", self._keys, " self_nodes: ", self._nodes

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
        """Return a node with highest weight , given a key."""

        # Calculate weight for each node with key
        self.addweight(key)
        node = 0
        for k, v in self._weight.items():
            if v == max(self._weight.values()):
                node = k
        if(self._debug):
            print 'in getnode key: ', key, ' node: ', node
        return node
'''
if __name__ == '__main__':
    import random
    hrwHashRing = HRWHashRing(False)
    hrwHashRing.addnode("1", "127.0.0.1:5001")
    hrwHashRing.addnode("2", "127.0.0.1:5002")
    hrwHashRing.addnode("3", "127.0.0.1:5003")
    d = {}
    random.seed(99)
    for i in xrange(1, 11):
         v = hrwHashRing.getnode(str(random.randint(1, 10)))
         if v not in d:
             d[v] = 1
         else:
             d[v] += 1
    print d
'''
