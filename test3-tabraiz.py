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
temperature = 38
if temperature > 38:
    print("Fever detected!")
else:
    print("Temperature is normal")
# Q2. Create variable  score = 72
#     Print the grade using these rules:
#       90 and above → "A"
#       80–89        → "B"
#       70–79        → "C"
#       60–69        → "D"
#       below 60     → "F"
#     Use if / elif / elif / elif / else
# YOUR CODE HERE
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
          
       


# Q3. Create  num = -7
#     Print whether num is: "Positive", "Negative", or "Zero"
# YOUR CODE HERE
num = -7
if num > 0:
    print("positve")
elif num < 0:
    print("Negative")
else:
    print("Zero")        

# Q4. Create  age = 20  and  has_id = True
#     A person can enter only if age >= 18 AND has_id is True.
#     Print "Entry allowed" or "Entry denied".
# YOUR CODE HERE
age = 20
has_id= True
if age >=18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")    

# Q5. Create  x = 15
#     Write this as a ONE-LINE if-else (ternary):
#     If x > 10 print "Big", else print "Small"
# YOUR CODE HERE
x = 15
print ("Big") if x > 10 else print("small")
    
# Q6. Nested if — Create  logged_in = True  and  is_admin = False
#     If logged_in:
#         If is_admin:  print "Welcome, Admin!"
#         Else:         print "Welcome, User!"
#     Else:             print "Please log in."
# YOUR CODE HERE
logged_in = True
is_admin = False
if logged_in :
    if is_admin:
        print("Welcome,Admin!")
    else:
        print("Welcome,User!")    
else:
    print("Please log in")

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


# Q8. Create  command = "quit"
#     Use match with  |  (OR) for multiple values per case:
#       "quit" | "exit" | "q"  → "Exiting program..."
#       "help" | "h"           → "Showing help..."
#       "start"                → "Starting..."
#       _                      → "Unknown command"
# YOUR CODE HERE
command = "quit"
match command: 
    case "quite" | "exit" | "q":
        print("Exiting program...")
    case "help" | "h":
        print("Showing help...")    
    case "start":
        print( "Starting...")
    case _:
        print("Unknown command")    


