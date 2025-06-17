import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import sorting_algorithms as sorting
import Linked_list
import binarysearchtree
from io import StringIO
import random
import time
import HTLL
import HTOA
import red_black_tree


def Ds_benchmark(input_sizes):
    LL={'LL': {}, 'BST': {}, 'Arr': {},'RBT': {}}
    operations=['insert','search','delete']

    for input in input_sizes:
        samples=[]
        for DS in LL.keys():
            for operation in operations:
                for k in range(10):
                    random_list=[random.randint(1,input) for x in range(input)]
                    
                    match DS:
                        case 'LL':
                            match operation:
                                case 'insert':
                                    start=time.time()
                                    L=Linked_list.LinkedList()
                                    for val in random_list:
                                        L.insert_at_head(val)
                                    end=time.time()
                                case 'search':
                                    L=Linked_list.LinkedList()
                                    for val in random_list:
                                        L.insert_at_head(val)
                                    start=time.time()
                                    random.shuffle(random_list)
                                    for val in random_list:
                                        L.search(val)
                                    end=time.time()
                                case 'delete':
                                    L=HTLL.LinkedList()
                                    for val in random_list:
                                        L.insert_at_head(val)
                                    random.shuffle(random_list)
                                    start=time.time()
                                    for val in random_list:
                                        L.delete(val)
                                    end=time.time()

                        case 'BST':
                            match operation:
                                case 'insert':
                                    start=time.time()
                                    bst=binarysearchtree.BinarySearchTree()
                                    for val in random_list:
                                        bst.insert(val)
                                    end=time.time()
                                case 'search':
                                    bst=binarysearchtree.BinarySearchTree()
                                    for val in random_list:
                                        bst.insert(val)
                                    start=time.time()
                                    random.shuffle(random_list)
                                    for val in random_list:
                                        bst.search(val)
                                    end=time.time()
                                case 'delete':
                                    bst=binarysearchtree.BinarySearchTree()
                                    for val in random_list:
                                        bst.insert(val)
                                    start=time.time()
                                    random.shuffle(random_list)
                                    for val in random_list:
                                        bst.delete(val)
                                    end=time.time()

                        case 'Arr':
                            match operation:
                                case 'insert':
                                    new=[]
                                    start=time.time()
                                    for val in random_list:
                                        new.append(val)
                                    end=time.time()
                                case 'search':
                                    new=[]
                                    for val in random_list:
                                        new.append(val)
                                    random.shuffle(new)
                                    start=time.time()
                                    for val_to_search in random_list:
                                        for val in new:
                                            if val == val_to_search:
                                                break
                                    end=time.time()
                                case 'delete':
                                    new=[]
                                    for val in random_list:
                                        new.append(val)
                                    random.shuffle(new)
                                    start=time.time()
                                    for val_to_delete in random_list:
                                        i=new.index(val_to_delete)
                                        new.pop(i)
                                    end=time.time()
                        case 'RBT':
                              match operation:
                                case 'insert':
                                    rbt=red_black_tree.RedBlackTree()
                                    start=time.time()
                                    for val in random_list:
                                        rbt.insert(val)
                                    end=time.time()
                                case 'search':
                                    rbt=red_black_tree.RedBlackTree()
                                    for val in random_list:
                                        rbt.insert(val)
                                    start=time.time()
                                    for val_to_search in random_list:
                                        rbt.search(val_to_search)
                                    end=time.time()

                    samples.append(end-start)

                if operation in LL[DS].keys():
                    LL[DS][operation].append(sum(samples)/len(samples))
                else:    
                    LL[DS][operation]=[sum(samples)/len(samples)]
    return LL
    
def hashtable_benchmark(size):
    dizionario_u={'HTuniversale': [], 'HTdoppiohash': [], 'HTaperto':[]}
    dizionario_s={'HTuniversale': [], 'HTdoppiohash': [], 'HTaperto':[]}
    for s in size:
        hash_tb_universale=HTLL.HashTableLl(100)
        hash_tb_aperto_d=HTOA.HashTableDoubleHashing(s*2)
        hash_tb_aperto_l=HTOA.HashTableLinearProbing(s*2)
        elements=[random.randint(1,s) for x in range(s)]
        for e in elements:
            hash_tb_universale.insert(e)
            hash_tb_aperto_d.insert(e)
            hash_tb_aperto_l.insert(e)
        never_seen=[]
        while len(never_seen)<s:
            n=random.randint(1,2000)
            if n in elements:
                pass
            else:
                never_seen.append(n)

        start=time.time()
        for i in never_seen:
            hash_tb_universale.search(i)
        end=time.time()
        dizionario_u['HTuniversale'].append(end-start)

        start=time.time()
        for i in elements:
            hash_tb_universale.search(i)
        end=time.time()
        dizionario_s['HTuniversale'].append(end-start)

        start=time.time()
        for i in never_seen:
            hash_tb_aperto_d.search(i)
        end=time.time()
        dizionario_u['HTdoppiohash'].append(end-start)
        
        start=time.time()
        for i in elements:
            hash_tb_aperto_d.search(i)
        end=time.time()
        dizionario_s['HTdoppiohash'].append(end-start)

        start=time.time()
        for i in never_seen:
            hash_tb_aperto_l.search(i)
        end=time.time()
        dizionario_u['HTaperto'].append(end-start)

        start=time.time()
        for i in elements:
            hash_tb_aperto_l.search(i)
        end=time.time()
        dizionario_s['HTaperto'].append(end-start)

    return (dizionario_u,dizionario_s)

