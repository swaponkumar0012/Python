class Node:
    """Represents a node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Represents a singly linked list."""
    def __init__(self):
        self.head = None

    def add_element(self, data):
        """Adds a new element to the end of the linked list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_element(self, key):
        """Deletes the first occurrence of an element with the given key."""
        current = self.head
        prev = None

        if current and current.data == key:
            self.head = current.next
            return

        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Element {key} not found in the list.")
            return

        prev.next = current.next


    def search_element(self, key):
        """Searches for an element with the given key and returns True if found, False otherwise."""
        current = self.head
        while current:
            if current.data == key:
                print("element is found in linked_list:")
                return 
            
            current = current.next
            print("element is not found in linked_list :")
            return
        

    def sort_list(self):
        """Sorts the linked list in ascending order based on node data."""
        if self.head is None or self.head.next is None:
            return 

    

    

       
        # Convert linked list to a Python list for sorting
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next

        elements.sort()

        # Reconstruct linked list from sorted elements
        current = self.head
        for data in elements:
            current.data = data
            current = current.next

    def display(self):
        """Displays the elements of the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def show_menu (self):
        print("\n-- Linked list Menu --")
    print("1. Insert Element")
    print("2. Display Linked List")
    print("3. Delete Linked List")
    print("4. Search Linked List")
    print("5. Sort Linked List")
    print("6. Exit")
    


linked_list = LinkedList()
while True: 
    linked_list.show_menu()
    choice= input("Enter your choice !!")
    if choice == "1":
        data = int(input("Enter the element to insert: "))
        linked_list.add_element(data)
        
    elif choice == "2":
        linked_list.display()
    elif choice == "3":
         data = int(input("Enter the element to delete: "))
         linked_list.delete_element(data)
    elif choice == "4":
        data = int(input("Enter the element to search: ")) 
    
        linked_list.search_element(data)
        

        

    elif choice == "5":
        linked_list.sort_list()
    

    
    

        



    elif choice == "6":
        print("Exiting")
        break






  
 








    


   