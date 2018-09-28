'''
Python script to find maximum permutation of a bipartite graph (the nodes are partitioned between sets, where all edges are between sets
and no edges exist between members of the same set -example of a 'matching problem').
Consider the mapping of the set {a, b, c...} to itself, each member of the set having an associated preference (weight) for the member of the
second set that it is 'pointing' to. We are looking for the subset of members for the given mapping that:
    1. is a one-to-one mapping (permutation) (each member of the second set is pointed to once and only once, and all members of the second set are pointed to)
    2. is the maximum permutation (maximises the satisfied preference weight)
Let us consider the case that all preference weights for each member of the first set are equal.
We remove members of the set that are *not* pointed to in an iterative or recursive fashion. If no such member exists, then there must already be a one-to-one mapping
of maximum subset size (members of this subset can permute freely, and thus each have their preferences satisfied). The removed members cannot
permute and therefore must map onto themselves (they cannot be permuted consistently with the max permutation group).
'''

M = [2, 2, 0, 5, 3, 5, 7, 4] #mapping preferences

#Naive recursive algorithm for finding a max permutation
def naive_max_perm(M, A=None):
    if A is None: A = set(range(len(M))) # initialise A = {0,1,...,n-1}
    if len(A) == 1: return A # base case - single elem in A
    B = set(M[i] for i in A) # the 'pointed to' elems
    C = A - B # the 'not pointed to' elems
    if C:
        A.remove(C.pop()) # remove elem not pointed to
        return naive_max_perm(M, A) # solve remaining problem recursively
    return A

A = naive_max_perm(M) # set containing members that may permute freely (and thus satisfy their preferences)
print A
newM = [ i for i in range(len(M))] # initialise final mappings consistent with max permutation group
while A:
    i = A.pop() 
    newM[i] = M[i] # members of A may have their preference satisfied
print newM

'''The repeated creation of the set B is a wasteful operation. Instead, we want to use reference counting to keep track of which members are no longer pointed to. We
could decrement the count for member x when the member pointing to x is eliminated, and if x reaches zero, the member x is eliminated from both sets.'''

#Efficient iterative algorithm for finding a max permutation

def max_perm(M):
    n = len(M) # no. of elems
    A = set(range(len(M))) # initialise A = {0,1,...,n-1}
    count = [0]*n # no. of times that each member of the second set is pointed to
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0] # members not pointed to
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0: # j no longer pointed to, add to list to be dealt with
            Q.append(j)
    return A

A = max_perm(M)
print A

'''
Now let us consider the case where preference weights are not equal. In this case, we do not necessarily want the permutation group with the largest number of members. Instead,
we want to ensure that we satisfy the members of the set that have the strongest preferences. For members of the set that are pointed to more than once, we choose that which has a
higher preference (greedy strategy) and try and build a permutable subgroup starting from it, by following connections until the original chosen node is found (this cycle is for
a one-to-one mapping subgroup. There may be other, independent subgroups. If the attempt is unsuccessful, we choose the pointing member with
next highest preference weight, and so on. After all attempts on nodes to which multiple members point have been attempted, we have (hopefully) found a one-to-one mapping
with maximum preference weights.
'''

Mw = {0: (2, 7), 1: (2, 3), 2: (0, 1), 3: (5, 10), 4: (3, 2), 5: (5, 1), 6: (7, 3), 7: (4, 12)}
# preference mapping with weights. Format is... member: (preferred member, preference weight)
print "weighted map", Mw

# Algorithm for finding a permutation with max preference weights

def weighted_max_perm(Mw):
    A = set(range(len(M))) # initialise A = {0,1,...,n-1}
    count = [0]*len(M) # no. of times each member is pointed to
    pointers = {i: [[], []] for i in range(len(M))} # list of pointers (and list of associated weights) to a given member
    for key, item in Mw.items():
        count[Mw[key][0]] += 1
        pointers[Mw[key][0]][0].append(key)
        pointers[Mw[key][0]][1].append(Mw[key][1])
#        pointers[Mw[key][0]].append(item)
    Q = [i for i in A if count[i] > 1] # members pointed to more than once
    print "pointers", pointers
    B = set()
    # find member pointing to disputed member that has lowest preference weight and delete
    while Q:
        print "Q", Q
        i = Q.pop()
        maxweight = max(pointers[i][1])
        j = pointers[i][1].index(maxweight)
        k = pointers[i][0][j]
        print "found node k with largest weight", k
        print "Trying to build max perm group including k"
        B.add(k)
        #CODE TO VERIFY IF A PERM GROUP CAN BE DERIVED STARTING FROM NODE k#
    return A

A = weighted_max_perm(Mw)
print A
