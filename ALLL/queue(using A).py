from collections import deque

class QueueArray:
    def __init__(self):
        self.queue = deque()

    # Enqueue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue
    def dequeue(self):
        if not self.is_empty():
            item = self.queue.popleft()
            print(f"Dequeued: {item}")
            return item
        else:
            print("Queue is empty!")

    # Peek
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty!")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", list(self.queue))


# Example usage:
q2 = QueueArray()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
q2.enqueue(40)
q2.display()

print("Front element:", q2.peek())
q2.dequeue()
q2.display()
