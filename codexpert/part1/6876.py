n = int(input())
height = []
for _ in range(n):
    height.append(int(input()))

answer = 0
stack = []

for h in height:
    while stack and stack[-1] <= h:
        stack.pop()
    answer += len(stack)
    stack.append(h)


print(answer)
