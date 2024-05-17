import sys

sys.setrecursionlimit(100)


def binary_search(city, start, end):
    median = (start + end) // 2
    print(start, end, median)
    if median == start or median == end:
        return median

    result = sum([i for i in city if i < median]) + (
        len([i for i in city if i >= median]) * median
    )

    if result < median:
        return binary_search(city, start, median)
    elif result > median:
        return binary_search(city, median, end)
    else:
        return True


city = [163, 209, 218, 325, 383, 410, 413, 443, 456, 531]
budge = 3051
print(city)

start = 0
end = budge
median = sum(city) // len(city)

answer = 0

if (
    sum([i for i in city if i < median])
    + (len([i for i in city if i >= median]) * median)
    < budge
):
    binary_search(city, 0, median)
else:
    binary_search(city, median, end)
