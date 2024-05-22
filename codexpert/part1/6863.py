import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_score = list(map(int, readl().split()))
    return N, list_score


N, list_score = Input_Data()

ans = []

for i, n in enumerate(list_score):
    ans.append([i + 1, n])

ans.sort(key=lambda x: x[1], reverse=True)

print(*[i for i, n in ans[:3]])
