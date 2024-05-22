import sys
from bisect import bisect_left

m, n, l = map(int, sys.stdin.readline().split())
guns = list(map(int, sys.stdin.readline().split()))
animals = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = 0
guns.sort()

for x, y in animals:
    if l < y:
        continue

    i = bisect_left(guns, x)
    for j in [i - 1, i, i + 1]:
        if 0 <= j < len(guns) and abs(guns[j] - x) + y <= l:
            answer += 1
            break

print(answer)
