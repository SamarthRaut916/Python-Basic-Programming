from collections import deque

# ---------------- Stack ---------------- #
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack


# ---------------- Queue ---------------- #
class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        return None
    
    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return list(self.queue)


# ---------------- Search ---------------- #
def linear_search(arr, target):
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr, target):
    arr = sorted(arr)  # ensure array is sorted
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1
        


# ---------------- Sort ---------------- #
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr[1:] if int(x) <= int(pivot)]
    greater = [x for x in arr[1:] if int(x) > int(pivot)]
    return quick_sort(less) + [pivot] + quick_sort(greater)


myList = [10,22,1,2,45,78,100,15]

# print(myList[1:])

# print(quick_sort(myList))
# print(merge_sort(myList))
# print(bubble_sort(myList))
print(binary_search(myList,45))