"""
Merge sort is a widely used sorting algorithm and uses the divide and conquer principle.

1. Divide: The unsorted array is divided into two halves, roughly in equal size.
2. Conquer: Each of the halves are recurcively sorted. This process continues until the subarrays
are small enough to be sorted easily(typically when they contain just one or zero elements).
3. Merge: The sorted subarrays are then merged back together. During the merge operation, the elements
from both subarrays are compared, and the smaller is placed in the final sorted array. This process
continues until all elements are merged into a single sorted array.

Time complexity:
Best = Average = Worst = O(n log n)
"""

def merge(array, p, q, r):
    #Create temp arrays
    L = array[p:q+1]
    R = array[q+1:r+1]
    i = j = 0
    k = p

    #Merge two halves back into array[p..r]
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    #Copy the remaining elements of L if there are any
    while i < len(L):
        array[k] = L[i]
        i += 1
        k += 1

    #Copy the remaining elements of R if there are any
    while j < len(R):
        array[k] = R[j]
        j += 1
        k += 1

def mergeSort(array, p, r):
    if p < r:

        q = (p+r) // 2

        mergeSort(array, p, q)
        mergeSort(array, q+1, r)
        merge(array, p, q, r)

arr = [12, 11, 13, 5, 6, 7, 54, 3, 22, 89]
mergeSort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)
