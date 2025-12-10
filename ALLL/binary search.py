def binary_search(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example
arr = [1, 3, 5, 7, 9, 11,13,20]
x = 13

index = binary_search(arr, x)
print("Found at index:", index)
