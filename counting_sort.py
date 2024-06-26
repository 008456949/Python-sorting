def counting_sort(arr):
    # Find the maximum element in the array
    max_val = max(arr)
    
    # Create a count array to store the count of each element
    count = [0] * (max_val + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Update the count array to store the cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create a sorted array using the count array
    sorted_arr = [0] * len(arr)
    for num in arr:
        sorted_arr[count[num] - 1] = num
        count[num] -= 1
    
    return sorted_arr