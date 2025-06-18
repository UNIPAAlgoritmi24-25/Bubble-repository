import heapq
from Undirected_Graph import Undirected_Graph_Weighted
    
def prim(graph):
    if not graph.vertex_set or not graph.edges_set:
        return []
    
    edge_weights = {}
    adjacency = {v: [] for v in graph.vertex_set}
    
    for u, v, weight in graph.edges_set:
        edge_weights[(u, v)] = weight
        edge_weights[(v, u)] = weight
        adjacency[u].append(v)
        adjacency[v].append(u)
    
    mst = []
    visited = set()
    min_heap = []
    
    start = graph.vertex_set[0]
    visited.add(start)
    
    for v in adjacency[start]:
        weight = edge_weights[(start, v)]
        heapq.heappush(min_heap, (weight, start, v))
    
    while min_heap and len(visited) < len(graph.vertex_set):
        weight, u, v = heapq.heappop(min_heap)
        
        if v in visited:
            continue
            
        visited.add(v)
        mst.append((u, v, weight))
        
        for neighbor in adjacency[v]:
            if neighbor not in visited:
                w = edge_weights[(v, neighbor)]
                heapq.heappush(min_heap, (w, v, neighbor))
    
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