# =================== INTERFACE  ===================

def main():
    st.sidebar.title("📋 Main Menu")
    
    section = st.sidebar.selectbox(
        "Select Section:",
        [
            "Sorting Algorithms", 
            "Linked Lists",
            "Binary Search Trees (BST)",
            "Data Structures Performance Test",
            "Hash Tables",
            "Hash Tables Performance Test",
            "Red-Black Tree",
            "Graphs"
        ]
    )

    if section == "Sorting Algorithms":
        show_sorting_section()
    elif section == "Linked Lists":
        show_linked_list_section()
    elif section == "Binary Search Trees (BST)":
        pass
    elif section == "Data Structures Performance Test":
        show_datastructures_benchmark()
    elif section == "Hash Tables":
        pass
    elif section == "Hash Tables Performance Test":
        show_hashtables_benchmark()
    elif section == "Red-Black Tree":
        pass
    elif section == "Graphs":
        pass

def show_sorting_section():
    st.header("🔄 Sorting Algorithms")
    
    st.subheader("Apply a Sorting Algorithm")
    
    col1, col2 = st.columns([1, 2])
        
    with col1:
            # scelta algoritmo
            algorithm = st.selectbox(
                "Select algorithm:",
                ["MergeSort", "QuickSort", "InsertionSort","BinaryInsertionSort" , "BubbleSort", "ShortBubbleSort", "CountingSort"]
            )
            
            # metodo di input
            input_method = st.radio(
                "Input method:",
                ["📝 Manual input", "📁 File upload", "🎲 Random generation"]
            )
        
    with col2:
            if input_method == "📝 Manual input":
                input_text = st.text_area(
                    "Enter numbers separated by comma:",
                    value="64, 340, 25, 12, 22, 11, 90",
                    height=100
                )
                if st.button("Sort", type="primary"):
                    try:
                        values = [int(x.strip()) for x in input_text.split(',')]
                        start_time = time.time()
                        sorted_values = apply_sorting_algorithm(algorithm, values.copy())
                        exec_time = time.time() - start_time
                        
                        col1, col2 = st.columns(2)
                        col1.write("**Original array:**")
                        col1.code(str(values))
                        col2.write("**Sorted array:**")
                        col2.code(str(sorted_values))
                        
                        st.info(f"⏱️ **Execution time**: {exec_time:.6f} seconds")
                    except ValueError:
                        st.error("Enter valid numbers separated by comma")
            
            elif input_method == "📁 File upload":
                '''da implementare'''

            elif input_method == "🎲 Random generation":
                size = st.number_input("Array size:", min_value=1, value=20, step=1, format="%d")
                
                if st.button("Generate and Sort"):
                    values = [random.randint(1, 100) for _ in range(size)]
                    start_time = time.time()
                    sorted_values = apply_sorting_algorithm(algorithm, values.copy())
                    exec_time = time.time() - start_time

                    col1, col2 = st.columns(2)
                    col1.write("**Original array:**")
                    col1.code(str(values))
                    col2.write("**Sorted array:**")
                    col2.code(str(sorted_values))

                    st.info(f"⏱️ **Execution time**: {exec_time:.6f} seconds")
    
    st.markdown("---")
    
    # =============== PERFORMANCE TESTING ===============
    st.subheader("Performance Testing")
    
    input_sizes = [10, 100, 1000, 10000]
    n_of_runs = 10
    
    if 'performance_cancelled' not in st.session_state:
        st.session_state.performance_cancelled = False
    
    # Cache
    cache_key = f"sorting_perf_{'_'.join(map(str, sorted(input_sizes)))}_{n_of_runs}"
  
    if cache_key not in st.session_state and not st.session_state.performance_cancelled:

        loading_container = st.container()
        
        with loading_container:
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.info("⏳ Loading performance test... This may take a few minutes.")
            
            with col2:
                if st.button("❌ Cancel", type="secondary"):
                    st.session_state.performance_cancelled = True
                    st.rerun()
        
        if not st.session_state.performance_cancelled:
            try:
                with st.spinner("Running performance test..."):
                    def check_cancelled():
                        return st.session_state.get('performance_cancelled', False)
                    
                    # Chiama performance_test con il callback
                    results = sorting.performance_test(
                        tuple(input_sizes), 
                        n_of_runs,
                        cancel_check_callback=check_cancelled
                    )

                if results is None:
                    st.session_state.performance_cancelled = True
                    loading_container.empty()
                    st.rerun()

                else:
                    # Salva in cache
                    st.session_state[cache_key] = results
                    
                    loading_container.empty()
                    st.success("Performance test completed!")
                
            except Exception as e:
                loading_container.empty()
                st.error(f"Error during test: {str(e)}")
                return
    
    elif st.session_state.performance_cancelled:
        st.warning("⚠️ Performance test was cancelled")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Restart Test", type="primary"):
                st.session_state.performance_cancelled = False
                if cache_key in st.session_state:
                    del st.session_state[cache_key]
                st.rerun()
        
        with col2:
            if cache_key in st.session_state:
                if st.button("Show Cached Results"):
                    st.session_state.performance_cancelled = False
                    st.rerun()
        st.stop()
    
    # Mostra risultati (da cache se sono salvati)
    if cache_key in st.session_state:
        results = st.session_state[cache_key]
        
        st.subheader("Table of results (avg time in seconds)")
        st.write("Sizes tested:", input_sizes)
        st.write("Average calculated on:", n_of_runs, "runs")

        # Create a df to show the results
        df = pd.DataFrame(results, index=input_sizes)
        df.index.name = "Input size"
        st.dataframe(df)
                    
        # Plot the results
        fig, ax = plt.subplots(figsize=(8, 5))
                    
        for algo_name, times in results.items():
           ax.plot(input_sizes, times, marker="o", label=algo_name)

        ax.set_xlabel("Input size")
        ax.set_ylabel("Avg time (s)")
        ax.set_title("Sorting Algorithms Performance Comparison", fontsize=14, fontweight='bold')
        ax.legend()
        ax.grid(True)
                    
        st.pyplot(fig)
    
        if st.button("🔄 Run New Test"):
            if cache_key in st.session_state:
                del st.session_state[cache_key]
            st.session_state.performance_cancelled = False
            st.rerun()

