"""
- Based on the divide and conquer approach where an array is divided into subarrays by selecting a pivot element.
- While dividing the array the pivot element should be positioned in such a way that elements less than pivot are kept on the left,
and elements greater than the pivot are on the right side.


How to choose Pivot:
- First or last element: Selecting first or last element in the array is straightforward. This is the default pivot choice in many 
quicksort implementations, however it can lead to poor performance if the input is already sorted or nearly sorted.

- Random pivot: Choosing a random element as the pivot is simple and effective. This approach helps avoid the worst case scenarios
that can occur with deterministic choices. Random pivots typically lead to more balanced partitions and better average-case performance.

- Median of Medians: More advanced pivot selection strategy. Involves dividing the array into smaller groups, finding the median of, 
each group, then recursively selecting the median of the medians as pivot. Guarantees good pivot selection, but has higher constant
factor and is typically used for larger datasets. 

One popular method is Median-of-Three:
- Look at first, middle and last element, sort them and choose the median of them.
"""

def partition(arr, left, right):
    i = left
    j = right
    pivot = arr[right]

    #This loop runs until i and j crossover and swaps small elements to the left and bigger elements to the right
    while i < j:
        #moves i to the right until we find an element bigger than or equal to pivot
        while i < right and arr[i] < pivot:
            i += 1
        #moves j to the left until we find an element smaller than pivot
        while j > left and arr[j] >= pivot:
            j -= 1
        #if i and j have not crossed, swap the elements at i and j
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # After the loops, i is the position where the pivot should go.
    # If the element at i is greater than the pivot, swap it with the pivot
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i


def quicksort(arr, left, right):
    #base case checks if subarray has more than one element
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

    
arr = [33, 65, 55, 71, 29, 65, 4, 18, 54, 32, 1, 4, 99, 65]
quicksort(arr, 0, len(arr) - 1)
print(arr)  # Output: [4, 10, 18, 23, 29, 33, 55, 71]