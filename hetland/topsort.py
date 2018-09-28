'''
Python script to perform topological sorting of a directed acyclic graph (DAG), or else to identify that the graph provided is not a valid DAG
Topological sorting: given a DAG, the nodes are sorted into a sequence such that, given the order of the nodes, all edges of the graph point forwards
(and thus the dependencies are respected). Note that for a given DAG, there may be more than one valid topologically sorted sequence.
'''

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from copy import deepcopy

# naive topological sorting algorithm
def naive_topsort(G, S=None):
    if S is None: S = deepcopy(G)
    if len(S) == 1: return [S.items()[0][0]] # base case, single node
    v = S.popitem(last=False)[0]
    seq = naive_topsort(G, S) # recursion(assumption), n-1. Seq is a list of nodes in topological order, added to sequentially
    min_i = 0
    for i,u in enumerate(seq):
        if v in G[u]: min_i = i + 1 # node v is dependent on node u, therefore v must place after u
    seq.insert(min_i, v) # fit node v in its correct place
    return seq

# efficient topological sorting algorithm (Kahn algorithm)
'''solve problem reductively by choosing (and removing from the DAG) the node which must come first in the topologically sorted sequence, i.e. that which has
no in-edges (note that another valid reductive solution is the opposite, to choose the node as that which must come last in the topologically sorted sequence
i.e. that which has no out-edges). If we (conceptually) remove all its out edges, then the remaining graph, with n-1 nodes, is a DAG that can be sorted
in the same way. Using this method, we can simply append the growing list, rather than having to perform the wasteful insert operation in the naive algorithm'''

def topsort(G):
    count = dict((u,0) for u in G) # in-degree for each node
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0] # valid initial nodes
    S = [] # the result
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1 # uncount out-edges of node u
            if count[v] == 0: # new valid start nodes in the remaining graph (if any)
                Q.append(v)
    if len(S) != len(G): # graph is not a valid DAG
        S = None
        return S
    return S

'''
0 - b
1 - a
2 - f
3 - e
4 - d
5 - c
Therefore correct order: 1, 0, 5, 4, 3, 2
For this graph, the topological ordered sequence is a unique solution
'''
#Driver code
#Example graph
G = OrderedDict([(0, set([5, 4, 2])), (1, set([0, 2])), (2, set([])), (3, set([2])), (4, set([2, 3])), (5, set([4]))])
#correct order: 1, 0, 5, 4, 3, 2
print G
seq = naive_topsort(G)
print seq
seq = topsort(G)
print seq
