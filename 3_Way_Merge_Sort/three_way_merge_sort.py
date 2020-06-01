
"""This function will handle the splitting of the data into 3 pieces
    The base case for the recursion to stop is if the length of the array is less than 3.
    In normal merge sort since we split by 2 the base case becomes if the array is less than 2.
    
"""
def three_way_merge_sort(a):
    if(len(a)>1):
        f_third=int(len(a)//3)
        s_third=(f_third*2)+1
        L=a[:f_third]
        M=a[f_third:s_third]
        R=a[s_third:]
        three_way_merge_sort(L)
        three_way_merge_sort(M)
        three_way_merge_sort(R)
        
        merge(a,L,M,R)

    """The merge function will handle the three way merge. This is more intense than the regualr merge sort
        due to the introduction of a third list/splice. The logic is as follows: compare the three splices and order
        them from lowest to highest once one of them runs out you then compare the other two and finally fill in the leftover.
    """
def merge(arr,L,M,R):
    i,j,k,l=0,0,0,0
    temp=[0]*(len(L)+len(R)+len(M))
    while(i<len(L) and j<len(M) and k<len(R)):
        if(L[i]<M[j] and L[i]<R[k]):
            temp[l]=L[i]
            i+=1
            l+=1
        elif(M[j]<R[k]):
            temp[l]=M[j]
            l+=1
            j+=1
        else:
            temp[l]=R[k]
            k+=1
            l+=1
    
    #Compare the left over first and second slices
    while(i<len(L) and j<len(M)):
        if(L[i]<M[j]):
            temp[l]=L[i]
            i+=1
            l+=1
        else:
            temp[l]=M[j]
            j+=1
            l+=1
    
    #Compare the leftovers from the second and third slices
    while(j<len(M)and k<len(R)):
        if(M[j]<R[k]):
            temp[l]=M[j]
            j+=1
            l+=1
        else:
            temp[l]=R[k]
            k+=1
            l+=1 
    #Compare the left over from the first and third slices
    while(i<len(L)and k<len(R)):
        if(L[i]<R[k]):
            temp[l]=L[i]
            i+=1
            l+=1
        else:
            temp[l]=R[k]
            k+=1
            l+=1
    #fill in the leftovers starting from the left segement (will always be smaller)
    while(i<len(L)):
        temp[l]=L[i]
        i+=1
        l+=1
    #fill in the leftovers starting from the middle segement
    while(j<len(M)):
        temp[l]=M[j]
        j+=1
        l+=1
    #fill in the leftovers starting from the left segement (will always be smaller)
    while(k<len(R)):
        temp[l]=R[k]
        k+=1
        l+=1
    for f in range(len(temp)):
        arr[f]=temp[f]