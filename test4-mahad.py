# ============================================================
#  Python Practice Test 4 — Muhammad Bilal Sajid
#  Topics covered (W3Schools order):
#    Functions · Range · Arrays · Iterators · Modules · Dates
#    Math · JSON · RegEx · PIP · Try...Except · String Formatting
#    None · User Input · Virtual Environment
#
#  Instructions:
#    - Fill in every line marked with:  # YOUR CODE HERE
#    - Do NOT delete any existing code
#    - Run the file when done: python test4.py
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — Functions
# ──────────────────────────────────────────────────────────

# Q1. Define a function  greet(name)  that prints  "Hello, <name>!"
#     Then call it with the name "Bilal".
# YOUR CODE HERE
print("Q1")
def greet(name):
    print(f"Hello, {name}!")

greet("Bilal")

# Q2. Define a function  add(a, b)  that RETURNS the sum.
#     Print the result of add(7, 5).
# YOUR CODE HERE
print("\nQ2")
def add(a, b):
    return a + b

print(f"Sum: {add(7, 5)}")

# Q3. Define a function  power(base, exp=2)  with a default argument.
#     Print power(5)  and  power(2, 3).
# YOUR CODE HERE
print("\nQ3")
def power(base, exp=2):
    return base ** exp

print(power(5))
print(power(2, 3))

# Q4. Define a function  total(*numbers)  that uses *args
#     to return the sum of any amount of numbers.
#     Print total(1, 2, 3, 4).
# YOUR CODE HERE
print("\nQ4")
def total(*numbers):
    return sum(numbers)

print(f"Total: {total(1, 2, 3, 4)}")

# Q5. Define a function  describe(**info)  that uses **kwargs
#     and prints each key and value.
#     Call describe(name="Bilal", role="Intern").
# YOUR CODE HERE
print("\nQ5")
def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe(name="Bilal", role="Intern")

# ──────────────────────────────────────────────────────────
# SECTION 2 — Range
# ──────────────────────────────────────────────────────────

# Q6. Use range() to print the numbers 1 through 5.
# YOUR CODE HERE
print("\nQ6")
for i in range(1, 6):
    print(i, end=" ")
print()

# Q7. Use range() with a step to print even numbers from 2 to 10.
# YOUR CODE HERE
print("\nQ7")
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# Q8. Use range() to print 10 down to 1 (countdown).
# YOUR CODE HERE
print("\nQ8")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ──────────────────────────────────────────────────────────
# SECTION 3 — Arrays (Lists used as arrays)
# ──────────────────────────────────────────────────────────

# Q9. Create an array  fruits = ["apple", "banana", "cherry"]
#     Print its length.
# YOUR CODE HERE
print("\nQ9")
fruits = ["apple", "banana", "cherry"]
print(f"Length: {len(fruits)}")

# Q10. Append "orange" to the array, then print the full array.
# YOUR CODE HERE
print("\nQ10")
fruits.append("orange")
print(fruits)

# Q11. Loop through the array and print each fruit on its own line.
# YOUR CODE HERE
print("\nQ11")
for fruit in fruits:
    print(fruit)

# Q12. Remove "banana" from the array and print the result.
# YOUR CODE HERE
print("\nQ12")
fruits.remove("banana")
print(fruits)

# ──────────────────────────────────────────────────────────
# SECTION 4 — Iterators
# ──────────────────────────────────────────────────────────

# Q13. Create an iterator from the tuple ("a", "b", "c") using iter().
#      Print the first two items using next().
# YOUR CODE HERE
print("\nQ13")
my_tuple = ("a", "b", "c")
my_iterator = iter(my_tuple)
print(next(my_iterator))
print(next(my_iterator))

# Q14. Loop through the iterable [10, 20, 30] using a for loop.
# YOUR CODE HERE
print("\nQ14")
for num in [10, 20, 30]:
    print(num)
print()

# ──────────────────────────────────────────────────────────
# SECTION 5 — Modules
# ──────────────────────────────────────────────────────────

# Q15. Import the  random  module and print a random integer
#      between 1 and 100 (use random.randint).
# YOUR CODE HERE
print("\nQ15")
import random
print(f"Random integer between 1 and 100: {random.randint(1, 100)}")

# Q16. Import only the  sqrt  function from the math module
#      and print sqrt(81).
# YOUR CODE HERE
print("\nQ16")
from math import sqrt
print(f"Square root of 81: {sqrt(81)}")

# ──────────────────────────────────────────────────────────
# SECTION 6 — Dates
# ──────────────────────────────────────────────────────────

# Q17. Import datetime and print the current date and time.
# YOUR CODE HERE
print("\nQ17")
import datetime
current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime}")

# Q18. Print today's year only.
# YOUR CODE HERE
print("\nQ18")
print(f"Current year: {current_datetime.year}")

# Q19. Format the current date as "DD/MM/YYYY" using strftime.
# YOUR CODE HERE
print("\nQ19")
print(f"Formatted date: {current_datetime.strftime('%d/%m/%Y')}")

# ──────────────────────────────────────────────────────────
# SECTION 7 — Math
# ──────────────────────────────────────────────────────────

# Q20. Print the largest of (3, 19, 7) using max()
#      and the smallest using min().
# YOUR CODE HERE
print("\nQ20")
print(f"Largest: {max(3, 19, 7)}")
print(f"Smallest: {min(3, 19, 7)}")

