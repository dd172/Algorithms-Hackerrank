class graph(object):
    """
    Graph class - made of nodes and edges

    methods: add_edge, add_edges, add_node, add_nodes, has_node,
    has_edge, nodes, edges, neighbors, del_node, del_edge, node_order,
    set_edge_weight, get_edge_weight
    """

    DEFAULT_WEIGHT = 1
    DIRECTED = False

    def __init__(self):
        self.node_neighbors = {}

    def __str__(self):
        return "Undirected Graph \nNodes: %s \nEdges: %s" % (self.nodes(), self.edges())

    def add_nodes(self, nodes):
        """
        Takes a list of nodes as input and adds these to a graph
        """
        for node in nodes:
            self.add_node(node)

    def add_node(self, node):
        """
        Adds a node to the graph
        """
        if node not in self.node_neighbors:
            self.node_neighbors[node] = {}
        else:
            raise Exception("Node %s is already in graph" % node)

    def has_node(self, node):
        """
        Returns boolean to indicate whether a node exists in the graph
        """
        return node in self.node_neighbors

    def add_edge(self, edge, wt=DEFAULT_WEIGHT, label=""):
        """
        Add an edge to the graph connecting two nodes.
        An edge, here, is a pair of node like C(m, n) or a tuple
        """
        u, v = edge
        if (v not in self.node_neighbors[u] and u not in self.node_neighbors[v]):
            self.node_neighbors[u][v] = wt
            if (u!=v):
                self.node_neighbors[v][u] = wt
        else:
            raise Exception("Edge (%s, %s) already added in the graph" % (u, v))

    def add_edges(self, edges):
        """ Adds multiple edges in one go. Edges, here, is a list of
        tuples"""
        for edge in edges:
            self.add_edge(edge)

    def nodes(self):
        """
        Returns a list of nodes in the graph
        """
        return self.node_neighbors.keys()

    def has_edge(self, edge):
        """
        Returns a boolean to indicate whether an edge exists in the
        graph. An edge, here, is a pair of node like C(m, n) or a tuple
        """
        u, v = edge
        return v in self.node_neighbors.get(u, [])

    def neighbors(self, node):
        """
        Returns a list of neighbors for a node
        """
        if not self.has_node(node):
            raise "Node %s not in graph" % node
        return self.node_neighbors[node].keys()

    def del_node(self, node):
        """
        Deletes a node from a graph
        """
        for each in list(self.neighbors(node)):
            if (each != node):
                self.del_edge((each, node))
        del(self.node_neighbors[node])

    def del_edge(self, edge):
        """
        Deletes an edge from a graph. An edge, here, is a pair like
        C(m,n) or a tuple
        """
        u, v = edge
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        del self.node_neighbors[u][v]
        if (u!=v):
            del self.node_neighbors[v][u]

    def node_order(self, node):
        """
        Return the order or degree of a node
        """
        return len(self.neighbors(node))


    def edges(self):
        """
        Returns a list of edges in the graph
        """
        edge_list = []
        for node in self.nodes():
            edges = [(node, each) for each in self.neighbors(node)]
            edge_list.extend(edges)
        return edge_list

    # Methods for setting properties on nodes and edges
    def set_edge_weight(self, edge, wt):
        """Set the weight of the edge """
        u, v = edge
        if not self.has_edge(edge):
            raise Exception("Edge (%s, %s) not an existing edge" % (u, v))
        self.node_neighbors[u][v] = wt
        if u != v:
            self.node_neighbors[v][u] = wt

    def get_edge_weight(self, edge):
        """Returns the weight of an edge """
        u, v = edge
        if not self.has_edge((u, v)):
            raise Exception("%s not an existing edge" % edge)
        return self.node_neighbors[u].get(v, self.DEFAULT_WEIGHT)

    def get_edge_weights(self):
        """ Returns a list of all edges with their weights """
        edge_list = []
        unique_list = {}
        for u in self.nodes():
            for v in self.neighbors(u):
                if u not in unique_list.get(v, set()):
                    edge_list.append((self.node_neighbors[u][v], (u, v)))
                    unique_list.setdefault(u, set()).add(v)
        return edge_list

def solution(gr,n,s):
    distance = [0] * n
    unseen_node = range(1,n+1)
    see_node = {}
    see_node_plus={}
    unseen_node.remove(s)
    NODE=0
    see_node[s]=1

    for node in unseen_node:
        if len(gr.neighbors(node))==1:
            for do_node in gr.neighbors(node):
                distance[node-1] = gr.get_edge_weight((node,do_node))
                unseen_node.remove(node)
                see_node_plus[do_node] = 1
                see_node_plus[node] = 1
    while len(unseen_node):
        MIN = 'inf'
        for do_node in see_node:

            # if not see_node_plus.get(do_node) and see_node[do_node] >=3:
            #     continue
            # if see_node_plus.get(do_node) and see_node[do_node] + see_node_plus[do_node] >= 3:
            #     continue
            for node in gr.neighbors(do_node):
                #print 'loop begin',MIN
                if node not in see_node:
                    if gr.get_edge_weight((node, do_node)) < MIN:
                        MIN = gr.get_edge_weight((node,do_node))
                        NODE = node
                        DO_NODE = do_node
                    #print 'zhongjian',node,do_node,MIN
        #print 'step'
        #print NODE,DO_NODE,MIN
        distance[NODE-1] =  MIN
        see_node[DO_NODE] += 1
        unseen_node.remove(NODE)      
        see_node[NODE] = 1
        #print 'distance',distance
        #print 'ado-nodes',see_node,unseen_node
        #print distance
    return sum(distance)


if __name__ == '__main__':
    gr = graph()
    N, M = map(int,raw_input().split())
    for _ in range(1,N+1):
        gr.add_node(_)
    for _ in xrange(M):
        x, y, r = map(int,raw_input().split())
        if gr.has_edge((x, y)) and gr.get_edge_weight((x, y)) > r:
            gr.del_edge((x, y))
            gr.add_edge((x, y), r)
        else:
            gr.add_edge((x, y), r)

    S = int(raw_input())
    #print gr.get_edge_weight((1,3))
    print solution(gr, N, S)