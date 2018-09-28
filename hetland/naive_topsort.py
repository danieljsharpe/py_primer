'''
Python script for naive topological sorting using adjacency list representation
'''

def naive_topsort(G, S=None):
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i = i+1
    seq.insert(min_i, v)
    return seq

#Adjacency list representation
G = {0: [5,4,2], 1: [0,2], 2: [], 3: [2], 4: [2,3], 5: [4]}
print G

#Note that if using pop() on a list, the argument to pop()
#if using pop() on a set, then pop() takes no arguments
l = [0, 1, 2, 3, 4, 5]
x = l.pop(0)

seq = naive_topsort(G)
print seq
