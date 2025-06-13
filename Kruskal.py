

"""Kruskal's Algorithm is a greedy algorithm designed to find a minimum spanning tree for a connected, undirected, and weighted graph. 
The goal of the algorithm is to construct a tree that connects all the vertices in the graph while minimizing the total sum of the edge weights, 
and ensuring that no cycles are formed.
The algorithm operates by considering edges in increasing order of weight, and incrementally builds the minimum spanning tree 
by adding the smallest possible edge at each step, provided that it does not form a cycle with the edges already included."""



class LinkedListNode_for_Graph:
    def __init__(self, value, weight=1, next=None):
        self.value = value
        self.weight = weight
        self.next = next

    def __str__(self):
        return str(self.value) + "(" + str (self.weight) +")"



class LinkedList_G:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current)
            if current.next:
                result += " -> "
            current = current.next
        return result
    

    def insert_at_head(self, value, weight=1):
        node = LinkedListNode_for_Graph(value, weight)
        node.next = self.head
        self.head = node




"""To efficiently detect cycles, Kruskal’s algorithm relies on the Disjoint Set Union-Find data structure,
which tracks the components (subsets of vertices) as they are merged together."""

class DisjointSet:
    def __init__(self, vertices):
        self.representative = {v: v for v in vertices}

    def find(self, v):
        if self.representative[v] != v:
            self.representative[v] = self.find(self.representative[v])  
        return self.representative[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.representative[root_v] = root_u




class UndirectedWeightedGraph:

    """The parameter vertices must be a list (or another ordered iterable), as it is used with enumerate to create a mapping 
    from each vertex to its index.
    This index mapping is then used to build the adjacency list representation of the graph."""

    def __init__(self, vertices, edges):
        self.vertex_set = vertices
        self.edges_set = edges  
        self.adj_array = [LinkedList_G() for _ in range(len(vertices))]
        self.vertex_to_index = {v: i for i, v in enumerate(vertices)}


    def adj_list_representation(self):
        for u, v, w in self.edges_set:
            self.adj_array[self.vertex_to_index[u]].insert_at_head(v, w)
            self.adj_array[self.vertex_to_index[v]].insert_at_head(u, w)


    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i]) + ": " + str(linked_list) + "\n"
        return result
    

    def kruskal(self):
        disjoint_set = DisjointSet(self.vertex_set)
        min_spann_t = []
        total_weight = 0

        sorted_edges = sorted(self.edges_set, key=lambda x: x[2])

        for u, v, weight in sorted_edges:
            if disjoint_set.find(u) != disjoint_set.find(v):
                disjoint_set.union(u, v)
                min_spann_t.append((u, v, weight))
                total_weight += weight

        return min_spann_t, total_weight
    


V = ["A","B","C","D","E","F","G","H","I"]
E = [('A', 'B', 4), ('B', 'C', 8), ('A', 'H', 8), ('C', 'D', 7), 
     ('B', 'H', 11),("H","I",7),("H","G",1),("G","F",2),("D","E",9),
     ("E","F",10),("G","I",6),("C","I",2), ("C","F",4),("D","F",14)]


UG = UndirectedWeightedGraph(V, E)
UG.adj_list_representation()
print("Adjacency list representation:" + str(UG))

minimum_spanning_tree, total = UG.kruskal()
print("Minimum spanning tree:", minimum_spanning_tree)
print("Total weight:", total)