# ============================================================
#  Python Practice Test 3 — Muhammad Bilal Sajid
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — If ... Else
# ──────────────────────────────────────────────────────────

# Q1
temperature = 38

if temperature > 37:
    print("Fever detected!")
else:
    print("Temperature is normal.")


# Q2
score = 72

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# Q3
num = -7

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q4
age = 20
has_id = True

if age >= 18 and has_id == True:
    print("Entry allowed")
else:
    print("Entry denied")


# Q5
x = 15
print("Big") if x > 10 else print("Small")


# Q6
logged_in = True
is_admin = False

if logged_in:
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in.")


print("--- Section 1: If...Else done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Match
# ──────────────────────────────────────────────────────────

# Q7
http_code = 404

match http_code:
    case 200:
        print("OK")
    case 301:
        print("Moved Permanently")
    case 404:
        print("Not Found")
    case 500:
        print("Internal Server Error")
    case _:
        print("Unknown status code")


# Q8
command = "quit"

match command:
    case "quit" | "exit" | "q":
        print("Exiting program...")
    case "help" | "h":
        print("Showing help...")
    case "start":
        print("Starting...")
    case _:
        print("Unknown command")


print("--- Section 2: Match done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — While Loops
# ──────────────────────────────────────────────────────────

# Q9
i = 1

while i <= 10:
    print(i)
    i = i + 1


# Q10
i = 1
total = 0

while i <= 100:
    total = total + i
    i = i + 1

print(total)


# Q11
i = 0

while i < 10:
    i = i + 1

    if i == 5:
        continue

    print(i)


# Q12
attempts = 0

while True:
    attempts = attempts + 1

    if attempts == 3:
        print("Too many attempts.")
        break
    else:
        print(f"Attempt {attempts}: wrong")


# Q13
count = 1

while count <= 5:
    print(count)
    count = count + 1
else:
    print("Loop finished!")


print("--- Section 3: While Loops done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — For Loops
# ──────────────────────────────────────────────────────────

# Q14
animals = ["cat", "dog", "rabbit", "parrot", "fish"]

for animal in animals:
    print(animal)


# Q15
for index, animal in enumerate(animals):
    print(index, ":", animal)


# Q16

# a
for i in range(1, 11):
    print(i)

# b
for i in range(0, 51, 5):
    print(i)

# c
for i in range(10, 0, -1):
    print(i)


# Q17
for i in range(1, 11):
    print("7 x", i, "=", 7 * i)


# Q18
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("Found it! Stopping.")
        break
    print(i)


# Q19
for i in range(1, 16):

    if i % 2 != 0:
        continue

    print(i)


# Q20
for animal in animals:

    if animal == "rabbit":
        pass    # pass does nothing and moves to the next statement

    else:
        print(animal)


# Q21
numbers = [4, 8, 12, 17, 20]

for num in numbers:
    if num % 2 != 0:
        print("Odd found:", num)
        break
else:
    print("No odd numbers found.")


# Q22
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# Q23
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
    for num in row:
        print(num)


# Q24
student = {
    "name": "Bilal",
    "city": "Lahore",
    "course": "Python",
    "year": 2026
}

for key, value in student.items():
    print(key, ":", value)


# Q25
source = [3, 6, 9, 12, 15, 18, 21, 24]

# a
squares = [x * x for x in range(1, 11)]
print(squares)

# b
even_numbers = [x for x in source if x % 2 == 0]
print(even_numbers)


print("--- Section 4: For Loops done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS
# ──────────────────────────────────────────────────────────

# PART A
for i in range(1, 51):

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)


# PART B

scores = [88, 45, 72, 91, 55, 63, 78, 49, 95, 60]

total = 0
highest = scores[0]
lowest = scores[0]
passed = 0
failed = 0

for score in scores:

    total = total + score

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    if score >= 50:
        passed = passed + 1
    else:
        failed = failed + 1

average = total / len(scores)

print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)
print("Passed:", passed)
print("Failed:", failed)


print("=== All done! Great work! ===")