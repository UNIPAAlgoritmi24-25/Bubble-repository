
import random

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
    

    

    def random_adj_matrix(self, n_vertex, n_edges):
        
        adj_matrix = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]
        random_couples = set()
        
        while len(random_couples) < n_edges:
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex))
            random_couples.add(couple)
        
        for couple in random_couples:
            i, j = couple
            adj_matrix[i - 1][j - 1] = 1  
            
        return adj_matrix
    



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
            print("Tree rooted at " + str(root_val) + ":")
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




V = [LinkedListNode_for_Graph(i) for i in range(1, 7)]
E = [(1, 2), (1, 4), (2, 5), (3, 5), (5, 4), (4, 2), (3, 6), (6, 6)]

G = Directed_Graph(V, E)
G.adj_list_representation()
G.depth_first_search(start_vertex=1)



"""-------------------------------------------------------------------------"""


class LinkedListNode_for_Graph:
    def __init__(self, value, weight=1, next=None):
        self.value = value
        self.weight = weight  
        self.next = next
        self.color = "white"
        self.distance = float("inf")
        self.parent = None
        self.discovery = None
        self.finished = None

    def __str__(self):
        return "(Node: " + str (self.value) + " )"
 

class LinkedList_G:
    def __init__(self, head=None):
        self.head = head

    def insert_at_head(self, value):
        node = LinkedListNode_for_Graph(value)
        node.next = self.head
        self.head = node

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current)
            if current.next:
                result += " -> "
            current = current.next
        return result

    


class Undirected_Unweighted_Graph:
    def __init__(self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []
        self.vertex_index = {v.value: i for i, v in enumerate(V)}



    def adj_list_representation(self):
        self.adj_array = [LinkedList_G() for _ in range(len(self.vertex_set))]
        for u, v in self.edges_set:
            self.adj_array[self.vertex_index[u]].insert_at_head(v)
            self.adj_array[self.vertex_index[v]].insert_at_head(u)  
        return self.adj_array
    



    def random_adj_matrix(self, n_vertex, n_edges):
        
        adj_matrix = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]
        random_couples = set()
        
        while len(random_couples) < n_edges:
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex))
            random_couples.add(couple)
        
        for couple in random_couples:
            i, j = couple
            adj_matrix[i - 1][j - 1] = 1  
            adj_matrix[j - 1][i - 1] = 1
            
        return adj_matrix
    
    

    def __str__(self):
        result = "Adjacency List Representation:\n"
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result
    


    def initialize_node(self):
        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None



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
    



    def depth_first_search(self):
        self.initialize_node()
        self.time = 0
        forest = []

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self._dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

        for root_val, nodes in forest:
            print("\nDFS Tree rooted at " + str(root_val) +":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) + " (discovery=" + str(node.discovery) + ", finish=" + str(node.finished) + ", parent=" + str(parent_val) + ")")
            




    def _dfs_visit(self, u, tree_nodes):
        self.time += 1
        u.discovery = self.time
        u.color = "grey"
        tree_nodes.append(u)

        u_index = self.vertex_index[u.value]
        current = self.adj_array[u_index].head

        while current:
            v = self.vertex_set[self.vertex_index[current.value]]
            if v.color == "white":
                v.parent = u
                self._dfs_visit(v, tree_nodes)
            current = current.next

        u.color = "black"
        self.time += 1
        u.finished = self.time





V = [LinkedListNode_for_Graph(i) for i in range(1, 7)]
E = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6)]

G = Undirected_Unweighted_Graph(V, E)
G.adj_list_representation()
print(G)

print("BFS from node 1:")
for node in G.breadth_first_search(1):
    print("Node " + str(node.value) + " , Distance = " + str(node.distance) +" , Parent = " +str(node.parent.value if node.parent else None) + ")")

G.depth_first_search()



"""-----------------------------------------------------------------------"""




class LinkedListNode_for_Graph:
    def __init__(self, value, weight=1, next=None):
        self.value = value
        self.weight = weight
        self.next = next
        self.color = "white"
        self.distance = float("inf")
        self.parent = None
        self.discovery = None
        self.finished = None

    def __str__(self):
        parent_val = self.parent.value if self.parent else None
        return "(Node: " + str(self.value)+ ", Weight: " + str(self.weight) + ")"
        



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




class Directed_Weighted_Graph:

    def __init__(self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []
        self.vertex_index = {v.value: i for i, v in enumerate(V)}



    def adj_list_representation(self):
        self.adj_array = [LinkedList_G() for _ in range(len(self.vertex_set))]
    
        for from_val, to_val, weight in self.edges_set:
            self.adj_array[self.vertex_index[from_val]].insert_at_head(to_val, weight)
    
        return self.adj_array
    
    

    def random_adj_matrix(self, n_vertex, n_edges):
        
        adj_matrix = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]
        random_couples = set()
        
        while len(random_couples) < n_edges:
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex), random.randint(1,101))
            random_couples.add(couple)
        
        for couple in random_couples:
            i, j, w = couple
            adj_matrix[i - 1][j - 1] = w
            
        return adj_matrix



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
            v.weight = 1




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
            print("Tree rooted at " + str(root_val) + ":")
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



