N = 15
ans = []

l = [0] * 25000
l[0] = "0/1"
l[-1] = "1/1"

for i in range(2, N + 1):
    for j in range(1, i):
        idx = int(j / i * 25000)
        if l[idx] == 0:
            l[idx] = "{}/{}".format(j, i)

ans = [s for s in l if s != 0]
print(*ans, sep="\n")
