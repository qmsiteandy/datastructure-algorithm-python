import random
import math


def mergeSort(arr):
    def sort(arr):
        if len(arr) <= 1:
            return arr
        middle = math.floor(len(arr) / 2)
        return merge(sort(arr[0:middle]), sort(arr[middle : len(arr)]))

    def merge(arr1, arr2):
        p1 = 0
        p2 = 0
        result = []
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] < arr2[p2]:
                result.append(arr1[p1])
                p1 += 1
            else:
                result.append(arr2[p2])
                p2 += 1
        while p1 < len(arr1):
            result.append(arr1[p1])
            p1 += 1
        while p2 < len(arr2):
            result.append(arr2[p2])
            p2 += 1
        return result

    return sort(arr)


test = []
for i in range(10):
    test.append(random.randint(0, 100))

print(mergeSort(test))
