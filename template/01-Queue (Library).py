import queue

queue = queue.Queue()

queue.put("LGE")
queue.put("SEC")

print(queue.qsize())

print(queue.get())
print(queue.get())
