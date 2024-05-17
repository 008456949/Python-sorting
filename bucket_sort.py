def bucket_sort(arr):
    """
    Sorts an array using the bucket sort algorithm.
    
    Args:
        arr (list): The array to be sorted.
    
    Returns:
        list: The sorted array.
    """
    # Determine the maximum value in the array
    max_val = max(arr)
    
    # Create empty buckets
    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]
    
    # Distribute elements into buckets
    for num in arr:
        index = int(num * num_buckets / (max_val + 1))
        buckets[index].append(num)
    
    # Sort each bucket individually
    for bucket in buckets:
        bucket.sort()
    
    # Concatenate the sorted buckets
    sorted_arr = [num for bucket in buckets for num in bucket]
    
    return sorted_arr