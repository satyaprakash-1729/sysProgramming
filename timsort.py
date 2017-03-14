import random as rn

def merge(arr,brr):
    i=0
    j=0
    finalArr = []
    while i<len(arr) and j<len(brr):
        while j<len(brr) and i<len(arr) and arr[i]<=brr[j]:
            finalArr.append(arr[i])
            i+=1
        while j<len(brr) and i<len(arr) and brr[j]<=arr[i]:
            finalArr.append(brr[j])
            j+=1
    while i<len(arr):
            finalArr.append(arr[i])
            i+=1
    while j<len(brr):
            finalArr.append(brr[j])
            j+=1
    return finalArr

def mergeSort(arr,n):
    if(n<=100):
        return sorted(arr)
    else:
        first = arr[:n/2]
        second = arr[n/2:]
        a = mergeSort(first,len(first))
        b = mergeSort(second,len(second))
        return merge(a,b)

def inPlaceQuickSort(A,start,end):
    if start<end:
        pivot=rn.randint(start,end)
        temp=A[end]
        A[end]=A[pivot]
        A[pivot]=temp
        
        p=inPlacePartition(A,start,end)
        inPlaceQuickSort(A,start,p-1)
        inPlaceQuickSort(A,p+1,end)


def inPlacePartition(A,start,end):
    pivot=rn.randint(start,end)
    temp=A[end]
    A[end]=A[pivot]
    A[pivot]=temp
    newPivotIndex=start-1
    for index in xrange(start,end):
        if A[index]<A[end]:#check if current val is less than pivot value
            newPivotIndex=newPivotIndex+1
            temp=A[newPivotIndex]
            A[newPivotIndex]=A[index]
            A[index]=temp
    temp=A[newPivotIndex+1]
    A[newPivotIndex+1]=A[end]
    A[end]=temp
    return newPivotIndex+1

def QuickSort(arr):
    inPlaceQuickSort(arr,0,len(arr)-1)
    return arr


n = int(raw_input())
arr = [rn.randint(0,1000) for _ in range(n)]

sorted(arr)