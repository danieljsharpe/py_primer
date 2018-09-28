import random
from dag import Dag

#Create a random graph
n_nodes = 10
n_edges = 20
randseed = 18
graph_is_dag = True

dag1 = Dag()
random.seed(randseed)

for i in range(n_nodes):
    dag1.add_node(i)
for i in range(n_edges):
    node1 = random.randint(0,n_nodes-1)
    node2 = random.randint(0,n_nodes-1)
    dag1.add_edge(node1, node2)
if graph_is_dag:
    while not dag1.validate():
        node1 = random.randint(0,n_nodes-1)
        node2 = random.randint(0,n_nodes-1)
        dag1.add_edge(node1, node2)
        # remove an edge between two nodes that are known to be connected
        print dag1.graph
print dag1.graph
