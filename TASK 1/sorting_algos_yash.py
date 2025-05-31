# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx_yash = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx_yash]:
                min_idx_yash = j
        arr[i], arr[min_idx_yash] = arr[min_idx_yash], arr[i]
    return arr
#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key_yash = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key_yash:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_yash
    return arr
