# Bubble-repository

Interactive platform for implementing and benchmarking fundamental algorithms and data structures. Built with Python and Streamlit for academic coursework.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

Open browser at `http://localhost:8501`


### 🔄 Sorting Algorithms
- **Algorithms**: MergeSort, QuickSort, InsertionSort, BubbleSort, CountingSort
- **Interactive testing** with manual input, file upload, or random generation
- **Automatic performance comparison** with charts and tables

### 📊 Data Structures
- **Linked Lists** - Complete operations (insert, search, delete, min, max, predecessor, successor)
- **Binary Search Trees** - All BST operations with visualization
- **Red-Black Trees** - Self-balancing tree implementation
- **Hash Tables** - Three implementations:
  - Universal hashing with chaining
  - Double hashing (open addressing)
  - Linear probing (open addressing)
- **Performance benchmarking** across all structures

### 🕸️ Graphs
- **Types**: Directed/Undirected, Weighted/Unweighted
- **Creation methods**: Manual input, random generation, file upload
- **Representations**: Adjacency lists and adjacency matrix
- **Algorithms**: BFS, DFS, Dijkstra, Kruskal, Topological Sort, Connected Components

## Implementation Details

### Sorting Algorithms Performance Test
- **Input sizes**: 10, 100, 1,000, 10,000 elements
- **Runs**: 10 iterations per algorithm per size
- **Output**: Comparative charts and statistical analysis

### Data Structures Benchmark
- **Operations tested**: Insert, Search, Delete
- **Structures compared**: Arrays, Linked Lists, BST, Red-Black Trees
- **Metrics**: Average execution time across multiple runs

### Graph Algorithms
- **BFS/DFS**: Complete traversal with distance/time tracking
- **Dijkstra**: Shortest paths in weighted graphs
- **Kruskal**: Minimum spanning tree for undirected weighted graphs
- **Topological Sort**: Linear ordering for directed acyclic graphs

## Requirements

- Python 3.8+
- Streamlit
- Pandas
- Matplotlib
- SymPy

## Academic Use

Developed for university coursework on algorithms and data structures. Implements all required functionality as specified in project guidelines:

- Complete sorting algorithm implementations with performance analysis
- Full data structure operations with comparative benchmarking
- Comprehensive graph algorithms for different graph types
- Interactive interface for testing and visualization

---