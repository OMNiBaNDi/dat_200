#Linear search - Time complexity, best case O(1), worst case O(n). 
#Usage: used in small to medium sized datasets where the cost of searching is not a critical factor.

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1