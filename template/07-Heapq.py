from heapq import *

heap = [42, 67, 32, 91, 12, 45, 76]
heapify(heap)

heappush(heap, 21)
print(heappop(heap))

max = nlargest(len(heap), heap)
print(max)
