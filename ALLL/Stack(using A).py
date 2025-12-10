class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackList:
    def __init__(self):
        self.top = None

    def push(self, x):
        new = Node(x)
        new.next = self.top
        self.top = new

    def pop(self):
        if self.top is None:
            return "Stack Underflow"
        val = self.top.data
        self.top = self.top.next
        return val

    def peek(self):
        return self.top.data if self.top else None

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Example
s = StackList()
s.push(15)
s.push(18)
s.push(20)
s.push(30)
s.display()
print("Popped:", s.pop())
s.display()
