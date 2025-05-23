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



class Undirected_Graph:
    def __init__ (self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList() for _ in range(len(self.vertex_set))]
        for v1, v2 in self.edges_set:
            self.adj_array[v1-1].insert_at_head(v2)
            self.adj_array[v2-1].insert_at_head(v1)
    
    def __str__(self):
        result = ""
        for i, linked_list in enumerate(self.adj_array):
            result += str(i+1) + ":"+ str(linked_list)+ "\n"
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
            adj_matrix[j - 1][i - 1] = 1  
            
        return adj_matrix

class Undirected_Graph_Weighted:
    def __init__ (self, V, E):
        self.vertex_set = V
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList() for _ in range(len(self.vertex_set))]
     
        for edge in self.edges_set:
            v1,v2,weight = edge
            
            self.adj_array[self.vertex_set.index(v1)].insert_at_head(v2)
            self.adj_array[self.vertex_set.index(v2)].insert_at_head(v1)

    
    def __str__(self):
        result = ""
        for i,linked_list in enumerate(self.adj_array):
         
            result += str(self.vertex_set[i]) + "->"+ str(linked_list)+ "\n"
            if i > len(self.edges_set):
                break
        return result
    
        
    def random_adj_matrix(self, n_vertex, n_edges):
        
        adj_matrix = [[0 for _ in range(n_vertex)] for _ in range(n_vertex)]
        random_couples = set()
        
        while len(random_couples) < n_edges:
            couple = (random.randint(1, n_vertex), random.randint(1, n_vertex))
            random_couples.add(couple)
        
        for couple in random_couples:
            i, j = couple
            val= random.randint(1,9)  
            adj_matrix[i - 1][j - 1] =val
            adj_matrix[j - 1][i -1 ] =val
            
        return adj_matrix

V=[1,2,34,3]
E=[(1,2,3),(2,3,3),(3,34,3)]
D_g = Undirected_Graph_Weighted(V,E)
D_g.adj_list_representation()
print (D_g)
