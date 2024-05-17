def radix_sort(arr):
    """
    Sorts the given array using the radix sort algorithm.
    
    Args:
        arr (list): The array to be sorted.
    """
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    
    # Perform counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    """
    Performs counting sort on the given array based on the given exponent.
    
    Args:
        arr (list): The array to be sorted.
        exp (int): The exponent used for counting sort.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    
    # Change count[i] so that count[i] contains the actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    # Copy the output array to arr[], so that arr[] contains
    # sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]