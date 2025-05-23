import random
class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class LinkedList:
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
    
    def insert_at_head(self, value):
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node



class Directed_Graph:
    def __init__ (self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList() for _ in range(len(self.vertex_set))]
        for couple in self.edges_set:
            v1,v2 = couple
            self.adj_array[v1-1].insert_at_head(v2)

    
    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(self.vertex_set[i]) + ":"+ str(linked_list)+ "\n"
        return result
    
        
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

class Directed_Graph_Weighted:
    def __init__ (self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList() for _ in range(len(self.vertex_set))]
        for edge in self.edges_set:
            v1,v2,weight = edge
            self.adj_array[v1-1].insert_at_head(v2)

    
    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result +=  str(self.vertex_set[i]) + ":"+ str(linked_list)+ "\n"
        return result
    
        
    def random_adj_matrix(self, n_vertex, n_edges):
        
        adj_matrix = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]
        random_couples = set()
        
        while len(random_couples) < n_edges:
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex))
            random_couples.add(couple)
        
        for couple in random_couples:
            i, j = couple
            adj_matrix[i - 1][j - 1] = random.randint(1,9)  
            
        return adj_matrix
      

V_G = [1,2,3,4,5,12]
E_G = [(1,2),(3,4),(5,6),(2,1), (1,3)]
D_g = Directed_Graph(V_G,E_G)
D_g.adj_list_representation()
print (D_g)
m2 = D_g.random_adj_matrix(7,12)
print(m2)