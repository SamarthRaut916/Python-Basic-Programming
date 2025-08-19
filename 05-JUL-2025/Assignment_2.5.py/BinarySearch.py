def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Found, return index
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Not found
numbers = [1, 3, 5, 7, 9, 11]
index = binary_search(numbers, 11)
print(f"Found at index: {index}")  
