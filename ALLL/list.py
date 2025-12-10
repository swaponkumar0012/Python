# Program to add, delete, search, and sort elements in a List

def display_menu():
    print("\n===== LIST OPERATIONS =====")
    print("1. Display List")
    print("2. Add Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Sort List")
    print("6. Exit")

def display_list(lst):
    print("Current List:", lst)

def add_element(lst):
    element = input("Enter element to add: ")
    lst.append(element)
    print(f"'{element}' added successfully.")

def delete_element(lst):
    element = input("Enter element to delete: ")
    if element in lst:
        lst.remove(element)
        print(f"'{element}' deleted successfully.")
    else:
        print("Element not found in the list.")

def search_element(lst):
    element = input("Enter element to search: ")
    if element in lst:
        index = lst.index(element)
        print(f"'{element}' found at index {index}.")
    else:
        print("Element not found in the list.")

def sort_list(lst):
    lst.sort()
    print("List sorted successfully.")

# Main program
lst = []

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_list(lst)
    elif choice == '2':
        add_element(lst)
    elif choice == '3':
        delete_element(lst)
    elif choice == '4':
        search_element(lst)
    elif choice == '5':
        sort_list(lst)
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
