def add_item(shopping_list):
    item = input("What would you like to add to the shopping list? ")
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")

def remove_item(shopping_list):
    item = input("What would you like to remove from the shopping list? ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def print_list(shopping_list):
    print("Shopping List:")
    for item in shopping_list:
        print(f"- {item}")

def main():
    shopping_list = []
    
    while True:
        print("\nOptions:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Print list")
        print("4. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            print_list(shopping_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
