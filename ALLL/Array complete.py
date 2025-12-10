# Program to add, delete, search, and sort elements in an array

def display_menu():
    print("\n===== ARRAY OPERATIONS =====")
    print("1. Display Array")
    print("2. Add Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Sort Array")
    print("6. Exit")

def display_array(arr):
    print("Current Array:", arr)

def add_element(arr):
    element = int(input("Enter element to add: "))
    arr.append(element)
    print(f"{element} added successfully.")

def delete_element(arr):
    element = int(input("Enter element to delete: "))
    if element in arr:
        arr.remove(element)
        print(f"{element} deleted successfully.")
    else:
        print("Element not found in array.")

def search_element(arr):
    element = int(input("Enter element to search: "))
    if element in arr:
        index = arr.index(element)
        print(f"{element} found at index {index}.")
    else:
        print("Element not found in array.")

def sort_array(arr):
    arr.sort()
    print("Array sorted successfully.")

# Main program
arr = []

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        display_array(arr)
    elif choice == '2':
        add_element(arr)
    elif choice == '3':
        delete_element(arr)
    elif choice == '4':
        search_element(arr)
    elif choice == '5':
        sort_array(arr)
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
