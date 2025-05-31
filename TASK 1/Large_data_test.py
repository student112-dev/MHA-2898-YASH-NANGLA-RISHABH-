import random
import time

from sorting_algos_yash import selection_sort as selection_sort, insertion_sort as insertion_sort

#Testing Over 10,000 Elemenets
# Large dataset generation
dataset_Raw= [random.randint(1, 1000) for _ in range(1000)]

# Time Taken for Selection Sort
start_time = time.time()
selection_sort(dataset_Raw.copy())
end_time = time.time()
print("Selection Sort Time", end_time - start_time, "seconds")

# Time Taken for Insertion Sort
start_time = time.time()
insertion_sort(dataset_Raw.copy())
end_time = time.time()
print("Insertion Sort Time", end_time - start_time, "seconds")