import math, random


def heapSort(arr):
    def minHeapify(n):
        left = n * 2 + 1
        right = n * 2 + 2
        minIndex = n
        if left < len(arr) and arr[left] < arr[minIndex]:
            minIndex = left
        if right < len(arr) and arr[right] < arr[minIndex]:
            minIndex = right
        if minIndex != n:
            temp = arr[minIndex]
            arr[minIndex] = arr[n]
            arr[n] = temp
            minHeapify(minIndex)

    def bulidHeap():
        for i in range(len(arr) - 1, -1, -1):
            minHeapify(i)

    result = []

    def sort():
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[0]
            arr[0] = arr[i]
            arr[i] = temp
            result.append(arr.pop())
            minHeapify(0)

    print(arr)
    bulidHeap()
    sort()
    return result


test = []
for i in range(10):
    test.append(random.randint(0, 100))

print(heapSort(test))
