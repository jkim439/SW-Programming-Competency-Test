import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    job = list(map(int, readl().split()))
    return N, M, job


T = int(sys.stdin.readline())
sol = []
for _ in range(T):
    # 입력받는 부분
    N, M, job = Input_Data()

    # 여기서부터 작성
    dq = deque(job)
    count = 0
    index = M

    while dq:
        poped = dq.popleft()
        index -= 1

        if any(i for i in dq if i > poped):
            dq.append(poped)
            if index < 0:
                index = len(dq) - 1

        else:
            count += 1
            if index < 0:
                break

    sol.append(count)


# 출력하는 부분
print(*sol, sep="\n")
