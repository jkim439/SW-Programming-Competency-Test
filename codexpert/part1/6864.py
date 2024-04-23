import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    package = list(map(int, readl().split()))
    return N, package


# 입력받는 부분
N, package = Input_Data()

# 여기서부터 작성
from heapq import *

heapify(package)
sum = 0

for _ in range(N - 1):
    a = heappop(package)
    b = heappop(package)
    sum += a + b
    heappush(package, a + b)


# 출력하는 부분
print(sum)
