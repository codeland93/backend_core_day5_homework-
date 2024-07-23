def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

def get_operation_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    return choice

def get_numbers():
    num_1 = float(input("Enter first number: "))
    num_2 = float(input("Enter second number: "))
    return num_1, num_2

def main():
    while True:
        choice = get_operation_choice()

        if choice in ['1', '2', '3', '4']:
            num_1, num_2 = get_numbers()

            if choice == '1':
                print(f"The result is: {add(num_1, num_2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num_1, num_2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num_1, num_2)}")
            elif choice == '4':
                print(f"The result is: {divide(num_1, num_2)}")
        else:
            print("Invalid input, please enter a valid choice.")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

