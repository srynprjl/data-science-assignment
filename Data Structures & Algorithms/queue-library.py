from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

print(queue)
print(f"Top: {queue[0]}")
print(f"Pop: {queue.popleft()}")
print(f"Pop: {queue.popleft()}")
print(queue)
