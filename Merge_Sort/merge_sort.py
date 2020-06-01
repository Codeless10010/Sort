


# This is the main crux of the merge sort algorithm 
#     Given a start and an end. The merge will attempt to
#     merge the two sides while maintaining ascention order
# 
def merge(arr,L,R):
    temp=[0]*(len(R)+len(L))
    l,r,k=0,0,0
    while(l<len(L) and r<len(R)):
        if(L[l]<R[r]):
            temp[k]=L[l]
            l+=1
            k+=1
        else:
            temp[k]=R[r]
            r+=1
            k+=1
    while(l<len(L)):
        temp[k]=L[l]
        k+=1
        l+=1
    while(r<len(R)):
        temp[k]=R[r]
        k+=1
        r+=1
    for i in range(len(temp)):
        arr[i]=temp[i]
        
        
        

    """Function used to break down the array into small chunks
    """
def mergeSort(arr):
    if len(arr)>1:
        middle=int(len(arr)//2)
        L=arr[:middle]
        R=arr[middle:]
        mergeSort(L)
        mergeSort(R)
        merge(arr,L,R)
