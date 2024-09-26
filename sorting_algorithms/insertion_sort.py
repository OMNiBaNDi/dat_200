#Insertion sort iterative solution

#Efficient for small datasets. Impractical for larger ones due to quadratic time complexity.

#Asymptotic analysis: Best case O(n), average case O(n^2), Worst case O(n^2)

def insertion_sort_iterative(arr):
    #start from index 1, as arr[0] is always sorted
    for i in range(1, len(arr)):
        key = arr[i]
        #move elements of arr[0...i-1], that are greater than key,
        #to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        #finally place the current element at its correct position
        arr[j+1] = key
        print(arr)

arr = [9, 7, 8, 2]

#insertion_sort_iterative(arr)

#RECURSIVE SOLUTION

def recursive_insertion_sort(arr, n):
    #base case: if there is only one element or the list is empty
    if n <= 1:
        return
    
    #sort the first n-1 elements
    recursive_insertion_sort(arr, n - 1)

    #Insert the last element into its correct position in the sorted part of the list
    key = arr[n - 1]
    j = n - 2
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
    print(arr)

print("original array:", arr)
recursive_insertion_sort(arr, len(arr))
print("sorted array:", arr)