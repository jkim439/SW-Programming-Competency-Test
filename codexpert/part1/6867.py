import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    pos = [int(readl()) for _ in range(N)]
    return N, pos


# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
from bisect import bisect_left, bisect_right

pos.sort()
answer = 0
for i, n in enumerate(pos):
    for m in pos[i + 1 :]:
        step = m - n
        count = bisect_right(pos, m + step * 2) - bisect_left(pos, m + step)
        if count > 0:
            answer += count

# 출력하는 부분
print(answer)
