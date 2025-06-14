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
                                    start=time.time()


                              
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
        



def main():

    t_1 = "Comparing sorting algorithms performances"
    st.title(t_1)

    input_sizes = (10, 100, 1000)
    n_of_runs = 10

    # Performance calculation
    with st.spinner("Calculating..."):
        results = sorting.performance_test(input_sizes, n_of_runs)

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
    ax.set_title(t_1)
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
   
    st.subheader("Datastructures benchmark")

    input_sizes=(10,100,1000,2000,3000,4000)
    Performance=Ds_benchmark(input_sizes)

    operations=['insert','search','delete']
    for operation in operations:
        fig, ax = plt.subplots(figsize=(8, 5))

        for DS in Performance.keys():
            if DS == 'RBT' and operation=='delete':
                pass
            else:
                ax.plot(input_sizes,Performance[DS][operation], marker='o',label=f'{DS}')
        ax.set_title(operation)
        ax.set_xlabel("Input size")
        ax.set_ylabel("Avg time (s)")
        ax.legend()
        st.pyplot(fig)
    
    input_size=[10,100,1000,2000,4000]
    ht_performance_unsuccesfull, ht_performance_succesfull=hashtable_benchmark(input_size)
    

    st.subheader('Hash table benchmarks')

    fig, ax=plt.subplots(figsize=(8,5))
    for ht in ht_performance_unsuccesfull.keys():
        ax.plot(input_size,ht_performance_unsuccesfull[ht], marker='o', label=ht)

    ax.set_title('Unsuccesful search')
    ax.set_xlabel("Input size")
    ax.set_ylabel("Avg time (s)")
    ax.legend()
    st.pyplot(fig)

    fig, ax=plt.subplots(figsize=(8,5))
    for ht in ht_performance_succesfull.keys():
        ax.plot(input_size,ht_performance_succesfull[ht], marker='o', label=ht)
        
    ax.set_title('succesful search')
    ax.set_xlabel("Input size")
    ax.set_ylabel("Avg time (s)")
    ax.legend()
    st.pyplot(fig)





if __name__ == "__main__":
    main()
