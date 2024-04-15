num = 1789
ans = 0


def getMinMax(n):
    l = []
    while n:
        l.append(n % 10)
        n //= 10
    l.sort()
    return (
        l[0] * 1000 + l[1] * 100 + l[2] * 10 + l[3] * 1,
        l[3] * 1000 + l[2] * 100 + l[1] * 10 + l[0] * 1,
    )


while num != 6174:
    min, max = getMinMax(num)
    num = max - min
    ans += 1

print(ans)
