import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def timsort(arr):
    arr.sort()

sizes = [100, 1000, 5000, 10000]
results = {}

for size in sizes:
    arr = [random.randint(0, 100000) for _ in range(size)]
    
    results[size] = {
        "Insertion Sort": timeit.timeit(lambda: insertion_sort(arr.copy()), number=1),
        "Merge Sort": timeit.timeit(lambda: merge_sort(arr.copy()), number=1),
        "Timsort (Python's sort)": timeit.timeit(lambda: timsort(arr.copy()), number=1)
    }

for size, times in results.items():
    print(f"Array size: {size}")
    for alg, time in times.items():
        print(f"  {alg}: {time:.6f} sec")
    print()