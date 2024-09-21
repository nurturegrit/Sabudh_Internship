import time
# Decorators
# used to add functionality to an existing functions - like add ons

# A function can take another function as an argument
# As functions are also objects in python
# decorators.py
# Define uppercase_decorator - modifies a function to return the result in uppercase
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # Call the original function and convert its result to uppercase
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

# Define say_hello
def say_hello(name):
    return f"Hello, {name}!"

#Apply uppercase_decorator to say_hello and assign to greet
greet = uppercase_decorator(say_hello)

#  Test the greet function
print(greet("Sumit")) 

#  Define timing_decorator that measures the execution time of a function
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        # start time
        start_time = time.time()
        # Call the original function
        result = func(*args, **kwargs)
        # Calculate the time taken to process the function
        process_time = time.time() - start_time
        # Print the timing information
        print(f"Function took {process_time} seconds to execute.")
        return result
    return wrapper

# Apply timing_decorator to greet and assign to timed_greet
timed_greet = timing_decorator(greet)

# Test the timed_greet function
print(timed_greet("Sumit"))

# Define a class called Math with methods add and subtract
class Math:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Define logging_decorator to log arguments and result
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        # Log the arguments
        print(f"Calling function with arguments: {args}, {kwargs}")
        # Call the original function
        result = func(*args, **kwargs)
        # Log the result
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# Apply logging_decorator to Math methods and test them
Math.add = logging_decorator(Math.add)
Math.subtract = logging_decorator(Math.subtract)

# Create an instance of Math class
math_instance = Math()

# Test add method
print(math_instance.add(10, 5)) 

# Test subtract method
print(math_instance.subtract(10, 5))
