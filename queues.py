
# collections is a Python module that I'm using
# deque is a object (class) on that module

from collections import deque

rome_queue = deque()
rome_queue.append(1)
rome_queue.append(5)
rome_queue.append(10)

print(rome_queue)

rome_queue.pop()

print(rome_queue)

rome_list = ['work2', 'work100'] # 2 million elements

rome_list.pop(0)
print(rome_list)

# O(n)


# O(1)
rome = {
    "name": "Rome",
    "age": 32
}