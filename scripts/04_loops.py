# Python Basics - Loops (For and While)

# 1. For Loop - Iterating over a list
print("=== For Loop - List Iteration ===")
fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    print(f"I like {fruit}")

# 2. For Loop - Using range()
print("\n=== For Loop - Range ===")
for i in range(1, 6):
    print(f"Count: {i}")

# 3. For Loop - With step
print("\n=== For Loop - Range with Step ===")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# 4. For Loop - Enumerate (getting index and value)
print("\n=== For Loop - Enumerate ===")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# 5. While Loop
print("\n=== While Loop ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# 6. While Loop with Break
print("\n=== While Loop with Break ===")
num = 0
while num < 10:
    if num == 5:
        break  # Exit the loop
    print(num, end=" ")
    num += 1
print()

# 7. While Loop with Continue
print("\n=== While Loop with Continue ===")
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skip this iteration
    print(num, end=" ")
print()

# 8. Nested Loops
print("\n=== Nested Loops ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# 9. For-Else (else runs if loop completes without break)
print("\n=== For-Else ===")
for i in range(1, 6):
    if i == 10:
        break
else:
    print("Loop completed successfully!")
