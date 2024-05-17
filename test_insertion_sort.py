"""
Module docstring goes here.
"""

# test_insertion_sort.py
import pytest
from insertion_sort import insertion_sort

def test_insertion_sort():
    """
    Function docstring goes here.
    """
    # Test case 1: Unsorted array
    arr = [5, 2, 8, 12, 1, 6]
    sorted_arr = [1, 2, 5, 6, 8, 12]
    insertion_sort(arr)
    assert arr == sorted_arr

    # Test case 2: Already sorted array
    arr = [1, 2, 3, 4, 5]
    sorted_arr = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == sorted_arr

    # Test case 3: Reverse sorted array
    arr = [5, 4, 3, 2, 1]
    sorted_arr = [1, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == sorted_arr

    # Test case 4: Array with duplicates
    arr = [4, 2, 5, 2, 3]
    sorted_arr = [2, 2, 3, 4, 5]
    insertion_sort(arr)
    assert arr == sorted_arr

    # Test case 5: Empty array
    arr = []
    sorted_arr = []
    insertion_sort(arr)
    assert arr == sorted_arr

    # Test case 6: Single element array
    arr = [1]
    sorted_arr = [1]
    insertion_sort(arr)
    assert arr == sorted_arr

if __name__ == "__main__":
    pytest.main()
