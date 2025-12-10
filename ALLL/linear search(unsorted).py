def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return index where the element is found
    return -1  # Return -1 if not found

# Example usage:
arr = [12, 5, 9, 1, 20]
target = 9

result = linear_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
