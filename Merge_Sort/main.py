from random import random
from mergeSort import mergeSort
import sys

length=int(sys.argv[1])
arr=[0]*length
for i in range(length):
    arr[i]=int(random()*10000)
mergeSort(arr)
print(arr)
    