import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = list(map(int, readl().split()))
    return N, num


# 입력받는 부분
N, num = Input_Data()

# 출력하는 부분
print(*sorted(num))
