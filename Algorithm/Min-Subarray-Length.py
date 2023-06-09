import math


def minSubArray(arr, k):
    right = 0
    left = 0
    sum = 0
    minLength = math.inf
    while left < len(arr):
        print(left, right, sum)
        if sum < k and right < len(arr):
            sum += arr[right]
            right += 1
        elif sum >= k:
            if right - left < minLength:
                minLength = right - left
            sum -= arr[left]
            left += 1
        elif right >= len(arr):
            break
    return minLength


arr = [8, 1, 6, 15, 3, 16, 5, 7, 14, 30, 12]
k = 60
print(minSubArray(arr, k))