def show_linked_list_section():
    st.header("📝 Linked Lists")
    
    if 'linked_list' not in st.session_state:
        st.session_state.linked_list = Linked_list.LinkedList()
    

    st.subheader("Linked List Operations")
        
        
    st.write("**Current List:**")
    if st.session_state.linked_list.head:
        st.code(str(st.session_state.linked_list))
    else:
        st.write("Empty list")

    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Insertion:**")
        new_value = st.number_input("Value to insert:", value=0)
        if st.button("Insert at head"):
            st.session_state.linked_list.insert_at_head(new_value)
            st.success(f"Value {new_value} inserted!")
        
    with col2:
        st.write("**Search:**")
        search_value = st.number_input("Value to search:", value=0, key="search")
        if st.button("Search"):
            result = st.session_state.linked_list.search(search_value)
            if result:
                st.success(f"✅ Value {search_value} found!")
            else:
                st.warning(f"❌ Value {search_value} not found.")
        
        
    st.subheader("Operations")
    col1, col2 = st.columns(2)
        
    with col1:
        if st.button("Minimum"):
            min_val = st.session_state.linked_list.minimum()
            if min_val is not None:
                st.metric("Minimum", min_val)
            else:
                st.write("Empty list")
        
    with col2:
        if st.button("Maximum"):
            max_val = st.session_state.linked_list.maximum()
            if max_val is not None:
                st.metric("Maximum", max_val)
            else:
                st.write("Empty list")
        
    with col1:
        pred_value = st.number_input("Predecessor of:", value=0, key="pred")
        if st.button("Predecessor"):
            pred = st.session_state.linked_list.predecessor(pred_value)
            if pred is not None:
                st.write(f"Predecessor: {pred}")
            else:
                st.write("No predecessor")
        
    with col2:
        succ_value = st.number_input("Successor of:", value=0, key="succ")
        if st.button("Successor"):
            succ = st.session_state.linked_list.successor(succ_value)
            if succ is not None:
                st.write(f"Successor: {succ.value}")
            else:
                st.write("No successor")

