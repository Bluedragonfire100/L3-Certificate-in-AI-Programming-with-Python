The program code is developed for users to input two numbers, which are calculated using various mathematical functions through the use of a menu option.  To select the method for carrying out a particular mathematical operation.   

Each operation is encapulated inside its own function and uses a while loop, so the program stays open until the user chooses to exit


def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """Returns the quotient of two numbers. Handles division by zero."""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def main():
    while True:
        # Display the menu option to the user
        print("\n--- Math Functions Menu ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")
        
        # Take the menu choice input
        choice = input("Enter your choice (1-5): ").strip()
        
        # Check if the user wants to exit first
        if choice == '5':
            print("Exiting the program. Goodbye!")
            break
#The following program calculates maths functions through use of a menu option system so a user can choose which function to carry out on two numbers they input.

#Each operation is encapsulated inside its own function and uses a while loop so the program stays open until the user chooses to exit        
        
# Validate that the menu option exists
        if choice in ('1', '2', '3', '4'):
            try:
                # Prompt the user for numerical values
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue
                
            # FIXED: Aligned all conditional blocks perfectly
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid option from 1 to 5.")

# FIXED: Completed the broken execution block at the bottom
if __name__ == "__main__":
    main()

#