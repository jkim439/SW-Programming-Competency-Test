import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos


N, pos = Input_Data()

from bisect import bisect_left, bisect_right

pos.sort()
answer = 0
for i, n in enumerate(pos):
    for m in pos[i + 1 :]:
        step = m - n
        count = bisect_right(pos, m + step * 2) - bisect_left(pos, m + step)
        if count > 0:
            answer += count

print(answer)
