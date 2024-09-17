#Insertion sort iterative solution

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

insertion_sort_iterative(arr)