class Stack:
    def __init__(self):
        self.stack = []

    # Push element onto stack
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    # Pop element from stack
    def pop(self):
        if not self.is_empty():
            item = self.stack.pop()
            print(f"Popped: {item}")
            return item
        else:
            print("Stack is empty!")

    # Peek at top element
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty!")

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display the stack
    def display(self):
        print("Stack:", self.stack)


# Example usage:
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element:", s.peek())
s.pop()
s.display()
