import random
class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.color=None
        self.f=0


class LinkedList:
    def __init__(self, head):
        
        self.head = head
      
    
    def insert_at_head(self, value):

        value.next = self.head
        self.head = value



class Directed_Graph:
    def __init__ (self, V, E):
        self.vertex_set = [LinkedListNode(e) for e in V]
        self.vertex_index=[e for e in V]
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList(self.vertex_set[i]) for i in range(len(self.vertex_set))]
      
        for couple in self.edges_set:
            v1,v2 = couple   
            self.adj_array[self.vertex_index.index(v1)].insert_at_head(self.vertex_set[self.vertex_index.index(v2)])

    
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
    def transposed_graph(self):
        new_edges=[(y,x) for (x,y) in self.edges_set]
        t_g=Directed_Graph(self.vertex_index, new_edges)
        t_g.adj_list_representation()
        
        return t_g
    
    def connected_components(self):
        dfs(self)
        t_g=self.transposed_graph()
        dfs(t_g)

class Directed_Graph_Weighted:
    def __init__ (self, V, E):
        self.vertex_set = [LinkedListNode(e) for e in V]
        self.vertex_index=[e for e in V]
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList() for _ in range(len(self.vertex_set))]
 
        for edge in self.edges_set:
            v1,v2,weight = edge   
            self.adj_array[self.vertex_index.index(v1)].insert_at_head(self.vertex_set[self.vertex_index.index(v2)])


    
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


global u_f
u_f=0
def dfs(G):
    for vertex in G.vertex_set:
        vertex.color='white'
    

    for vertex in G.vertex_set:
        if vertex.color == 'white':
            
            dfs_visit(G,vertex)
          
            print(end='\n')

def dfs_visit(G,vertex):
    global u_f
    vertex.color='grey'
    print('('+str(vertex.value),end='')
    current=G.adj_array[G.vertex_index.index(vertex.value)].head
    
    while current.value != vertex.value:
        
        if current.color=='white':
            
            dfs_visit(G,current)
        current=current.next
      
        
    vertex.color='black'
    u_f=u_f+1
    vertex.f=u_f
    print(str(vertex.value)+')', end='')
   
    

    #print(current.head.value, vertex.value)



V_G = [1,2,3,4,5,6,12]
E_G = [(1,2),(2,3),(3,4),(5,6),(6,12)]

D_g = Directed_Graph(V_G,E_G)


D_g.adj_list_representation()
dfs(D_g)
for vertex in D_g.vertex_set:
    print(vertex.f)

#D_g.connected_components()

#print (D_g)


