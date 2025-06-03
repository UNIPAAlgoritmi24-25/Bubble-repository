import random
class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.color=None
        self.f=0
        self.d=None
        self.prev=None


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
        dfs(self, False)
        t_g=self.transposed_graph()
        t_g.vertex_set=self.vertex_set

        dfs(t_g, True)

class Directed_Graph_Weighted:
    def __init__ (self, V, E):
        self.vertex_set = [LinkedListNode(e) for e in V]
        self.vertex_index=[e for e in V]
        self.edges_set = E
        self.adj_array = []

    def adj_list_representation (self):
        self.adj_array = [LinkedList(self.vertex_set[i]) for i in range(len(self.vertex_set))]
 
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



def dfs(G, f_order=False):
    for vertex in G.vertex_set:
        vertex.color='white'
    
    global u_f
    u_f=0
    if f_order == False:

        for vertex in G.vertex_set:
            if vertex.color == 'white':
                
                dfs_visit(G,vertex)
            
                print(end='\n')
    else:
      
        for vertex in sorted(G.vertex_set, key=lambda x: x.f):
            if vertex.color == 'white':
                dfs_visit(G,vertex, 0)
            
                print(end='\n')

def dfs_visit(G,vertex, update_end=1):
    global u_f
    vertex.color='grey'
    print('('+str(vertex.value),end='')
    current=G.adj_array[G.vertex_index.index(vertex.value)].head
    s=[]
    while current is not None and current.value not in s:
        i=self.parent(i)

        s.append(current.value)
        
        if current.color=='white':
            dfs_visit(G,current)
        
        current=current.next
    
    vertex.color='black'
    if update_end==1:
        u_f=u_f+1
        vertex.f=u_f
    print(str(vertex.value)+')', end='')
   
    

    #print(current.head.value, vertex.value)

class min_heap:
    def __init__(self):
        self.heap=[]
        self.heap_size=0
    def minimum(self):
        return self.heap[0]
    def parent(self,i):
        return (i-1) // 2
    def left(self,i):
        return (2*i)+1
    def right(self, i):
        return (2*i)+2
    def min_heapify(self,i):
        A=self.heap 
        left=self.left(i)
        right=self.right(i)
        
        p = i 

        if left < self.heap_size and A[left].d < A[p].d:
            p = left

        if right < self.heap_size and A[right].d < A[p].d:
            p = right

  
        if p != i:
            A[i], A[p] = A[p], A[i] 
            self.min_heapify(p)

    def extract_minimum(self):
        min_val = self.minimum() 
        A = self.heap

       
        A[0] = A[self.heap_size - 1]
        A.pop()
        self.heap_size -= 1 
        self.min_heapify(0)
        return min_val
    
    def insert(self,value):
        self.heap_size += 1
        self.heap.append(value)
        self.decrease_key(999,value)




    def decrease_key(self,x,k):
        if k.d < x:
            i=self.heap.index(k)
            while i > 0 and self.heap[self.parent(i)].d > self.heap[i].d:
                self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
                i=self.parent(i)


def relax(u,v,w):
    if v.d > u.d+w:
        v.d=u.d+w
        v.prev=u


def djkstra(G,s):
    for vertex in G.vertex_set: 
        vertex.d=999
        vertex.prev=None 
    s.d=0
    S=set()
    Q=min_heap()
    for vertex in G.vertex_set:
        Q.insert(vertex)
    while len(Q.heap) != 0:
        u=Q.extract_minimum()
        S.add(u)
        print(u.value)
     

V_G = [1,2,3,4,5,6,12]
E_G = [(1,2,3),(2,3,5),(3,4,6), (5,4,7)]

D_g = Directed_Graph_Weighted(V_G,E_G)


D_g.adj_list_representation()
djkstra(D_g, D_g.vertex_set[0])

