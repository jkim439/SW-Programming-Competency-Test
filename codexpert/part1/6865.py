import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query


# 입력받는 부분
N, num, T, query = Input_Data()


# 여기서부터 작성
sol = []
from bisect import bisect_left

for q in query:
    i = bisect_left(num, q)
    if num[i] == q:
        sol.append(i)
    else:
        sol.append(0)

# 출력하는 부분
print(*sol, sep="\n")
