def insertion_sort(data):
    for turn in range(1, len(data)):
        for i in range(turn, 0, -1):
            if data[i - 1] > data[i]:
                data[i - 1], data[i] = data[i], data[i - 1]
            else:
                break
    return data


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
insertion_sort(data)
print(data)
