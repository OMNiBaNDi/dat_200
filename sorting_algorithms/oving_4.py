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
    
    # Print the array state after partitioning
    print(f"Pivot {pivot} at index {i}, Array after partition: {arr}")

    return i


def quicksort(arr, left, right):
    #base case checks if subarray has more than one element
    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

arr = [-20, -16, 8, -3, 9, 14, 1, -8, 17, 5]
print(f"Initial array: {arr}")
quicksort(arr, 0, len(arr) - 1)
print(f"Sorted array: {arr}")