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

def solution(gr,n, s):
    distance = ['inf'] * n
    unseen_nodes = range(1,n+1)
    
    distance[s-1] = 0
    while len(unseen_nodes):
        #print [distance[x-1] for x in unseen_nodes]
        #print 'min',min([distance[x-1] for x in unseen_nodes])
        MIN = min([distance[x-1] for x in unseen_nodes])
        
        for i in range(n):
            if distance[i] == MIN:
                if i+1 in unseen_nodes:
                    node = i+1
                    break
        #print 'node:'node
        #print node
        for do_node in gr.neighbors(node):
            if do_node not in unseen_nodes:
                continue
            if gr.has_edge((node,do_node)):
                edge = gr.get_edge_weight((node,do_node))
                if distance[node-1] == 'inf':
                    continue
                if distance[do_node-1] == 'inf':
                    distance[do_node-1] = edge + distance[node-1]
                elif distance[do_node-1] > distance[node-1] + edge:
                    try:
                        distance[do_node-1] = distance[node-1] + edge
                    except:
                        #print 'distance error:',do_node,node,distance[do_node-1],distance[node-1]
                        print do_node,edge
        try:
            unseen_nodes.remove(node)
            #print 'remove node :', node
        except:
            print 'remove node error:', node
        finally:
            pass
        #print 'node',node,'removed'
        #print distance
    for item in distance:
        if item == 0:
            pass
        elif item == 'inf':
            print -1,
        else:
            print item,
    print


if __name__ == '__main__':
    for _ in xrange(int(raw_input())):

        N, M = map(int, raw_input().split())

        gr = graph()
        for node in range(1,N+1):
            gr.add_node(node)
        for i in range(M):

            x, y, r = map(int, raw_input().split())
            
            if gr.has_edge((x,y)):
                if r < gr.get_edge_weight((x, y)):
                    gr.del_edge((x, y))
                    gr.add_edge((x, y),r)
            if not gr.has_edge((x, y)):
                gr.add_edge((x,y),r)

        s = int(raw_input())

        #print gr.nodes()
        #print gr.neighbors(2)
        #print gr.neighbors(4)
        #print gr.get_edge_weight((4,3))
        solution(gr,N, s)