V = [LinkedListNode_for_Graph(i) for i in range(1, 7)]
E = [(1, 2, 4), (1, 4, 5), (2, 5, 2),(3, 5, 3), (5, 4, 11), (4, 2, 9),(3, 6, 111), (6, 6, 22)]

G = Directed_Weighted_Graph(V, E)
G.adj_list_representation()

print("Adjacency List Representation of the Graph:")
print(G)


print("BFS (from vertex 1)")
bfs_result = G.breadth_first_search(1)
for node in bfs_result:
    parent_val = node.parent.value if node.parent else None
    print("Node "+ str (node.value) + ": Distance = " + str(node.distance) + ", Parent = "+ str(parent_val))

print("DFS")
G.depth_first_search()


matrix = G.random_adj_matrix(4, 5)
for row in matrix:
    print(row)




"""-----------------------------------------------------------------------"""



class LinkedListNode_for_Graph:
    def __init__(self, value, weight=1, next=None):
        self.value = value
        self.weight = weight
        self.next = next
        self.color = "white"
        self.distance = float("inf")
        self.parent = None
        self.discovery = None
        self.finished = None

    def __str__(self):
        if self.weight is not None:
            return "(Node: " + str(self.value) + ", Weight: " + str(self.weight) + ")"
        else:
            return "(Node: " + str(self.value) + ")"




class LinkedList_G:
    def __init__(self, head=None):
        self.head = head

    def insert_at_head(self, value, weight=1):
        node = LinkedListNode_for_Graph(value, weight)
        node.next = self.head
        self.head = node

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result += str(current)
            if current.next:
                result += " -> "
            current = current.next
        return result
    

    

class Undirected_Weighted_Graph:
    def __init__(self, V, E):
        self.vertex_set = V
        self.edges_set = E  
        self.adj_array = []
        self.vertex_index = {v.value: i for i, v in enumerate(V)}


    def adj_list_representation(self):
        self.adj_array = [LinkedList_G() for _ in self.vertex_set]
        for u, v, w in self.edges_set:
            self.adj_array[self.vertex_index[u]].insert_at_head(v, w)
            self.adj_array[self.vertex_index[v]].insert_at_head(u, w)  
        return self.adj_array
    



    def random_adj_matrix(self, n_vertex, n_edges):
        
        adj_matrix = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]
        random_couples = set()
        
        while len(random_couples) < n_edges:
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex), random.randint(1,101))
            random_couples.add(couple)
        
        for couple in random_couples:
            i, j, w = couple
            adj_matrix[i - 1][j - 1] = w
            adj_matrix[j - 1][i - 1] = w
            
        return adj_matrix



    def __str__(self):
        result = "Adjacency List Representation:\n"
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result
    

    def initialize_node(self):
        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None



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
            current = self.adj_array[u_index].head

            while current:
                neighbor = self.vertex_set[self.vertex_index[current.value]]
                if neighbor.color == "white":
                    neighbor.color = "grey"
                    neighbor.distance = u.distance + 1
                    neighbor.parent = u
                    queue.enqueue(neighbor)
                current = current.next

            u.color = "black"

        return visited
    



    def depth_first_search(self):
        self.initialize_node()
        self.time = 0
        forest = []

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self._dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

        for root_val, nodes in forest:
            print("DFS Tree rooted at "+ str(root_val)+":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) + "discovery= " + str(node.discovery) + ", finish= " + str(node.finished) +", parent= " + str(parent_val))




    def _dfs_visit(self, u, tree_nodes):
        self.time += 1
        u.discovery = self.time
        u.color = "grey"
        tree_nodes.append(u)

        u_index = self.vertex_index[u.value]
        current = self.adj_array[u_index].head
        while current:
            neighbor = self.vertex_set[self.vertex_index[current.value]]
            if neighbor.color == "white":
                neighbor.parent = u
                self._dfs_visit(neighbor, tree_nodes)
            current = current.next

        u.color = "black"
        self.time += 1
        u.finished = self.time



V = [LinkedListNode_for_Graph(i) for i in range(1, 7)]
E = [(1, 2, 4), (1, 4, 5), (2, 5, 2), (3, 5, 3), (5, 4, 11), (4, 2, 9), (3, 6, 111), (6, 6, 22)]

G = Undirected_Weighted_Graph(V, E)
G.adj_list_representation()
print(G)

print("BFS from node 1:")
for node in G.breadth_first_search(1):
    print("Node " + str(node.value) +", Distance = " + str(node.distance) + ", Parent = " + str(node.parent.value if node.parent else None))

print("DFS:")
G.depth_first_search()