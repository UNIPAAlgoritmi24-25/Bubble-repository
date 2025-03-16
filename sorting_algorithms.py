"""
This module contains the implementation of various sorting algorithms.
"""

from random import randint
import time
import sys

# ---------------------------------------------------------------------#
# Merge sort
# ---------------------------------------------------------------------#


def merge(left, right, values):
    """
    The merge procedure in the merge sort algorithm
    merges two sorted arrays into one."""

    i_left = i_right = j = 0

    # comparing left and right sublists and merging them in values
    while i_left < len(left) and i_right < len(right):
        if left[i_left] <= right[i_right]:
            values[j] = left[i_left]
            i_left += 1
        else:
            values[j] = right[i_right]
            i_right += 1
        j += 1

    # Copy any remaining values
    while i_left < len(left):
        values[j] = left[i_left]
        i_left += 1
        j += 1

    while i_right < len(right):
        values[j] = right[i_right]
        i_right += 1
        j += 1

    return values


def merge_sort(values):
    """
    The Merge sort algorithm is a divide and impera algorithm that divides the
    array into two halves, sorts them and then merges them back together.
    It is a recursive, non in-place algorithm.
    Time complexity: O(n log n)
    """
    if len(values) <= 1:
        return values

    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    values = merge(left, right, values)

    return values


# ---------------------------------------------------------------------#
# Quick sort
# ---------------------------------------------------------------------#


def quick_sort(values, start, end):
    """
    The Quick sort algorithm is a divide and impera algorithm that use a
    pivot and move elements bigger than pivot to the right and  smaller than pivot to the left
    then recursively repeat the procedure for left and right sublists.
    Time complexity: O(n log n)
    """
    if start < end:
        q = partition(values, start, end)
        quick_sort(values, start, q - 1)
        quick_sort(values, q + 1, end)


def partition(values, start, end):
    """
    partion helper function that swap values and return the i'th
    index from where to start and where to end the next sublists division.
    """

    pivot = values[randint(start, end)]
    i = start - 1
    
    for j in range(start, end):
        if values[j] <= pivot:
            i += 1
            values[i], values[j] = values[j], values[i]
    # print(i+1)
    values[i + 1], values[end] = values[end], values[i + 1]
    return i + 1


# ---------------------------------------------------------------------#
# Insertion sort
# ---------------------------------------------------------------------#

def insertion_sort(values):
    """
    The Insertion sort algorithm builds a sorted array by iteratively inserting 
    each element into its correct position within the already sorted portion.
    It works similarly to how people sort playing cards in their hands.
    It is an in-place algorithm with simple implementation.
    Time complexity: O(n²) in worst case, but efficient for small or nearly sorted arrays.
   """
    n = len(values)
    for i in range(1, n):
        key = values[i]
        j = i - 1

        while j >= 0 and values[j] > key:
            values[j + 1] = values[j] 
            j = j - 1
        
        values[j + 1] = key
    return values

if __name__ == "__main__":

    # values = merge_sort(values)
    # quick_sort(values, 0, len(values)-1)
    # values = insertion_sort(values)

    input_lists=[[randint(0,100) for x in range(1000)], [randint(0,100) for x in range(4000)], [randint(0,100) for x in range(8000)], [randint(0,100) for x in range(12000)], [randint(0,100) for x in range(16000)], [randint(0,100) for x in range(20000)]]
    functions=[lambda x: quick_sort(x,0, len(x)-1), lambda x: merge_sort(x), lambda x: insertion_sort(x)]
    functions_name={'quick_sort': [], 'merge_sort': [], 'insertion_sort': []}
    
    sys.setrecursionlimit(999999)
    

    for values in input_lists:
        for algorithm,name in zip(functions, functions_name.keys()):
            mean_time=0
            for run in range(0,10):
                start_time=time.time()
                algorithm(values)
                end_time=time.time()
                mean_time=mean_time+((end_time-start_time)/10)
        
            functions_name[name].append(mean_time)

    print(functions_name)
          

    


  
 #quicksort(lista, 0, len(lista)-1)
 #mergesort(lista)
