N = int(input())

for _ in range(N):
    a = str(input())
    b = "".join(reversed(a))
    sum = str(int(a) + int(b))
    if sum == "".join(reversed(sum)):
        print("YES")
    else:
        print("NO")
