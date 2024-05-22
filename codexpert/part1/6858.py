import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


N = Input_Data()
sol = []

dq = deque([i for i in range(1, N + 1)])
while dq:
    n = int(dq[-1] / 2)
    dq.rotate(-n)
    sol.append(dq.popleft())

print(*sol)
