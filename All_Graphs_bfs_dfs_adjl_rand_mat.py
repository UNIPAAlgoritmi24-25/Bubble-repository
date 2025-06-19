
import random

"""Implementation of a basic directed graph structure with support for Breadth-First Search (BFS) and Depth-First Search (DFS). 
It uses linked lists to represent adjacency lists."""


class LinkedListNode_for_Graph:

    """Represents a node in an adjacency list for a graph. Contains additional attributes to support BFS and DFS, such as color, distance, parent, discovery and finished"""


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

    """Represents a linked list for storing adjacency nodes in a graph. Used to build adjacency lists for each vertex in the graph."""

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



class Queue:

    """Class used in BFS to track nodes to visit.
    (This class is shared across multiple graph implementations and is repeated in each for modularity and clarity.)"""

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

    """Represents a directed graph using an adjacency list.Supports graph creation, BFS, DFS, and random adjacency matrix generation."""

    
    def __init__(self, V, E):
        
        """Initializes the graph with a list of vertices (V) and a list of edges (E). Builds a vertex-to-index map. """

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
            
        return  adj_matrix, random_couples
    



    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result




    def initialize_node(self):

        """Resets traversal-related attributes (color, distance, parent, discovery and finished) for all nodes in preparation for BFS or DFS. """

        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None







    def breadth_first_search(self, source_value):

        """Performs Breadth-First Search starting from the vertex with the given value.Returns a list of visited nodes in the order they were explored."""

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
    





    def depth_first_search(self, start_vertex=None):

        """Performs Depth-First Search (DFS) on the graph. If start_vertex is provided, begins traversal from that vertex;otherwise, performs DFS on the entire graph (forest).
        Prints the DFS tree with discovery and finishing times."""


        self.initialize_node()
        self.time = 0
        forest = []

        if start_vertex is not None:
            start_node = self.vertex_set[self.vertex_index[start_vertex]]
            if start_node.color == "white":
                tree_nodes = []
                self.dfs_visit(start_node, tree_nodes)
                forest.append((start_node.value, tree_nodes))

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self.dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

        for root_val, nodes in forest:
            print("Tree rooted at " + str(root_val) + ":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) + " (discovered=" + str(node.discovery) + 
                      ", finished=" + str(node.finished) + ", parent=" + str(parent_val) + ")")
                




    def dfs_visit(self, u, tree_nodes):

        """Method for DFS that recursively explores the depth of the graph; marks discovery and finishing times, and builds the DFS tree"""

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
                self.dfs_visit(v, tree_nodes)

        u.color = "black"
        self.time += 1
        u.finished = self.time





def test_f():
    vertices = [LinkedListNode_for_Graph(i) for i in range(1, 6)]
    edges = [(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)]
    graph = Directed_Graph(vertices, edges)

    graph.adj_list_representation()
    print("Adjacency List Representation")
    print(graph)
    print("BFS from Node 1") #ricordare di cambiare anche qui se si decide di cominciare da un nodo diverso
    bfs_result = graph.breadth_first_search(1)
    for node in bfs_result:
        print(str(node))

    print("\nDFS")
    graph.depth_first_search()

    print("\nRandom Adjacency Matrix (5 vertices, 6 edges)") #come per la BFS
    matrix = graph.random_adj_matrix(5, 6)
    for row in matrix:
        print(row)


test_f()




#---------------------------------------------------------------------------------------------------------





class LinkedListNode_for_Graph:

    """Represents a node in the adjacency list linked structure of a graph."""

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
        return "(Node: " + str(self.value) + ", Weight: " + str(self.weight) + ")"





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

        """Creates a new node with the given value and weight (default is 1), inserts it at the start of the list"""

        node = LinkedListNode_for_Graph(value, weight)
        node.next = self.head
        self.head = node




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




class Directed_Weighted_Graph:


    """Represents a directed weighted graph using adjacency lists."""

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
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex), random.randint(1, 101))
            random_couples.add(couple)

        for couple in random_couples:
            i, j, w = couple
            adj_matrix[i - 1][j - 1] = w

        return adj_matrix, random_couples
    



    def __str__(self):

        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result
    


    def initialize_node(self):

        """Resets traversal-related attributes"""

        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None
            v.weight = 1




    def breadth_first_search(self, source_value):
        
        """Performs BFS starting from the specified source vertex."""

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
    




    def depth_first_search(self, start_vertex=None):

        """Performs depth-first search (DFS) for the entire graph. If start_vertex is specified, starts DFS from that vertex.
        Prints discovery and finishing times and parent info for all nodes in DFS forest."""

        self.initialize_node()
        self.time = 0
        forest = []

        if start_vertex is not None:
            start_node = self.vertex_set[self.vertex_index[start_vertex]]
            if start_node.color == "white":
                tree_nodes = []
                self.dfs_visit(start_node, tree_nodes)
                forest.append((start_node.value, tree_nodes))

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self.dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

        for root_val, nodes in forest:
            print("Tree rooted at " + str(root_val) + ":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) + " (discovered=" + str(node.discovery) + ", finished=" + str(node.finished) + ", parent=" + str(parent_val) + ")")




    def dfs_visit(self, u, tree_nodes):

        """Updates discovery and finishing timestamps and tracks traversal tree."""

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
                self.dfs_visit(v, tree_nodes)

        u.color = "black"
        self.time += 1
        u.finished = self.time





def test_f2():

    vertices = [LinkedListNode_for_Graph(i) for i in range(1, 7)]
    edges = [(1, 2, 10), (1, 3, 5), (2, 4, 1),(3, 2, 3),(3, 4, 9),(3, 5, 2),(4, 5, 4),(5, 1, 7),(5, 6, 6),(6, 4, 2)]

    graph = Directed_Weighted_Graph(vertices, edges)
    graph.adj_list_representation()

    print("Adjacency List Representation:")
    print(graph)

    random_matrix = graph.random_adj_matrix(5, 8)
    print("Random Adjacency Matrix (5 vertices, 8 edges):") # in caso cambiare se si cambia numero di archi e vertici
    for row in random_matrix:
        print(row)

    print("\nBFS starting from vertex 1:")
    bfs_result = graph.breadth_first_search(1)
    for node in bfs_result:
        print("Node " + str(node.value) +", Distance: " + str(node.distance))

    print("\nDFS")
    graph.depth_first_search()


test_f2()




#---------------------------------------------------------------------

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
        return "(Node: " + str(self.value) + " )"
 

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



class Undirected_Unweighted_Graph:

    """Represents an undirected, unweighted graph using an adjacency list."""

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
            
        return adj_matrix, random_couples
    
    


    def __str__(self):
        
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result
    


    def initialize_node(self):
        
        """Resets traversal-related properties of each vertex in the graph."""

        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None




    def breadth_first_search(self, source_value):

        """ Performs BFS starting from the vertex with the given value."""

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

        """Performs Depth-First Search (DFS) over the entire graph."""

        self.initialize_node()
        self.time = 0
        forest = []

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self.dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

        for root_val, nodes in forest:
            print("\nDFS Tree rooted at " + str(root_val) + ":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) + " (discovery=" + str(node.discovery) + ", finish=" + str(node.finished) + ", parent=" + str(parent_val) + ")")
            



    def dfs_visit(self, u, tree_nodes):
    
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
                self.dfs_visit(v, tree_nodes)
            current = current.next

        u.color = "black"
        self.time += 1
        u.finished = self.time






def test3_f():

    vertices = [LinkedListNode_for_Graph(i) for i in range(1, 6)]
    edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
    graph = Undirected_Unweighted_Graph(vertices, edges)

    
    graph.adj_list_representation()
    print("\n Adjacency List")
    print(graph)


    print("\nBFS(from node 1) ")
    bfs_result = graph.breadth_first_search(1)
    for node in bfs_result:
        parent_val = node.parent.value if node.parent else None
        print("Node " + str(node.value) + ", Distance: " + str(node.distance) +", Parent: " + str(parent_val))


    print("\nDFS")
    graph.depth_first_search()


    print("\nRandom Adjacency Matrix (4 vertices, 6 edges)")
    edges = [(1, 2), (1, 3), (2, 4), (3, 5)]
    matrix, edge_set = graph.random_adj_matrix(4, 6)
    print(edge_set)
    for row in matrix:
        print(row)


test3_f()







#------------------------------------------------------------------

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
        return "(Node: " + str(self.value) + ", Weight: " + str(self.weight) + ")"
        




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
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex), random.randint(1, 101))
            random_couples.add(couple)

        for couple in random_couples:
            i, j, w = couple
            adj_matrix[i - 1][j - 1] = w
            adj_matrix[j - 1][i - 1] = w  

        return adj_matrix, random_couples
    



    def __str__(self):
        
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i].value) + ": " + str(linked_list) + "\n"
        return result




    def initialize_node(self):

        """Resets all vertex metadata to their default values. Used before any traversal like BFS or DFS."""

        for v in self.vertex_set:
            v.color = "white"
            v.distance = float("inf")
            v.parent = None
            v.discovery = None
            v.finished = None





    def breadth_first_search(self, source_value):
        
        """Performs BFS starting from the source vertex."""

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

        """Performs a DFS across the graph. Outputs DFS forest trees with discovery and finish times."""

        self.initialize_node()
        self.time = 0
        forest = []

        for v in self.vertex_set:
            if v.color == "white":
                tree_nodes = []
                self.dfs_visit(v, tree_nodes)
                forest.append((v.value, tree_nodes))

        for root_val, nodes in forest:
            print("DFS Tree rooted at " + str(root_val) + ":")
            for node in nodes:
                parent_val = node.parent.value if node.parent else None
                print("Node " + str(node.value) +" discovery= " + str(node.discovery) + ", finish= " + str(node.finished) +", parent= " + str(parent_val))
                



    def dfs_visit(self, u, tree_nodes):
       
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
                self.dfs_visit(neighbor, tree_nodes)
            current = current.next

        u.color = "black"
        self.time += 1
        u.finished = self.time







def test4_f():
    
    vertices = [LinkedListNode_for_Graph(i) for i in range(1, 6)]
    edges = [(1, 2, 4),(1, 3, 1),(2, 3, 2),(3, 4, 5),(4, 5, 3)]

    graph = Undirected_Weighted_Graph(vertices, edges)

    print("\nAdjacency List Representation:")
    graph.adj_list_representation()
    print(graph)

    
    print("\nBFS starting from vertex 1:")
    bfs_result = graph.breadth_first_search(1)
    for node in bfs_result:
        parent_val = node.parent.value if node.parent else None
        print("Node " + str(node.value) + ", Distance: " + str(node.distance) + ", Parent: " + str(parent_val))

    print("\nDFS")
    graph.depth_first_search()

    print("\nRandom Adjacency Matrix (6 vertices, 6 edges):")
    matrix = graph.random_adj_matrix(6, 6)
    for row in matrix:
        print(row)



test4_f()