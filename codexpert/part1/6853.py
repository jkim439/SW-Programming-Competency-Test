s = "()(((()())(())()))(())"
s = list(s)

ans = 0
stick = 0

for i in range(len(s)):
    if s[i] == "(":
        stick += 1
    else:
        stick -= 1
        if s[i - 1] == "(":
            ans += stick
        else:
            ans += 1

print(ans)
