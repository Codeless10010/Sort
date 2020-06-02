# Name: Intro Sort
# Original Author: J. W. J. Williams
# Time Comlexity:
#   Best Case:O(n)
#   Average Case: O(nlogn)
#   Worst Case: O(nlogn)
# Space Complexity: O(n)
# Logic: Create a max heap (tree with root as the largest element). Then swap the root with last element and consider it sorted. Repeat these steps until completed.

def heap_sort(arr):
    for i in range(len(arr)//2-1,-1,-1):
        heapify(arr,len(arr),i)
        
    print(arr)
    for i in range(len(arr)-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

def heapify(arr,length,r):
    left_child=r*2+1
    right_child=r*2+2
    largest=r
    if(left_child<length and arr[largest]<arr[left_child]):
        largest=left_child
    if(right_child<length and arr[largest]<arr[right_child]):
        largest=right_child
    if(largest!=r):
        arr[r],arr[largest]=arr[largest],arr[r]
        heapify(arr,length,largest)
    