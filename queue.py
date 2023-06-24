class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        else:
            print("Queue is empty.")
            return None

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()
print(queue.isEmpty())  # Output: True

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.dequeue())  
# Output: 1
print(queue.dequeue())  
# Output: 2
print(queue.isEmpty())  
# Output: False
print(queue.dequeue()) 
# Output: 3
print(queue.dequeue()) 
# Output: Queue is empty. None
