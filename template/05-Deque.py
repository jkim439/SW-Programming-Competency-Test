from collections import deque

deque = deque()

deque.append(1)
deque.appendleft(2)

deque.extend([3])
deque.extendleft([4])

print(deque.pop())
print(deque.popleft())

deque.remove(1)

deque.rotate(1)
deque.rotate(-1)
