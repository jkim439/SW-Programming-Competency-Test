import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = list(map(int, readl().split()))
    return N, num


N, num = Input_Data()

print(*sorted(num, reverse=True))
