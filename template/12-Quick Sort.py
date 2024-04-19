def quick_sort(data):
    if len(data) <= 1:
        return data

    else:
        pivot = data[0]
        left = [i for i in data if i < pivot]
        right = [i for i in data if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
print(quick_sort(data))
