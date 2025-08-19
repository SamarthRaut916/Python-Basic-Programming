def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
unsorted = [64, 25, 12, 22, 11]
sorted_list = selection_sort(unsorted)
print("Sorted:", sorted_list)  
