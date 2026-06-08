# Python Basics - Control Flow (If, Elif, Else)

# 1. If Statement
print("=== If Statement ===")
age = 18

if age >= 18:
    print("You are an adult")

# 2. If-Else Statement
print("\n=== If-Else Statement ===")
temperature = 15

if temperature > 20:
    print("It's warm outside")
else:
    print("It's cold outside")

# 3. If-Elif-Else Statement
print("\n=== If-Elif-Else Statement ===")
score = 75

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# 4. Nested If Statements
print("\n=== Nested If Statements ===")
is_member = True
purchase_amount = 100

if is_member:
    if purchase_amount > 50:
        discount = 0.2  # 20% discount
        final_price = purchase_amount * (1 - discount)
        print(f"Member discount applied! Final price: ${final_price}")
    else:
        print("Purchase minimum not met for discount")
else:
    print("Not a member")

# 5. Using Comparison in Conditionals
print("\n=== Using Comparisons in Conditionals ===")
num = 15

if num > 10 and num < 20:
    print(f"{num} is between 10 and 20")

if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
