# Custom exception for negative number input
class NegativeNumberError(Exception):
    def __init__(self, message="Negative numbers are not allowed."):
        self.message = message
        super().__init__(self.message)

# Function to divide two numbers and handle errors
def divide_numbers():
    try:
        # Prompt the user for input
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        # Check if either number is negative
        if num1 < 0 or num2 < 0:
            raise NegativeNumberError  # Raise custom exception

        # Perform division and print the result
        result = num1 / num2
    except NegativeNumberError as nne:
        # Handle NegativeNumberError
        print(f"Error: {nne}")
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")
    else:
        # If no exceptions occur, print the result
        print(f"The result of {num1} divided by {num2} is {result}")
    finally:
        # Finally block executes regardless of exceptions
        print("Program execution completed.")

# Call the function to execute the program
divide_numbers()
