from random import random
from Selection_Sort.selection_sort import selection_sort 
import sys

length=int(sys.argv[1])
arr=[0]*length
for i in range(length):
    arr[i]=int(random()*10000)
print("The Array Before Sorting:")
print(arr)
selection_sort(arr)
print("The Array After Sorting:")
print(arr)
    