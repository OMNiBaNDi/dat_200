
#Iterative solution

def fact_iterative(n):
    prod = 1
    for i in range(n, 0, -1):
        prod = prod * i
    return prod

def fact_recursive(n):
    #base case
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)