import math
import random


def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while j >= 0 and arr[j] >= key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


test = []
for i in range(10):
    test.append(random.randint(0, 100))

print(insertionSort(test))
