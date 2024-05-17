# Description: Bubble sort algorithm
ar = [1, 4, 2, 5, 6]

def bubble_sort(arr):
    """
    Sorts the given array using the bubble sort algorithm.

    Args:
        arr (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(arr)
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
    return arr

print(bubble_sort(ar))
