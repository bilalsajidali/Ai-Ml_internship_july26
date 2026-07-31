# ============================================================
#  Python Practice Test 3 — Muhammad Bilal Sajid
#  Topics covered (W3Schools order):
#    If...Else · Match · While Loops · For Loops
#    (includes: elif, nested if, break, continue, pass,
#               range(), nested loops, else on loops)
#
#  Instructions:
#    - Fill in every line marked with:  # YOUR CODE HERE
#    - Do NOT delete any existing code
#    - Run the file when done: python test3.py
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — If ... Else
# ──────────────────────────────────────────────────────────

# Q1. Create variable  temperature = 38
#     If temperature > 37, print "Fever detected!"
#     Otherwise print "Temperature is normal."
# YOUR CODE HERE
print("Q1")
temperature = 38
if temperature > 37:
    print("Fever detected!\n")
else:
    print("Temperature is normal.\n")

# Q2. Create variable  score = 72
#     Print the grade using these rules:
#       90 and above → "A"
#       80–89        → "B"
#       70–79        → "C"
#       60–69        → "D"
#       below 60     → "F"
#     Use if / elif / elif / elif / else
# YOUR CODE HERE
print("Q2")
score = 72
if score >= 90:
    print("A\n")
elif score >= 80:
    print("B\n")
elif score >= 70:
    print("C\n")
elif score >= 60:
    print("D\n")
else:
    print("F\n")

# Q3. Create  num = -7
#     Print whether num is: "Positive", "Negative", or "Zero"
# YOUR CODE HERE
print("Q3")
num = -7
if num > 0:
    print("Positive\n")
elif num < 0:
    print("Negative\n")
else:
    print("Zero\n")

# Q4. Create  age = 20  and  has_id = True
#     A person can enter only if age >= 18 AND has_id is True.
#     Print "Entry allowed" or "Entry denied".
# YOUR CODE HERE
print("Q4")
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed\n")
else:
    print("Entry denied\n")

# Q5. Create  x = 15
#     Write this as a ONE-LINE if-else (ternary):
#     If x > 10 print "Big", else print "Small"
# YOUR CODE HERE
print("Q5")
x = 15
print("Big\n") if x > 10 else print("Small\n")

# Q6. Nested if — Create  logged_in = True  and  is_admin = False
#     If logged_in:
#         If is_admin:  print "Welcome, Admin!"
#         Else:         print "Welcome, User!"
#     Else:             print "Please log in."
# YOUR CODE HERE
print("Q6")
logged_in = True
is_admin = False
if logged_in:
    if is_admin:
        print("Welcome, Admin!\n")
    else:
        print("Welcome, User!\n")
else:
    print("Please log in.\n\n")

