# 此模組快速建立 minHeap
# 如果想使用 maxHeap，只需要將每個數值加上負號即可
import heapq
import random

test = []
for i in range(10):
    test.append(-random.randint(0, 100))

print("init", test)

heapq.heapify(test)  # 直接修改 test
print("heapified", test)


print("result", [-heapq.heappop(test) for i in range(len(test))])
