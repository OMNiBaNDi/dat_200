

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