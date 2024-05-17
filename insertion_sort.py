
def insertion_sort(arr):
    """
    Sorts the given array using the insertion sort algorithm.

    Parameters:
    arr (list): The array to be sorted.

    Returns:
    None. The array is sorted in-place.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [5, 2, 8, 12, 1, 6]
insertion_sort(arr)
print(arr)

