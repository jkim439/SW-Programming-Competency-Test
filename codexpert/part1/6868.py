n = int(input())
city_budget = list(map(int, input().split()))
total_budget = int(input())

city_budget.sort()
start = 1
end = city_budget[-1]
max_budget = 0

while start <= end:
    mid_budget = (start + end) // 2
    use_budget = 0

    for budget in city_budget:
        if budget <= mid_budget:
            use_budget += budget
        else:
            use_budget += mid_budget

    if use_budget > total_budget:
        end = mid_budget - 1
    else:
        max_budget = mid_budget
        start = mid_budget + 1


print(max_budget)