# Q21. Print the absolute value of -42 using abs().
# YOUR CODE HERE
print("\nQ21")
print(f"Absolute value of -42: {abs(-42)}")

# Q22. Using the math module, print  math.pi  and  math.ceil(4.2).
# YOUR CODE HERE
print("\nQ22")
import math
print(f"Pi: {math.pi}")
print(f"Ceiling of 4.2: {math.ceil(4.2)}")

# ──────────────────────────────────────────────────────────
# SECTION 8 — JSON
# ──────────────────────────────────────────────────────────

# Q23. Import json. Convert this Python dict to a JSON string and print it:
#      person = {"name": "Bilal", "age": 21, "intern": True}
# YOUR CODE HERE
print("\nQ23")
import json
person = {"name": "Bilal", "age": 21, "intern": True}
person_json = json.dumps(person)
print(f"Person as JSON: {person_json}")

# Q24. Convert this JSON string back into a Python dict and
#      print the value of "city":
#      data = '{"city": "Lahore", "population": 11000000}'
# YOUR CODE HERE
print("\nQ24")
data = '{"city": "Lahore", "population": 11000000}'
parsed_data = json.loads(data)
print(f"City: {parsed_data['city']}")
print(f"Population: {parsed_data['population']}")

# ──────────────────────────────────────────────────────────
# SECTION 9 — RegEx
# ──────────────────────────────────────────────────────────

# Q25. Import re. Search the string "The rain in Spain"
#      for the pattern "rain" and print whether it was found.
# YOUR CODE HERE
print("\nQ25")
import re
search_result = re.search("rain", "The rain in Spain")
if search_result:
    print("Found!")
else:
    print("Not found.")

# Q26. Use re.findall() to find all digits in "abc123def456"
#      and print the result.
# YOUR CODE HERE
print("\nQ26")
digits = re.findall(r"\d", "abc123def456")
print(f"Digits found: {digits}")

# ──────────────────────────────────────────────────────────
# SECTION 10 — PIP
# ──────────────────────────────────────────────────────────

# Q27. In a COMMENT below, write the pip command you would use
#      to install a package called  requests.
# YOUR CODE HERE
# pip install requests

# Q28. In a COMMENT below, write the pip command to list all
#      installed packages.
# YOUR CODE HERE
# pip list

# ──────────────────────────────────────────────────────────
# SECTION 11 — Try...Except
# ──────────────────────────────────────────────────────────

# Q29. Wrap  print(10 / 0)  in try/except and print
#      "Cannot divide by zero!" if a ZeroDivisionError happens.
# YOUR CODE HERE
print("\nQ29")
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Q30. Try to convert  int("hello")  inside try/except.
#      Catch the ValueError and print "Not a number".
#      Add a  finally  block that prints "Done".
# YOUR CODE HERE
print("\nQ30")
try:
    int("hello")
except ValueError:
    print("Not a number")
finally:
    print("Done")

# ──────────────────────────────────────────────────────────
# SECTION 12 — String Formatting
# ──────────────────────────────────────────────────────────

# Q31. Use an f-string to print:  "Bilal is 21 years old"
#      using variables name and age.
# YOUR CODE HERE
print("\nQ31")
name = "Bilal"
age = 21
print(f"{name} is {age} years old")

# Q32. Use the .format() method to print:
#      "Price: 50 dollars"  using a variable price = 50.
# YOUR CODE HERE
print("\nQ32")
price = 50
print("Price: {} dollars".format(price))

# Q33. Use an f-string to print the number 3.14159 rounded
#      to 2 decimal places.
# YOUR CODE HERE
print("\nQ33")
pi_val = 3.14159
print(f"{pi_val:.2f}")

# ──────────────────────────────────────────────────────────
# SECTION 13 — None
# ──────────────────────────────────────────────────────────

# Q34. Create a variable  result = None
#      Use an if statement to check  if result is None
#      and print "No value yet".
# YOUR CODE HERE
print("\nQ34")
result = None
if result is None:
    print("No value yet")

# ──────────────────────────────────────────────────────────
# SECTION 14 — User Input
# ──────────────────────────────────────────────────────────

# Q35. Ask the user for their name with input() and greet them.
#      (You may comment this out if running non-interactively.)
# YOUR CODE HERE
print("\nQ35")
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")


# Q36. Ask the user for a number, convert it to int,
#      and print the number multiplied by 2.
# YOUR CODE HERE
print("\nQ36")
user_num = int(input("Enter a number: "))
print(user_num * 2)

# ──────────────────────────────────────────────────────────
# SECTION 15 — Virtual Environment
# ──────────────────────────────────────────────────────────

# Q37. In a COMMENT below, write the command to CREATE a virtual
#      environment named  venv.
# YOUR CODE HERE
# python -m venv venv

# Q38. In a COMMENT below, write the command to ACTIVATE the
#      virtual environment on Windows.
# YOUR CODE HERE
# venv\Scripts\activate

# Q39. In a COMMENT below, write the command to DEACTIVATE a
#      virtual environment.
# YOUR CODE HERE
# deactivate

# ──────────────────────────────────────────────────────────
# BONUS — Putting it together
# ──────────────────────────────────────────────────────────

# Q40. Write a function  safe_divide(a, b)  that:
#        - returns a / b
#        - but uses try/except to return None if b is 0
#      Print safe_divide(10, 2) and safe_divide(10, 0).
# YOUR CODE HERE
print("\nQ40")
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))