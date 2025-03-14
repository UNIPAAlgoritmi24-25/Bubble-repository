"""Bubble sort makes multiple passes through a list. 
It compares adjacent elements and exchanges those that are out of order. 
Each pass through the list places the next largest value in its proper place, relative to the unsorted
portion of the list.

We provide two implementations: one with a complexity of Θ(n²) (for the standard BubbleSort), 
and another, that uses a flag and is sometimes referred to as "Short Bubble Sort", 
with a complexity of  Ω(n) and O(n²)."""


def BubbleSort (array):
    n = len (array)
    for i in range (n-1):
        for j in range (n-1-i):
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1],array[j]
    return array




def ShortBubbleSort (array):
    exchange = True
    pass_num = len(array)-1
    while pass_num >0 and exchange:
        exchange = False 
        for i in range (pass_num):
            if array[i] > array[i+1]:
                exchange = True
                array[i],array[i+1]=array[i+1],array[i]
        pass_num-=1
    return array