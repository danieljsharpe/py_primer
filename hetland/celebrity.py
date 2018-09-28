'''
Python script to solve the celebrity problem.
In a directed graph, we want to find (if it exists) a node with incoming edges from *all* other nodes, and no* outgoing edges (celebrity in a crowd known by all others).
'''

from random import randrange
import numpy as np

n=100
p = 0.5 # sets T/F selection probability
#G = [[randrange(2) for i in range(n)] for i in range(n)] # crude random graph
G = np.random.choice(a=[False, True], size=(n,n), p=[p,1-p])# Crude Boolean random graph
c = randrange(n) # set celebrity
for i in range(n):
    G[i][c] = True # incoming connection
    G[c][i] = False # no outgoing connection

#Naive algorithm
def naive_celeb(G):
    n = len(G)
    for u in range(n):
        for v in range(u,n):
            if u == v: continue
            if G[u][v]: break
            if not G[v][u]: break
        else:
            return u # no breaks - found celebrity
    return None

#Efficient algorithm
def celeb(G):
    n = len(G)
    u, v = 0, 1 # starting indices
    for c in range(2,n+1):
        if G[u][v]: u = c # u knows v, u cannot be celebrity
        else: v = c # v is unknown by u, v cannot be celebrity
    if u == n: c = v # u was replaced last, use v
    else: c = u # otherwise, u is a candidate
    # at this point we have one candidate which, if present, is the celebrity. Do check
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else:
        return c
    return None

print naive_celeb(G)
print celeb(G)
