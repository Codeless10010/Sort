from random import random
from three_way_merge_sort import three_way_merge_sort
import sys

length=int(sys.argv[1])
arr=[0]*length
for i in range(length):
    arr[i]=int(random()*10000)
three_way_merge_sort(arr)
print(arr)
    