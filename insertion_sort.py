def insertion_sort(array):
    """
    Sorts the given array using the insertion sort algorithm.

    Parameters:
    array (list): The array to be sorted.

    Returns:
    None. The array is sorted in-place.
    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

# Example usage:
arr = [5, 2, 8, 12, 1, 6]
insertion_sort(arr)
print(arr)