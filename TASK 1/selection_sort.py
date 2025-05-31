"""
    Selection Sort implementation
    Sorts the list in ascending order.
"""
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Testing
dataset_Raw= [45, 22, 89, 11, 10]
print("Original Dataset", dataset_Raw)
sorted_yash = selection_sort(dataset_Raw.copy())
print("Sorted Dataset", sorted_yash)
