# Selection sort is the basic sort with time complexity of O(n^2) overall. and space complexity of 1
# the basic idea of selection sort is to iterate through the whole array and find lowest number and store
# it in a sub array and remove the lowest element. Once completed you have a sorted list.

def selection_sort(array):
    temp=[0]*len(array)
    min,ind=array[0],0
    for i in range(len(temp)):
        min=array[0]
        ind=0
        for j in range(len(array)):
             if(array[j]<min):
                 ind=j
                 min=array[j]
        temp[i]=min
        del array[ind]

    
    for i in range(len(temp)):
        array.append(temp[i])
