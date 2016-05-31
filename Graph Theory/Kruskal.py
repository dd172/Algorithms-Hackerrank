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

class WeightedUF():  
    fatherid=[]  
    sz=[]  
    count=0  
    def __init__(self,n):  
        self.count=n  
        self.fatherid=[i for i in range(n)]  
        self.sz=[0 for i in range(n)]  
    def getcount(self):  
        return self.count  
    def connected(self,p,q):  
        return self.find(p)==self.find(q)  
    def find(self,p):  
        while p !=self.fatherid[p]:  
            p=self.fatherid[p]  
        return p  
    def pathcompressionfind(self,p):  
        if p==self.fatherid[p]:  
            return p  
        else:  
            self.fatherid[p]=self.pathcompressionfind(self.fatherid[p])  
            return self.fatherid[p]  
    def union(self,p,q):  
        i=self.find(p)  
        j=self.find(q)  
        if i==j:  
            return   
        if self.sz[i]<self.sz[j]:  
            self.fatherid[i]=j  
            self.sz[j]+=self.sz[i]  
        else:  
            self.fatherid[j]=i  
            self.sz[i]+=self.sz[j]  
        self.count-=1 

  
  
  


def solution(gr,n,m,s):
    unseen_node = range(1,n+1)
    mark = [0] * m
    see_node = []
    distance = 0
    UF = WeightedUF(n+1)
    #print UF.sz
    list = sorted(gr.get_edge_weights())
    #print list[0:50]
    #print list
    while len(list):
        MIN = 'inf'
        MIN_NODE = 'inf'
        #print list
        for (r,(x,y)) in list:
            #print r,x,y, UF.connected(x,y)
            if not UF.connected(x,y):
                if r <= MIN and x+y < MIN_NODE:
                    MIN = r
                    u,v = x,y
                    MIN_NODE = x + y
                if r > MIN:
                    break
        for (r,(x,y)) in list:
            if r > MIN:
                break
            if UF.connected(x,y):
                list.remove((r,(x,y)))
        #print '-',MIN,u,v
        if MIN != 'inf':
            list.remove((MIN,(u,v)))
            distance += MIN
        UF.union(u,v)
        
        #print see_node
    
    return distance


if __name__ == '__main__':
    gr = graph()
    N, M = map(int,raw_input().split())
    for i in range(1,N+1):
        gr.add_node(i)
    for _ in xrange(M):
        x, y, r = map(int,raw_input().split())
        if gr.has_edge((x, y)) and gr.get_edge_weight((x,y)) > r:
            gr.del_edge((x, y))
            gr.add_edge((x, y), r)
        elif not gr.has_edge((x, y)):
            gr.add_edge((x, y), r)
    S = int(raw_input())
    #print gr
    #print gr.get_edge_weights()
    print solution(gr,N,M,S)