print("--- Section 1: If...Else done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Match (Python 3.10+)
# ──────────────────────────────────────────────────────────

# Q7. Create  http_code = 404
#     Use a match statement:
#       200 → "OK"
#       301 → "Moved Permanently"
#       404 → "Not Found"
#       500 → "Internal Server Error"
#       _   → "Unknown status code"
# YOUR CODE HERE
print("Q7")
http_code = 404
match http_code:
    case 200:
        print("OK\n")
    case 301:
        print("Moved Permanently\n")
    case 404:
        print("Not Found\n")
    case 500:
        print("Internal Server Error\n")
    case _:
        print("Unknown status code\n")

# Q8. Create  command = "quit"
#     Use match with  |  (OR) for multiple values per case:
#       "quit" | "exit" | "q"  → "Exiting program..."
#       "help" | "h"           → "Showing help..."
#       "start"                → "Starting..."
#       _                      → "Unknown command"
# YOUR CODE HERE
print("Q8")
command = "quit"
match command:
    case "quit" | "exit" | "q":
        print("Exiting program...\n")
    case "help" | "h":
        print("Showing help...\n")
    case "start":
        print("Starting...\n")
    case _:
        print("Unknown command\n")

print("--- Section 2: Match done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — While Loops
# ──────────────────────────────────────────────────────────

# Q9. Print numbers 1 to 10 using a while loop.
# YOUR CODE HERE
print("Q9")
i = 1
while i <= 10:
    print(i,end=" ")
    i += 1
print("\n")  

# Q10. Use a while loop to find the SUM of numbers 1 to 100.
#      Print the final sum.  (should be 5050)
# YOUR CODE HERE
print("Q10")
total = 0
j = 1
while j <= 100:
    total += j
    j += 1
print(f"Sum of 1 to 100 is: {total}\n")

# Q11. Use  continue  in a while loop to print numbers 1–10
#      but SKIP number 5.
# YOUR CODE HERE
print("Q11")
k = 0
while k < 10:
    k += 1
    if k == 5:
        continue
    print(k,end=" ")
print("\n")  

# Q12. while True with break —
#      Create  attempts = 0
#      Loop forever, increment attempts each time.
#      If attempts == 3: print "Too many attempts." and break.
#      Otherwise: print f"Attempt {attempts}: wrong"
# YOUR CODE HERE
print("Q12")
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("Too many attempts.")
        break
    print(f"Attempt {attempts}: wrong")
print()  

# Q13. While loop with  else —
#      Count from 1 to 5. When the loop ends naturally,
#      the else block should print "Loop finished!"
# YOUR CODE HERE
print("Q13")
count = 1
while count <= 5:
    print(count,end=" ")
    count += 1
else:
    print("\nLoop finished!\n")

print("--- Section 3: While Loops done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — For Loops
# ──────────────────────────────────────────────────────────

# Q14. Loop through this list and print each item:
animals = ["cat", "dog", "rabbit", "parrot", "fish"]
# YOUR CODE HERE
print("Q14")
for animal in animals:
    print(animal,end=" ")
print("\n")  

# Q15. Loop through  animals  using  enumerate()  and print:
#      0 : cat
#      1 : dog  ... etc.
# YOUR CODE HERE
print("Q15")
for index, animal in enumerate(animals):
    print(f"{index} : {animal}")
print()    

# Q16. Use range() — three tasks in one question:
#      a) Print 1 to 10            using range(1, 11)
#      b) Print 0, 5, 10 ... 50   using range(0, 51, 5)
#      c) Count down 10 to 1      using range(10, 0, -1)
# YOUR CODE HERE
print("Q16")
print("a)", end=" ")
for i in range(1, 11):
    print(i, end=" ")
print()
print("b)", end=" ")
for i in range(0, 51, 5):
    print(i, end=" ")
print()
print("c)", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print("\n")  

# Q17. Use a for loop with range to print the multiplication table of 7:
#      7 x 1 = 7
#      7 x 2 = 14  ...  7 x 10 = 70
# YOUR CODE HERE
print("Q17")
for i in range(1, 11):
    print(f"7 x {i} = {7 * i}")
print()

# Q18. Loop through numbers 1–20. Use  break  when you hit a number
#      divisible by both 3 AND 5 (i.e. 15).
#      Print each number before breaking, then "Found it! Stopping."
# YOUR CODE HERE
print("Q18")
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print(f"\n{i} Found it! Stopping.")
        break
    print(f"{i}",end=" ")
print("\n")  

# Q19. Loop through numbers 1–15. Use  continue  to skip odd numbers.
#      Print only even numbers.
# YOUR CODE HERE
print("Q19")
for i in range(1, 16):
    if i % 2 != 0:
        continue
    print(f"{i}",end=" ")
print("\n")  

# Q20. Loop through  animals. If the animal is "rabbit", use  pass.
#      For all others, print the animal.
#      Add a comment explaining what pass does.
# YOUR CODE HERE
print("Q20")
for animal in animals:
    if animal == "rabbit":
        pass  # We use pass here because if we leave an if block completely empty, the code would crash and give a syntax error. pass means do nothing
    else:
        print(animal,end=" ")
print("\n")  

# Q21. for...else —
#      Loop through  [4, 8, 12, 17, 20]  searching for an ODD number.
#      If found: print "Odd found: X" and break.
#      If loop finishes without breaking: else prints "No odd numbers found."
numbers = [4, 8, 12, 17, 20]
# YOUR CODE HERE
print("Q21")
for num in numbers:
    if num % 2 != 0:
        print(f"Odd found: {num}/n")
        break
else:
    print("No odd numbers found.\n")
print()

# Q22. Nested loops — print this number pattern:
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5
# YOUR CODE HERE
print("Q22")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
print("\n")  

# Q23. Nested loops — loop through this 2D grid and print every number:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# YOUR CODE HERE
print("Q23")
for row in grid:
    for num in row:
        print(num, end=" ")
print("\n")  

# Q24. Loop through this dictionary and print each key + value:
student = {"name": "Bilal", "city": "Lahore", "course": "Python", "year": 2026}
# YOUR CODE HERE
print("Q24")    
for key, value in student.items():
    print(f"{key}: {value}")
print()

# Q25. List comprehension — two tasks:
#      a) Create a list of squares for 1–10 and print it.
#         Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#      b) Filter ONLY even numbers from the list below and print it.
#         Expected: [6, 12, 18, 24]
source = [3, 6, 9, 12, 15, 18, 21, 24]
# YOUR CODE HERE
print("Q25")
squares = [i ** 2 for i in range(1, 11)]
print("a)",squares)
evens = [num for num in source if num % 2 == 0]
print("b)",evens)

print("--- Section 4: For Loops done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS — Mini Project: FizzBuzz + Score Stats
# ──────────────────────────────────────────────────────────

# PART A — FizzBuzz
# Loop through 1 to 50:
#   divisible by 3 AND 5 → "FizzBuzz"
#   divisible by 3 only  → "Fizz"
#   divisible by 5 only  → "Buzz"
#   otherwise            → the number
# YOUR CODE HERE
print("--- FIZZBUZZ ---")
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"Index {i} -> FizzBuzz")
    elif i % 3 == 0:
        print(f"Index {i} -> Fizz")
    elif i % 5 == 0:
        print(f"Index {i} -> Buzz")
    else:
        print(f"Index {i} -> {i}")

# PART B — Exam Statistics (no sum/min/max built-ins — use loops!)
scores = [88, 45, 72, 91, 55, 63, 78, 49, 95, 60]
# 1. Average score
# 2. Highest score
# 3. Lowest score
# 4. Count of students who passed (>= 50)
# 5. Count of students who failed (< 50)
# YOUR CODE HERE
print("\n--- EXAM STATS ---")
total_score = 0
highest_score = scores[0]
lowest_score = scores[0]
passed_count = 0
failed_count = 0
score_count = 0

for score in scores:
    total_score += score
    score_count += 1
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score
    if score >= 50:
        passed_count += 1
    else:
        failed_count += 1

average_score = total_score / score_count

print(f"Average Score: {average_score}")
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")

print("=== All done! Great work! ===")