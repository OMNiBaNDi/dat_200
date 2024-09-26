"""
Shell sort builds on insertion sort to improve efficiency by reducing the number of comparisons'
and swaps.

The array is divided into subarrays based on the gap sequence. It does this by sorting subarrays
with a certain gap(or interval) and gradually reducing the gap.

There are several gap sequences.
1. Shells original sequence starts with n/2 and halves until reaching 1
2. Knuth Sequence starts with 1, 4, 13, 40, 121, ... calculated by the formula 3K+13K+1
3. Hibbards sequence: Uses powers of 2 minus 1(2^k - 1): 1, 2, 3, 7, 15, 31

BEST KNOWN GAP SEQUENCE: Knuth sequence, shell sort has time complexity of O(n^(3/2))
"""

#Time complexity: Best case O(n log n), average case O(n^(3/2)), worst case O(n^2)

def shellSort(array, n):
    #arrange elements at each n/2, n/4, n/8 ... intervals
    interval = n // 2
    while interval > 0:
        print("interval: ", interval)
        for i in range(interval, n):
            temp = array[i]
            j = i
            
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

                array[j] = temp
                print(array)
            
        interval //= 2


shellSort([3, 6, 2, 1, 7, 9, 8, 5], 8)