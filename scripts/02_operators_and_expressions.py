# Python Basics - Operators and Expressions

# 1. Arithmetic Operators
a = 10
b = 3

addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b

print("=== Arithmetic Operators ===")
print(f"{a} + {b} = {addition}")
print(f"{a} - {b} = {subtraction}")
print(f"{a} * {b} = {multiplication}")
print(f"{a} / {b} = {division}")
print(f"{a} // {b} = {floor_division}")
print(f"{a} % {b} = {modulus}")
print(f"{a} ** {b} = {exponentiation}")

# 2. Comparison Operators
print("\n=== Comparison Operators ===")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# 3. Logical Operators
print("\n=== Logical Operators ===")
x = True
y = False

print(f"True AND False: {x and y}")
print(f"True OR False: {x or y}")
print(f"NOT True: {not x}")

# 4. Assignment Operators
print("\n=== Assignment Operators ===")
c = 5
c += 3  # c = c + 3
print(f"c += 3: {c}")

c -= 2  # c = c - 2
print(f"c -= 2: {c}")

c *= 2  # c = c * 2
print(f"c *= 2: {c}")
