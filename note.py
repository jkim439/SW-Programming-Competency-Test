n = 5
l = []

for i in range(1, n):
    for j in range(i + 1, n + 1):
        a = i / j
        b = str(i) + "/" + str(j)
        if not any(a == e[0] for e in l):
            # if not any(a in l for l in l):
            l.append([a, b])

l.sort(key=lambda x: x[0])

ans = ["0/1"] + [i[1] for i in l] + ["1/1"]
for val in ans:
    print(val)
