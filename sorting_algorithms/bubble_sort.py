#Bubble sort iterative solution
"""
def bubble_sort_ite(arr):
    for i in range(len(arr) - 1):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        print("pass number", i, arr)

arr = [9, 7, 8, 2]
print(arr)
print(bubble_sort_ite(arr))
"""

#Bubble sort recursive solution
#Time complexity: best case O(n), average O(n^2), worst case O(n^2)


def bubble_sort_recursive(arr, n):
    #base case
    if n <= 1:
        return
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    bubble_sort_recursive(arr, n - 1)

arr = [9, 7, 8, 2, 6, 3, 1, 5]
bubble_sort_recursive(arr, 8)
print("sorted array: ", arr)