#Binary search: Time complexity, best case O(1), worst case O(log n).
#Usage: Binary search is highly efficient for large, sorted datasets, however it requires that the data be sorted beforehand.

#Iterative Binary search

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1