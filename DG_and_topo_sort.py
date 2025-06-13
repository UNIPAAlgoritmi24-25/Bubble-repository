
"""In the LinkedListNode_for_Graph class I defined attributes used in the BFS (distance), 
and in the DFS (discovery for the discovery time, and finished for the finishing time)"""


class LinkedListNode_for_Graph:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.color = "white"
        self.distance = float("inf")
        self.parent = None
        self.discovery = None
        self.finished = None

    def __str__(self):
        parent_val = self.parent.value if self.parent else None
        return "(Node: " + str(self.value) + ", Distance: " + str(self.distance) + ", Parent: " + str(parent_val) + ")"




class LinkedList_G:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current.value)
            if current.next:
                result += " -> "
            current = current.next
        return result

    def insert_at_head(self, node):
        node.next = self.head
        self.head = node





"""The Queue class implements the FIFO (First-In-First-Out) data structure used in BFS to keep track of the nodes to be explored next. 
This allows BFS to explore nodes level-by-level, ensuring that nodes closer to the source are visited before nodes farther away."""

class Queue:
    def __init__(self):
        self.q = []

    def queue_empty(self):
        return len(self.q) == 0

    def enqueue(self, el):
        self.q.insert(0, el)

    def dequeue(self):
        if not self.queue_empty():
            return self.q.pop()
        return None




class Directed_Graph:

    def __init__(self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []
        self.vertex_index = {v.value: i for i, v in enumerate(V)}


    def adj_list_representation(self):
        self.adj_array = [LinkedList_G() for _ in range(len(self.vertex_set))]
        for v1, v2 in self.edges_set:
            node = LinkedListNode_for_Graph(v2)
            self.adj_array[self.vertex_index[v1]].insert_at_head(node)
        return self.adj_array


    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result



    """The initialize_node method resets all node attributes to their default values before starting any graph traversal algorithm, 
    such as BFS, DFS, or Topological Sort. Specifically, it sets: color to "white" (unvisited), distance to infinity (for BFS),
    parent to None (no predecessor), discovery and finished times to None (used in DFS and Topological Sort)."""


    def initialize_node(self):
        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None




    """Breadth-First Search is a graph traversal algorithm that starts from a designated source vertex and explores all vertices reachable 
    from it by visiting vertices in order of their distance from the source (measured in the number of edges). 
    BFS explores the graph in layers, visiting all neighbors of a vertex before moving on to vertices at the next distance level."""


    def breadth_first_search(self, source_value):
        self.initialize_node()
        source = self.vertex_set[self.vertex_index[source_value]]
        source.color = "grey"
        source.distance = 0

        queue = Queue()
        queue.enqueue(source)
        visited = []

        while not queue.queue_empty():
            u = queue.dequeue()
            visited.append(u)
            u_index = self.vertex_index[u.value]
            current_adj_node = self.adj_array[u_index].head

            while current_adj_node:
                v_val = current_adj_node.value
                v = self.vertex_set[self.vertex_index[v_val]]
                if v.color == "white":
                    v.color = "grey"
                    v.distance = u.distance + 1
                    v.parent = u
                    queue.enqueue(v)
                current_adj_node = current_adj_node.next

            u.color = "black"

        return visited
    


    """Depth-First Search is a graph traversal algorithm that starts at a source vertex and explores as far along each branch as possible 
    before backtracking. It recursively visits an unvisited adjacent vertex, marking vertices as discovered, 
    and records discovery and finishing times during traversal."""


    def depth_first_search(self, start_vertex=None):
        self.initialize_node()
        self.time = 0
        forest = []

        if start_vertex is not None:
            start_node = self.vertex_set[self.vertex_index[start_vertex]]
            if start_node.color == "white":
                tree_nodes = []
                self._dfs_visit(start_node, tree_nodes)
                forest.append((start_node.value, tree_nodes))

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self._dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

       

        for root_val, nodes in forest:
            print("\nTree rooted at " + str(root_val) + ":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) + " (discovered=" + str(node.discovery) + ", finished=" + str(node.finished) + ", parent=" + str(parent_val) + ")")


        
    def _dfs_visit(self, u, tree_nodes):
        self.time += 1
        u.discovery = self.time
        u.color = "grey"
        tree_nodes.append(u)

        u_index = self.vertex_index[u.value]
        current = self.adj_array[u_index].head
        neighbors = []
        while current:
            neighbors.append(current.value)
            current = current.next
        neighbors.reverse()

        for val in neighbors:
            v = self.vertex_set[self.vertex_index[val]]
            if v.color == "white":
                v.parent = u
                self._dfs_visit(v, tree_nodes)

        u.color = "black"
        self.time += 1
        u.finished = self.time





    """Topological Sort is an ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v),
    vertex u appears before v in the ordering."""

    def topological_sort(self):
        self.initialize_node()
        self.time = 0
        topo_sort_stack = []
        rec_stack = set()
        self.has_cycle = False

        for v in self.vertex_set:
            if v.color == "white":
                self.dfs_topo(v, topo_sort_stack, rec_stack)
                if self.has_cycle:
                    break

        if self.has_cycle:
            return (False, [])  
        else:
            return (True, [node.value for node in reversed(topo_sort_stack)])




    """The dfs_topo method is a DFS modified for topological sort and cycle detection (to see if the graph is a DAG)
    
    N.B.Since adjacency lists are built by inserting nodes at the head for efficiency (constant-time insertion),
    the order of neighbors in each list is reversed compared to the original input. 
    To ensure a predictable and input-consistent traversal order during DFS, we reverse the list of neighbors before visiting them."""

    def dfs_topo(self, u, topo_stack, rec_stack):
        self.time += 1
        u.discovery = self.time
        u.color = "grey"
        rec_stack.add(u.value)

        u_index = self.vertex_index[u.value]
        current = self.adj_array[u_index].head
        neighbors = []
        while current:
            neighbors.append(current.value)
            current = current.next
        neighbors.reverse()

        for el in neighbors:
            v = self.vertex_set[self.vertex_index[el]]
            if v.color == "white":
                v.parent = u
                self.dfs_topo(v, topo_stack, rec_stack)
                if self.has_cycle:
                    return
            elif v.value in rec_stack:
                
                self.has_cycle = True
                return

        u.color = "black"
        self.time += 1
        u.finished = self.time
        rec_stack.remove(u.value)
        topo_stack.append(u)




V = [LinkedListNode_for_Graph(i) for i in range(1, 7)]
E = [(1, 2), (1, 4), (2, 5), (3, 5), (5, 4), (4, 2), (3, 6), (6, 6)]

G = Directed_Graph(V, E)
G.adj_list_representation()
G.depth_first_search(start_vertex=1)




V = [LinkedListNode_for_Graph(ch) for ch in ["a", "b", "c", "d", "e", "f", "g", "h"]]
E = [("a", "d"), ("a", "c"), ("b", "d"), ("c", "d"), ("c", "f"), ("f", "g"), ("e", "f"), ("e", "g")]

g = Directed_Graph(V, E)
g.adj_list_representation()
print(g.topological_sort())  


V_G2 = [LinkedListNode_for_Graph(i) for i in range(1, 9)]
E = [(1,4), (1,3), (2,4), (3,4), (3,6), (6,7), (5,6), (5,7)]

g2 = Directed_Graph(V_G2, E)
g2.adj_list_representation()
print(g2.topological_sort())