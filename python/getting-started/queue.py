# queue
from collections import deque

queue = deque(["1", "2"])
queue.append("3")
queue.append("4")
print queue.popleft()
print queue.popleft()