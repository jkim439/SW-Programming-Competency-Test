import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_score = list(map(int, readl().split()))
    return N, list_score


# 입력받는 부분
N, list_score = Input_Data()

# 여기서부터 받는
ans = []

for i, n in enumerate(list_score):
    ans.append([i + 1, n])

ans.sort(key=lambda x: x[1], reverse=True)

# 출력하는 부분
print(*[i for i, n in ans[:3]])
