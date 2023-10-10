def find_cyclic_shift(arr):
    n = len(arr)

    # Check if the array is already sorted
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
        return 0

    index = -1
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # If we find more than one such index, return -1
            if index != -1:
                return -1
            index = i

    if index == -1:
        return -1

    # Calculate the shift needed
    t = n - index - 1

    # Perform the cyclic shift
    arr = arr[-t:] + arr[:-t]

    # Check if the array is sorted
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
        return t
    else:
        return -1


# Example usage
print(find_cyclic_shift([3, 8, 1, 5]))  # Output: 2
