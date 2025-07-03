import heapq
from Undirected_Graph import Undirected_Graph_Weighted

def prim(graph):
    if not graph.vertex_set:
        return []
    
    vertices = list(graph.vertex_set)
    key = {v: float('inf') for v in vertices}  # key[v] = ∞
    parent = {v: None for v in vertices}       # parent[v] = NIL
    
    root = vertices[0]
    key[root] = 0  # radice messa a 0
    
    Q = [(key[v], v) for v in vertices]
    heapq.heapify(Q) #per ordinare
    
    adjacency = {v: [] for v in vertices}
    edge_weights = {}
    
    for u, v, weight in graph.edges_set:
        adjacency[u].append(v)
        adjacency[v].append(u)
        edge_weights[(u, v)] = weight
        edge_weights[(v, u)] = weight
    
    in_mst = set()
    
    while Q:
        # Extract-Min
        current_key, u = heapq.heappop(Q)
        
        # Se abbiamo già processato questo vertice vai avanti
        if u in in_mst:
            continue
            
        # Se la key è cambiata vai avanti
        if current_key > key[u]:
            continue
            
        in_mst.add(u)
        
        for v in adjacency[u]:
            if v not in in_mst: 
                weight = edge_weights[(u, v)]
                
                if weight < key[v]:
                    parent[v] = u      
                    key[v] = weight    
                    # Decrease-Key(Q, v, w(u,v))
                    heapq.heappush(Q, (weight, v))
    
    mst = []
    for v in vertices:
        if parent[v] is not None:
            mst.append((parent[v], v, key[v]))
    
    return mst


# test
if __name__ == "__main__":
    # Stesso grafo usato in Kruskal per confrontarlo
    V = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    E = [('A','B', 4), ('B', 'C', 8), ('A', 'H',8), ('C', 'D', 7), 
         ('B', 'H', 11), ("H", "I", 7), ("H", "G", 1), ("G", "F", 2), 
         ("D", "E",9), ("E", "F", 10), ("G", "I", 6), ("C", "I", 2), 
         ("C", "F", 4), ("D", "F",14) ]
    
    graph = Undirected_Graph_Weighted(V, E)
    
    mst = prim(graph)
    
    print("Minimum Spanning Tree:")
    total_weight = 0
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")
        total_weight += w
    
    print(f"\nTotal weight: {total_weight}")