class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty.")
            return None

    def isEmpty(self):
        return len(self.stack) == 0

stack = Stack()
print(stack.isEmpty()) 
# Output: True

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  
# Output: 3
print(stack.pop())  
# Output: 2
print(stack.isEmpty()) 
# Output: False
print(stack.pop())  
# Output: 1
print(stack.pop()) 
# Output: Stack is empty. None
