def selection_sort(data):
    for select in range(len(data) - 1):
        min = select
        for i in range(select + 1, len(data)):
            if data[min] > data[i]:
                min = i
        data[select], data[min] = data[min], data[select]
    return data


data = [7, 2, 4, 1, 6, 9, 3, 5, 8]
print(data)
selection_sort(data)
print(data)
