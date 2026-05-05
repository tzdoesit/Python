# practice for data structures


# python list = dynamic array
nums = [10, 20, 30, 40, 50]
print(nums[2]) # print 30
nums.append(60)# O(1) amortized
nums.insert(1, 15) # O(n) - shifts elements
print(nums[4])

# linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
# 1 -> 2 -> 3 -> None

# Stack = LIFO
stack = []
stack.append("a")   # push
stack.append("b")
stack.append("c")
print(stack.pop()) # "c" - last in, first out
print(stack.pop()) # "b"

# Queue = FIFO
from collections import deque
q = deque()
q.append("task1")   # enqueue
q.append("task2")
q.append("task3")
print(q.popleft())  # "task1" - FIFO

# deque - more flexible than a stack or queue alone

from collections import deque
d=deque([1,2,3])
d.appendleft(0)  # [0,1,2,3]
d.append(4)      # [0,1,2,3,4]
d.popleft()      # 0
d.pop()          # 4
d.append(69)
print(d)         # should print [1,2,3,69]
