# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def make_circular(head):
    if head is None:
        return

    temp = head
    while temp.next is not None:  
        temp = temp.next

    temp.next = head  


def print_circular(head, limit=10):
    temp = head
    count = 0
    while temp is not None and count < limit:
        print(temp.data, end=" ")
        temp = temp.next
        count += 1
    print()



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


print("Before circular:")
print_circular(head, 3)

make_circular(head)

print("After circular:")
print_circular(head, 15)  


