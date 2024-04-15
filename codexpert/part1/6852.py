r = 4
ans = 0
r2 = r**2

for h in range(1, r):
    ans += int((r**2 - h**2) ** 0.5)

print(ans * 4)
