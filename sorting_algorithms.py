"""
This module contains the implementation of various sorting algorithms.
"""

from random import randint
from random import shuffle
import time
import sys
from utils import random_list

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
    
    pivot = values[end]
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

# ---------------------------------------------------------------------#
# Binary Insertion sort
# ---------------------------------------------------------------------#

def bin_search(a, val, start, end):
    """
    The Binary Insertion Sort algorithm builds a sorted array by iteratively inserting
    each element into its correct position within the already sorted portion,
    using binary search to determine the insertion point.
    It improves upon standard Insertion Sort by reducing the number of comparisons needed.
    While it requires O(n log n) comparisons, the shifting operations still require O(n²) time.
    Time complexity: O(n²) in worst case, but with fewer comparisons than standard Insertion Sort.
    Particularly efficient when comparison operations are more expensive than shifting elements.
    """
    if start > end:
        return start
    mid = (start+end)//2
    if a[mid] <= val:
        return bin_search(a, val, mid+1, end)
    else:
        return bin_search(a, val, start, mid-1)

def BinaryInsertionSort(a):
    for i in range(1, len(a)):
        val = a[i]
        j = bin_search(a, val, 0, i-1)
        for t in range(i-1,j-1,-1):
            a[t+ 1] = a[t]    
        a[j] = val
    return a

# ---------------------------------------------------------------------#
# Bubble Sort
# ---------------------------------------------------------------------#

# ---------------------------------------------------------------------#
# Bubble sort
# ---------------------------------------------------------------------#

"""Bubble sort makes multiple passes through a list.
It compares adjacent elements and exchanges those that are out of order.
Each pass through the list places the next largest value in its proper place, relative to the unsorted
portion of the list.

We provide two implementations: one with a complexity of Θ(n²) (for the standard BubbleSort),
and another, that uses a flag and is sometimes referred to as "Short Bubble Sort",
with a complexity of  Ω(n) and O(n²)."""


def BubbleSort(array):
    n = len(array)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def ShortBubbleSort(array):
    exchange = True
    pass_num = len(array) - 1
    while pass_num > 0 and exchange:

        exchange = False
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                exchange = True
                array[i], array[i + 1] = array[i + 1], array[i]
        pass_num -= 1
    return array


# ---------------------------------------------------------------------#
# Counting sort
# ---------------------------------------------------------------------#



def CountingSort(array):
    """
    CountingSort is a non-comparative sorting algorithm that sorts elements by counting the occurrences of each value within a specified range.
    
    It then uses the cumulative frequency to determine the correct position of each element in the sorted output array.
    
    Algorithm time complexity: O(n + k), where n is the number of elements in the input array, and k is the range of values.
    
    Algorithm space complexity: O(n + k), due to the space required for the frequency array and the ordered output array.
    """
    min_value = min(array)
    max_value = max(array)
    n = len(array)
    range_values = (max_value - min_value) + 1
    frequency_array = [0] * range_values
    for element in array:
        frequency_array[element - min_value] += 1

    for i in range(1, len(frequency_array)):
        frequency_array[i] += frequency_array[i - 1]

    ordered_array = [0] * (n)
    for j in range(n - 1, -1, -1):
        element = array[j]
        pos = frequency_array[element - min_value] - 1
        ordered_array[pos] = element
        frequency_array[element - min_value] -= 1
    return ordered_array


# ---------------------------------------------------------------------#
# Performance test function
# ---------------------------------------------------------------------#


def performance_test(
    input_sizes: tuple[int], n_of_runs: int,
    cancel_check_callback=None 
) -> dict[str, list[float]]:
    """This functions allows to execute a performance test on the sorting
    algos of the module.
    Random lists will be generated on given input_sizes and the mean of
    n_of_run will be returned as the "score of the algoritm for that
    specific size.

    Args:
        input_sizes (tuple[int]): the sizes of the random lists used in
        tests.
        n_of_runs (int): the number of runs for input size.

    Returns:
        (dict[str, list[float]]): A dictionary containing a list of
        performances expressed in seconds for each sorting algorithm.
    """
    # set this high to avoid max recursion depth errors with recursive
    # algos like quicksort and mergesort
    sys.setrecursionlimit(999999)
    # generate random valuess to be sorted
    random_valuess = [random_list(size) for size in input_sizes]

    functions = [
        lambda x: quick_sort(x, 0, len(x) - 1),
        lambda x: merge_sort(x),
        lambda x: insertion_sort(x),
        lambda x: BinaryInsertionSort(x),
        lambda x: BubbleSort(x),
        lambda x: ShortBubbleSort(x),
        lambda x: CountingSort(x),
    ]

    # this will be used to list the performances of the algorithms
    performances = {
        "quick_sort": [],
        "merge_sort": [],
        "insertion_sort": [],
        "BinaryInsertionSort": [],
        "BubbleSort": [],
        "ShortBubbleSort": [],
        "CountingSort": [],
    }

    for values in random_valuess:
        for algorithm, name in zip(functions, performances.keys()):
            if cancel_check_callback and cancel_check_callback():
                return None
            time_total = 0

            for run in range(n_of_runs):
                if cancel_check_callback and cancel_check_callback():
                    return None
                
                # call the algo to sort the list and record the elapsed time
                shuffle(values)
                start_time = time.time()
                algorithm(values)
                end_time = time.time()

                time_total += end_time - start_time
                

            # append the mean time to algo's performance list
            time_mean = round(time_total / n_of_runs, 6)
            performances[name].append(time_mean)

    return performances

def carica_da_file(nome_file):
    """Carica una lista di numeri da un file di testo separati da una virgola"""
    values = []
    with open(nome_file, 'r') as file:
        contenuto = file.read()
        numeri = contenuto.split(',')
        
        for numero in numeri:
            numero = numero.strip()
            if numero:
                try:
                    if '.' in numero:
                        values.append(float(numero))
                    else:
                        values.append(int(numero))
                except ValueError:
                    pass 
    return values


if __name__ == "__main__":
    input_sizes = (10, 100, 1000)  # 10_000
    n_of_runs = 10

    performances = performance_test(input_sizes, n_of_runs)
    # output their performances
    print(
        *(
            f"{algo} performances: {performances}\n"
            for algo, performances in performances.items()
        )
    )

