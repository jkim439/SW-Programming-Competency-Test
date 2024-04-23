from bisect import bisect_left, bisect_right

nums = [4, 5, 5, 5, 5, 5, 5, 5, 5, 6]
n = 5

print(bisect_left(nums, n))
print(bisect_right(nums, n))
