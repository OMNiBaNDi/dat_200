

#Iterative solution to selectionSort

def selectionSort_iterative(arr):
    #loop to iterate over the array elements
    for i in range(len(arr)):
        #set min_index equal to the first unsorted element
        min_index = i
        #iterate over unsorted sublist
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


arr = [7, 5, 4, 2, 3, 1]


#Recursive solution to selectionSort

def selectionSort_recursive(arr, n):
    # Base case: if the list is empty or contains a single element
    if n <= 1:
        return arr

    # Find the minimum element in the unsorted list
    min_index = 0
    for i in range(1, n):
        if arr[i] < arr[min_index]:
            min_index = i

    # Swap the minimum element with the first element in the unsorted list
    arr[0], arr[min_index] = arr[min_index], arr[0]

    # Sort the remaining n-1 elements and merge the result with the first element
    arr[1:] = selectionSort_recursive(arr[1:], n - 1)

    return arr  # Return the sorted array

# Example usage
arr = [64, 25, 12, 22, 11, 66, 32, 10, 4, 1, 6, 7]
sorted_arr = selectionSort_recursive(arr, len(arr))
print(sorted_arr)