def show_datastructures_benchmark():
    st.header("📊 Data Structures Performance Test")
    
    st.write("Performance comparison between **Arrays**, **Linked Lists**, **BST** and **Red-Black Tree**")
    
    col1, col2 = st.columns(2)
    with col1:
        input_sizes = st.multiselect(
            "Sizes to test:",
            [10, 100, 1000, 2000, 3000, 4000, 5000, 10000],
            default=[10, 100, 1000, 10000]
        )
    with col2:
        st.info("📝 Tests performed: **Insert**, **Search**, **Delete**\n\n⏱️ **10 runs** for each operation")
    
    if st.button("🚀 Run Complete Benchmark", type="primary"):
        if not input_sizes:
            st.error("Select at least one size!")
        else:
            with st.spinner("⏳ Running benchmark... This may take several minutes."):
                Performance = Ds_benchmark(tuple(input_sizes))
                
                operations = ['insert', 'search', 'delete']
                for operation in operations:
                    st.subheader(f"📈 Performance: {operation.title()}")
                    
                    fig, ax = plt.subplots(figsize=(8, 5))

                    for DS in Performance.keys():
                        if DS == 'RBT' and operation == 'delete':
                            pass
                        else:
                            ax.plot(input_sizes, Performance[DS][operation], 
                                   marker='o', label=f'{DS}')
                    
                    ax.set_title(f'Performance {operation.title()}', fontsize=14, fontweight='bold')
                    ax.set_xlabel("Input size")
                    ax.set_ylabel("Average time (s)")
                    ax.legend()
                    ax.grid(True, alpha=0.3)
                    st.pyplot(fig)

def show_hashtables_benchmark():
    st.header("📈 Hash Tables Performance Test")
    
    st.write("Performance comparison between the **3 implementations** of hash table")
    
    col1, col2 = st.columns(2)
    with col1:
        input_size = st.multiselect(
            "Sizes to test:",
            [10, 100, 1000, 2000, 4000, 5000, 10000],
            default=[10, 100, 1000, 10000]
        )
    with col2:
        st.info("""
        📝 **Tests performed:**
        - **Unsuccessful** searches (non-existing elements)
        - **Successful** searches (existing elements)
        
        🔧 **Implementations tested:**
        - Universal Hash
        - Double Hashing (open addressing)  
        - Linear Probing (open addressing)
        """)
    
    if st.button("🚀 Run Hash Tables Benchmark", type="primary"):
        if not input_size:
            st.error("Select at least one size!")
        else:
            with st.spinner("⏳ Running hash tables performance test..."):
                ht_performance_unsuccessful, ht_performance_successful = hashtable_benchmark(input_size)
            
                st.subheader('🔍 Unsuccessful Searches')
                fig, ax = plt.subplots(figsize=(8, 5))

                for ht in ht_performance_unsuccessful.keys():
                    ax.plot(input_size, ht_performance_unsuccessful[ht], 
                           marker='o', label=ht)
                
                ax.set_title('Unsuccessful Searches', fontsize=14, fontweight='bold')
                ax.set_xlabel("Input Size", fontsize=12)
                ax.set_ylabel("Average Time (s)", fontsize=12)
                ax.legend(fontsize=10)
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)
                
         
                st.subheader('✅ Successful Searches')
                fig, ax = plt.subplots(figsize=(12, 6))
                
                for ht in ht_performance_successful.keys():
                    ax.plot(input_size, ht_performance_successful[ht], 
                           marker='o', label=ht)
                
                ax.set_title('Successful Searches', fontsize=14, fontweight='bold')
                ax.set_xlabel("Input Size", fontsize=12)
                ax.set_ylabel("Average Time (s)", fontsize=12)
                ax.legend(fontsize=10)
                ax.grid(True, alpha=0.3)
                st.pyplot(fig)

def apply_sorting_algorithm(algorithm, values):
    """Apply the selected sorting algorithm"""
    if algorithm == "MergeSort":
        return sorting.merge_sort(values)
    elif algorithm == "QuickSort":
        sorting.quick_sort(values, 0, len(values) - 1)
        return values
    elif algorithm == "InsertionSort":
        return sorting.insertion_sort(values)
    elif algorithm == "BinaryInsertionSort":
        return sorting.BinaryInsertionSort(values)
    elif algorithm == "BubbleSort":
        return sorting.BubbleSort(values)
    elif algorithm == "ShortBubbleSort":
        return sorting.ShortBubbleSort(values)
    elif algorithm == "CountingSort":
        return sorting.CountingSort(values)
    return values


if __name__ == "__main__":
    main()