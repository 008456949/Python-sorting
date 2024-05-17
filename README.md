# Python Sorting Algorithms

This repository contains various sorting algorithm techniques implemented in Python.

## Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Radix Sort
- Counting Sort
- Bucket Sort

## Tips and Tricks

- When choosing a sorting algorithm, consider the size of the input data. Some algorithms perform better on small datasets, while others are more efficient for larger datasets.
- Understand the time complexity of each sorting algorithm. This will help you choose the most appropriate algorithm for your specific use case.
- Take advantage of built-in sorting functions in Python, such as `sorted()` and `list.sort()`, which use efficient sorting algorithms under the hood.

## Code Helpers

- If you need to sort a list of objects based on a specific attribute, you can use the `key` parameter in the `sorted()` or `list.sort()` functions. For example, to sort a list of dictionaries by the 'name' key, you can use `sorted(my_list, key=lambda x: x['name'])`.
- To sort a list in descending order, you can use the `reverse` parameter in the `sorted()` or `list.sort()` functions. For example, `sorted(my_list, reverse=True)` will sort the list in descending order.

## Definitions

- **Sorting Algorithm**: A method or process used to arrange elements in a specific order.
- **Time Complexity**: A measure of the amount of time taken by an algorithm to run as a function of the length of the input.
- **Bubble Sort**: A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Selection Sort**: A sorting algorithm that divides the input list into a sorted and an unsorted region, and repeatedly selects the smallest (or largest) element from the unsorted region and moves it to the sorted region.
- **Insertion Sort**: A sorting algorithm that builds the final sorted array one item at a time by repeatedly inserting a selected element into the correct position in the sorted portion of the array.
- **Merge Sort**: A divide-and-conquer algorithm that divides the input list into two halves, sorts each half recursively, and then merges the sorted halves to produce a sorted list.
- **Quick Sort**: A divide-and-conquer algorithm that selects a pivot element and partitions the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
- **Heap Sort**: A comparison-based sorting algorithm that uses a binary heap data structure to sort elements.
- **Radix Sort**: A non-comparative sorting algorithm that sorts data with integer keys by grouping keys by the individual digits which share the same significant position and value.
- **Counting Sort**: A sorting algorithm that sorts elements based on their frequencies, rather than their values.
- **Bucket Sort**: A sorting algorithm that works by distributing the elements of an array into a number of buckets, and then sorting each bucket individually.

Feel free to explore the code and learn about different sorting techniques!
