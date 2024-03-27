import queue

queue = queue.PriorityQueue()

queue.put((2, "SEC"))
queue.put((1, "LGE"))

print(queue.qsize())

print(queue.get())
print(queue.get())
