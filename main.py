from random import random
from Selection_Sort.selection_sort import selection_sort 
from Bubble_Sort.bubble_sort import bubble_sort
from Merge_Sort.merge_sort import merge_sort
from three_Way_Merge_Sort.three_way_merge_sort import three_way_merge_sort
from Quick_Sort.quick_sort import quick_sort
from time import time
import sys

def selectionSort(arr):
    print("================ Selection Sort ================")
    print("The Array Before Sorting:")
    print(arr)
    selection_sort(arr)
    print("The Array After Sorting:")
    print(arr)
    
def bubbleSort(arr):
    print("================ Bubble Sort ================")
    print("The Array Before Sorting:")
    print(arr)
    bubble_sort(arr)
    print("The Array After Sorting:")
    print(arr)
    
def mergeSort(arr):
    print("================ Merge Sort ================")
    print("The Array Before Sorting:")
    print(arr)
    merge_sort(arr)
    print("The Array After Sorting:")
    print(arr)
    
def threeWayMergeSort(arr):
    print("================ Three Way Merge Sort ================")
    print("The Array Before Sorting:")
    print(arr)
    three_way_merge_sort(arr)
    print("The Array After Sorting:")
    print(arr)

def quick_sort_main(arr):
    print("================ Quick Sort ================")
    print("The Array Before Sorting:")
    time_start=time()
    print(arr)
    quick_sort(arr,0, len(arr))
    time_took=time()-time_start
    print("The Array After Sorting:")
    print(arr)
    print("The process took: ",time_took)


if __name__ == "__main__":
    length=int(sys.argv[2])
    arr=[0]*length
    for i in range(length):
        arr[i]=int(random()*10000)
    
    if(sys.argv[1]=='-bubble'):
        selectionSort(arr)
    elif(sys.argv[1]=='-selection'):
        selectionSort(arr)
    elif(sys.argv[1]=='-merge'):
        mergeSort(arr)
    elif(sys.argv[1]=='-3waymerge'):
        threeWayMergeSort(arr)
    elif(sys.argv[1]=='-quick'):
        quick_sort_main(arr)
        
