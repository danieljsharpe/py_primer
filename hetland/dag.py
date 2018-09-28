'''
Python class for constructing a random directed acyclic graph (DAG)
'''

from copy import copy, deepcopy
from collections import deque
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

class Dag(object):

    def __init__(self):
        self.reset_graph()

    def reset_graph(self):
        self.graph = OrderedDict()

    def add_node(self, node_name, graph=None):
        if not graph:
            graph = self.graph
        if node_name in graph:
            raise KeyError("node %s already exists" % node_name)
        graph[node_name] = set()

    def add_edge(self, ind_node, dep_node, graph=None):
        if not graph:
            graph = self.graph
        if ind_node not in graph or dep_node not in graph:
            raise KeyError("Attempting to add edge involving one or more nonexistent nodes")
        graph[ind_node].add(dep_node)

    # returns a list of all predecessors of the given node
    def predecessors(self, node, graph=None):
        if graph is None:
            graph = self.graph
        return [key for key in graph if node in graph[key]]

    # returns a list of all nodes this node has edges towards
    def downstream(self, node, graph=None):
        if graph is None:
            graph = self.graph
        if node not in graph:
            raise KeyError('node %s is not in graph' % node)
        return list(graph[node])

    # returns a list of all nodes ultimately downstream of the given node in the
    # dependency graph, in topological order
    def all_downstreams(self, node, graph=None):
        if graph is None:
            graph = self.graph
        nodes = [node]
        nodes_seen = set()
        i = 0
        while i < len(nodes):
            downstreams = self.downstream(nodes[i], graph)
            for downstream_node in downstreams:
                if downstream_node not in nodes_seen:
                    nodes_seen.add(downstream_node)
                    nodes.append(downstream_node)
            i +=1
        return list(
            filter(
                lambda node: node in nodes_seen,
                self.topological_sort(graph=graph)
            )
        )

    # return a list of all leaves (nodes with no downstreams)
    def all_leaves(self, graph=None):
        if graph is None:
            graph = self.graph
        return [key for key in graph if not graph[key]]

    # returns a list of all nodes in the graph with no dependencies
    def ind_nodes(self, graph=None):
        if graph is None:
            graph = self.graph
        dependent_nodes = set(
            node for dependents in iter(graph.values()) for node in dependents)
        return [node for node in graph.keys() if node not in dependent_nodes]

    # Returns Boolean of whether DAG is valid by attempting a topological sort
    def validate(self, graph=None):
        graph = graph if graph is not None else self.graph
        if len(self.ind_nodes(graph)) == 0:
            return False # no indep. nodes detected
        try:
            self.topological_sort(graph)
        except ValueError:
            return False # failed topological sort
        return True

    # Returns a topological ordering of the DAG. Raises ValueError if this is not possible
    # (in which case, graph is not a valid DAG)
    def topological_sort(self, graph=None):
        if graph is None:
            graph = self.graph

        in_degree = {}
        for u in graph:
            in_degree[u] = 0

        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1

        queue = deque()
        for u in in_degree:
            if in_degree[u] == 0:
                queue.appendleft(u)

        l = []
        while queue:
            u = queue.pop()
            l.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.appendleft(v)

        if len(l) == len(graph):
            return l
        else:
            raise ValueError('graph is not acyclic')
