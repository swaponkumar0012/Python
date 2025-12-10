# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to make the linked list circular
def make_circular(head):
    if head is None:
        return

    temp = head
    while temp.next is not None:  # move to the last node
        temp = temp.next

    temp.next = head  # connect last node to head


# Function to print circular list (limit to avoid infinite loop)
def print_circular(head, limit=10):
    temp = head
    count = 0
    while temp is not None and count < limit:
        print(temp.data, end=" ")
        temp = temp.next
        count += 1
    print()


# ----------- Driver Code -----------
# Create simple linked list: 10 -> 20 -> 30
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

print("Before circular:")
print_circular(head, 3)

make_circular(head)

print("After circular:")
print_circular(head, 10)  # shows repetition due to circular structure
