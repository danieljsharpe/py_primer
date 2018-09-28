'''
Python scripts for walking through connected component of a graph and for finding connected components
'''


# Components function wraps the walk function in a loop over nodes, in order to find (and traverse) all connected components of the graph
def components(G):
    comp = []
    seen = set() # nodes already visited
    for u in G: # all possible starting points
        if u in seen: continue
        C = walk(G, u) # traverse component
        seen.update(C) # add keys of C to seen
        comp.append(C) # collect the components
    return comp

# Walk function traverses a single connected component of a graph and returns a predecessor map (traversal tree) for the nodes it has visited
def walk(G, s, S=set()):
    P, Q = dict(), set() # P keeps track of predecessor nodes (visited), Q is a "to-do" queue
    P[s] = None # start node has no predecessor
    Q.add(s) # we plan on starting with node s
    while Q: # still nodes to visit
        u = Q.pop() # pick one, arbitrarily (affects behaviour of walk, but entire connected component will be explored regardless)
        for v in G[u].difference(P,S):
            Q.add(v)
            P[v] = u
    return P


#Graph representing the bridges of Konigsberg
G = {0: set([1,2,3]), 1: set([3]), 2: set([3]), 3: set([])}
#G = {0: set([1,2,3]), 1: set([0,3]), 2: set([0,3]), 3: set([1,2,3])}
print G

P = walk(G,2)
print P

tree = components(G)
print tree
