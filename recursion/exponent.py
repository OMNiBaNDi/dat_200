
#Iterative solution to find power of number

def exp_iterative(x, n):
    base = x
    exponent = n
    result = 1

    for exponent in range(exponent, 0, -1):
        result *= base
    return result

#Recursive solution to find the power of a number
def exp_recursive(x, n):
    #base case
    if n == 0:
        return 1
    else:
        return x * exp_recursive(x, n-1)