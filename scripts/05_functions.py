# Python Basics - Functions

# 1. Simple Function
print("=== Simple Function ===")

def greet():
    print("Hello, Welcome to Python!")

greet()

# 2. Function with Parameters
print("\n=== Function with Parameters ===")

def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# 3. Function with Multiple Parameters
print("\n=== Function with Multiple Parameters ===")

def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(f"5 + 3 = {sum_result}")

# 4. Function with Default Parameters
print("\n=== Function with Default Parameters ===")

def introduce(name, age=20, city="Unknown"):
    print(f"Name: {name}, Age: {age}, City: {city}")

introduce("John")
introduce("Jane", 25)
introduce("Bob", 30, "New York")

# 5. Function with Multiple Return Values
print("\n=== Function with Multiple Return Values ===")

def get_coordinates():
    x = 10
    y = 20
    return x, y

coord_x, coord_y = get_coordinates()
print(f"Coordinates: ({coord_x}, {coord_y})")

# 6. Function with Variable Length Arguments (*args)
print("\n=== Function with *args ===")

def sum_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum: {sum_numbers(1, 2, 3)}")
print(f"Sum: {sum_numbers(1, 2, 3, 4, 5)}")

# 7. Function with Keyword Arguments (**kwargs)
print("\n=== Function with **kwargs ===")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="Boston")

# 8. Lambda Function (Anonymous Function)
print("\n=== Lambda Function ===")

square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared}")

# 9. Docstring - Function Documentation
print("\n=== Function with Docstring ===")

def multiply(a, b):
    """
    Multiply two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    return a * b

print(f"3 * 4 = {multiply(3, 4)}")
print(multiply.__doc__)
