import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    str_exp = readl().split()
    nums = list(map(int, str_exp[0::2]))
    op = str_exp[1::2]
    return N, nums, op


N, nums, op = Input_Data()

sol = -1
stack = [nums[0]]

for o, n in zip(op, nums[1:]):
    if o == "+":
        stack.append(n)
    elif o == "-":
        stack.append(-n)
    elif o == "*":
        stack.append(stack.pop() * n)
    elif o == "/":
        stack.append(int(stack.pop() / n))

print(sum(stack))