print("--- Section 2: Match done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — While Loops
# ──────────────────────────────────────────────────────────

# Q9. Print numbers 1 to 10 using a while loop.
# YOUR CODE HERE
numbers = 1

while numbers <= 10:
    print(numbers)
    numbers += 1 
 
# Q10. Use a while loop to find the SUM of numbers 1 to 100.
#      Print the final sum.  (should be 5050)
# YOUR CODE HERE
numbers = 1
total = 0
while numbers <= 100:
    total = total + numbers
    numbers += 1
    print(total)

# Q11. Use  continue  in a while loop to print numbers 1–10
#      but SKIP number 5.
# YOUR CODE HERE
numbers = 1
while numbers <= 10:
    numbers += 1 
    if numbers == 5:
        continue
    print(numbers)
 

# Q12. while True with break —
#      Create  attempts = 0
#      Loop forever, increment attempts each time.
#      If attempts == 3: print "Too many attempts." and break.
#      Otherwise: print f"Attempt {attempts}: wrong"
# YOUR CODE HERE
attempts = 0
while True:
    attempts = attempts + 1
    if attempts == 3:
        print("Too many attempts.")
        break
    else:
        print( f"Attempt {attempts}: wrong")

# Q13. While loop with  else —
#      Count from 1 to 5. When the loop ends naturally,
#      the else block should print "Loop finished!"
# YOUR CODE HERE
count = 1
while count <= 5:
    print(count)
    count = count+1
else:print("Loop Finished")



print("--- Section 3: While Loops done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — For Loops
# ──────────────────────────────────────────────────────────

# Q14. Loop through this list and print each item:
#animals = ["cat", "dog", "rabbit", "parrot", "fish"]
# YOUR CODE HERE
animals = ["cat", "dog", "rabbit", "parrot", "fish"]
for animal in animals:
    print(animal)


# Q15. Loop through  animals  using  enumerate()  and print:
#      0 : cat
#      1 : dog  ... etc.
# YOUR CODE HERE
for index , animal in enumerate(animals):
    print(index ,":",animal)

# Q16. Use range() — three tasks in one question:
#      a) Print 1 to 10            using range(1, 11)
#      b) Print 0, 5, 10 ... 50   using range(0, 51, 5)
#      c) Count down 10 to 1      using range(10, 0, -1)
# YOUR CODE HERE
number = 10
for number in range(1,11):
    print(number)
for number in range(0,51,5):
    print(number)
for count in range(10 ,0 ,-1 ):
    print(count)   
# Q17. Use a for loop with range to print the multiplication table of 7:
#      7 x 1 = 7
#      7 x 2 = 14  ...  7 x 10 = 70
# YOUR CODE HERE
for i in range(1,11):

    print("7 x",i, "=",7*i)

# Q18. Loop through numbers 1–20. Use  break  when you hit a number
#      divisible by both 3 AND 5 (i.e. 15).
#      Print each number before breaking, then "Found it! Stopping."
# YOUR CODE HERE
for n in range(1,21):
    if n%3 == 0 and n%5 == 0:
        print(f"{n}Found it! Stopping.")
        break
    print(n)



# Q19. Loop through numbers 1–15. Use  continue  to skip odd numbers.
#      Print only even numbers.
# YOUR CODE HERE
for i in range(1,16):
    if i%2 != 0:
        continue    
    print(i)

# Q20. Loop through  animals. If the animal is "rabbit", use  pass.
#      For all others, print the animal.
#      Add a comment explaining what pass does.
# YOUR CODE HERE
if animal in animals:
    print("rabbit")
    pass #We use pass here because if we leave an if block completely empty, the code would crash
else:
    print(animal)

# Q21. for...else —
#      Loop through  [4, 8, 12, 17, 20]  searching for an ODD number.
#      If found: print "Odd found: X" and break.
#      If loop finishes without breaking: else prints "No odd numbers found."
#numbers = [4, 8, 12, 17, 20]
# YOUR CODE HERE
numbers = [4, 8, 12, 17, 20]
for number in numbers:
 if  number%2 != 0:
    print("odd found:",number)
    break
else:
    print("No odd numbers foound")
    


# Q22. Nested loops — print this number pattern:
#      1
#      1 2
#      1 2 3
#      1 2 3 4
#      1 2 3 4 5
# YOUR CODE HERE
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()    

# Q23. Nested loops — loop through this 2D grid and print every number:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# YOUR CODE HERE
for row in grid:
    for num in row:
        print(num, end=" ")
    print()

# Q24. Loop through this dictionary and print each key + value:
student = {"name": "Bilal", "city": "Lahore", "course": "Python", "year": 2026}
# YOUR CODE HERE
for key,value in student.items():
    print(key,":",value)


# Q25. List comprehension — two tasks:
#      a) Create a list of squares for 1–10 and print it.
#         Expected: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#      b) Filter ONLY even numbers from the list below and print it.
#         Expected: [6, 12, 18, 24]
# YOUR CODE HERE
source = [3, 6, 9, 12, 15, 18, 21, 24]
number = []
for x in range(1,11):
    sq=x**2
    number.append(sq)
print(number)

for n in source:
    n%2 != 0
    source.remove(n)
print(source)

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
print("="*10, "FizzBuzz", "="*10)
for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")  
    elif i%5==0:
        print("Buzz") 
    else:
        print(i)        
    

# PART B — Exam Statistics (no sum/min/max built-ins — use loops!)
#scores = [88, 45, 72, 91, 55, 63, 78, 49, 95, 60]
# 1. Average score
# 2. Highest score
# 3. Lowest score
# 4. Count of students who passed (>= 50)
# 5. Count of students who failed (< 50)
# YOUR CODE HERE
scores = [88, 45, 72, 91, 55, 63, 78, 49, 95, 60]
t_sum = 0
highest_score=0
lowest_score=100
count_passed = 0
coount_failed = 0
for s in scores:
    t_sum += s
    if s > highest_score:
        highest_score = s
    if s<lowest_score:
        lowest_score = s
    if s >=50:
        count_passed += 1
    if s < 50:
        coount_failed +=1


print(f"Average:  {t_sum/len(scores)}") 
print(f"Highest scores: {highest_score} ")
print(f"lowest scores: {lowest_score}") 
print(f" Count of students who passed: {count_passed}") 
print(f"Count of students who failed: {coount_failed}")    


print("=== All done! Great work! ===")
