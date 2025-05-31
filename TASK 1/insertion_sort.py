"""
    Insertion Sort implementation for Yash Nangla (Rishabh).
    Sorts the list in ascending order.
""" 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value_yash = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value_yash:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value_yash
    return arr

# Test dataset
dataset = [45, 22, 89, 11, 10 , 8]
print("Original Dataset", dataset)
sorted_values = insertion_sort(dataset.copy())
print("Sorted Dataset", sorted_values)
