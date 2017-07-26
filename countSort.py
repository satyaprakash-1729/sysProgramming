import os,sys,random

def countSort(dictionary,maxentry):
    count = [[] for _ in range(maxentry+1)]
    arr = dictionary.values()
    keys1 = dictionary.keys()
    for i in range(len(arr)):
        count[arr[i]].append(keys1[i])
    ansArr = []
    for i in range(1,len(count)+1):
        for j in count[-i]:
            ansArr.append((j,maxentry - i + 1))
    return ansArr

import random as rn

#n = int(raw_input())
#arr = [rn.randint(1,1000) for _ in range(n)]
#radixsort(arr)
#countSort(arr,1000)
print countSort({"a":34, "b": 12, "c":56}, 100)