'''
Python script to create a randomised directed acyclic graph (DAG) that is guaranteed to be topologically sorted
'''

from dag import Dag
from random import randrange
import numpy as np


#Construct a random DAG
n = 10 # no. of nodes
p = 0.2 # probability of adding an edge
m = 50 # max. no. of edge-adding attempts
dag1 = Dag()
for i in range(n):
    dag1.add_node(i)
for i in range(m):
    addedge = np.random.choice(a=[True, False], p=[p,1-p])
    if addedge:
        j = randrange(0,n-2)
        k = j
        while k <= j: 
            k = randrange(0,n-1)
        dag1.add_edge(j,k)
    else:
        continue
#if there are any independent nodes (other than the first), add a dependency
while dag1.ind_nodes() != [0]:
    i = dag1.ind_nodes()[-1]
    if i != 1: dag1.add_edge(randrange(0,i-1),i)
    elif i == 1: dag1.add_edge(0,i)

print dag1.graph
