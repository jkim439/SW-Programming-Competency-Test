import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    package = list(map(int, readl().split()))
    return N, package


N, package = Input_Data()

from heapq import *

heapify(package)
sum = 0

for _ in range(N - 1):
    a = heappop(package)
    b = heappop(package)
    sum += a + b
    heappush(package, a + b)


print(sum)
