import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


# 입력 받는 부분
N = Input_Data()
sol = []

# 여기서부터 작성
dq = deque([i for i in range(1, N + 1)])
while dq:
    n = int(dq[-1] / 2)
    dq.rotate(-n)
    sol.append(dq.popleft())

# 출력하는 부분
print(*sol)
