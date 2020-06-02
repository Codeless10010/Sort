# Name: Quick Sort
# Original Author: Tony Hoare
# Time Comlexity:
#   Best Case:O(n)
#   Average Case: O(nlogn)
#   Worst Case: O(n^2)
# Space Complexity: O(n)
# Logic: Choose a pivot number. partion the rest of the array as either less than the pivot or greate than the pivot. Recursively apply the steps before to the sub arrays.


def partition(arr,low,high):
    pivot=arr[high-1]
    j=low
    for i in range (low, high):
        if(arr[i]<pivot):
            arr[i],arr[j]=arr[j],arr[i]
            j+=1
    arr[j],arr[high-1]=arr[high-1],arr[j]
    return(j)
    

def quick_sort(arr,low,high):
    if(low<high):
        p_index=partition(arr,low,high)
        quick_sort(arr,low,p_index)
        quick_sort(arr,p_index+1,high)