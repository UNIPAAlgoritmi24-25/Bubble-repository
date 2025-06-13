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
def Ds_benchmark(input_sizes):
    LL={'LL': {}, 'BST': {}, 'Arr': {}}
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

                    samples.append(end-start)

                if operation in LL[DS].keys():
                    LL[DS][operation].append(sum(samples)/len(samples))
                        
                else:    
                    LL[DS][operation]=[sum(samples)/len(samples)]
    return LL
            
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
    '''
    file=st.file_uploader('inserisci file txt')
    if st.button('Carica'):
        data = StringIO(file.getvalue().decode("utf-8"))
        string_data=data.read()
        to_use=list(string_data.split(','))
    '''
    Performance=Ds_benchmark(input_sizes)
    print(Performance)


if __name__ == "__main__":
    main()
