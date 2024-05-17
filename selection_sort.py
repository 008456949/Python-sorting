def selection_sort(array):
    """
    Sorts an array using the selection sort algorithm.

    Args:
        array (list): The array to be sorted.

    Returns:
        list: The sorted array.
    """
    n = len(array)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# Example usage:
arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Sorted array:", sorted_arr)

