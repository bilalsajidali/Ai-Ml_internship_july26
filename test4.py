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



# Q2. Define a function  add(a, b)  that RETURNS the sum.
#     Print the result of add(7, 5).
# YOUR CODE HERE



# Q3. Define a function  power(base, exp=2)  with a default argument.
#     Print power(5)  and  power(2, 3).
# YOUR CODE HERE



# Q4. Define a function  total(*numbers)  that uses *args
#     to return the sum of any amount of numbers.
#     Print total(1, 2, 3, 4).
# YOUR CODE HERE



# Q5. Define a function  describe(**info)  that uses **kwargs
#     and prints each key and value.
#     Call describe(name="Bilal", role="Intern").
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 2 — Range
# ──────────────────────────────────────────────────────────

# Q6. Use range() to print the numbers 1 through 5.
# YOUR CODE HERE



# Q7. Use range() with a step to print even numbers from 2 to 10.
# YOUR CODE HERE



# Q8. Use range() to print 10 down to 1 (countdown).
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 3 — Arrays (Lists used as arrays)
# ──────────────────────────────────────────────────────────

# Q9. Create an array  fruits = ["apple", "banana", "cherry"]
#     Print its length.
# YOUR CODE HERE



# Q10. Append "orange" to the array, then print the full array.
# YOUR CODE HERE



# Q11. Loop through the array and print each fruit on its own line.
# YOUR CODE HERE



# Q12. Remove "banana" from the array and print the result.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 4 — Iterators
# ──────────────────────────────────────────────────────────

# Q13. Create an iterator from the tuple ("a", "b", "c") using iter().
#      Print the first two items using next().
# YOUR CODE HERE



# Q14. Loop through the iterable [10, 20, 30] using a for loop.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 5 — Modules
# ──────────────────────────────────────────────────────────

# Q15. Import the  random  module and print a random integer
#      between 1 and 100 (use random.randint).
# YOUR CODE HERE



# Q16. Import only the  sqrt  function from the math module
#      and print sqrt(81).
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 6 — Dates
# ──────────────────────────────────────────────────────────

# Q17. Import datetime and print the current date and time.
# YOUR CODE HERE



# Q18. Print today's year only.
# YOUR CODE HERE



# Q19. Format the current date as "DD/MM/YYYY" using strftime.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 7 — Math
# ──────────────────────────────────────────────────────────

# Q20. Print the largest of (3, 19, 7) using max()
#      and the smallest using min().
# YOUR CODE HERE



# Q21. Print the absolute value of -42 using abs().
# YOUR CODE HERE



# Q22. Using the math module, print  math.pi  and  math.ceil(4.2).
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 8 — JSON
# ──────────────────────────────────────────────────────────

# Q23. Import json. Convert this Python dict to a JSON string and print it:
#      person = {"name": "Bilal", "age": 21, "intern": True}
# YOUR CODE HERE



# Q24. Convert this JSON string back into a Python dict and
#      print the value of "city":
#      data = '{"city": "Lahore", "population": 11000000}'
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 9 — RegEx
# ──────────────────────────────────────────────────────────

# Q25. Import re. Search the string "The rain in Spain"
#      for the pattern "rain" and print whether it was found.
# YOUR CODE HERE



# Q26. Use re.findall() to find all digits in "abc123def456"
#      and print the result.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 10 — PIP
# ──────────────────────────────────────────────────────────

# Q27. In a COMMENT below, write the pip command you would use
#      to install a package called  requests.
# YOUR CODE HERE

# Q28. In a COMMENT below, write the pip command to list all
#      installed packages.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 11 — Try...Except
# ──────────────────────────────────────────────────────────

# Q29. Wrap  print(10 / 0)  in try/except and print
#      "Cannot divide by zero!" if a ZeroDivisionError happens.
# YOUR CODE HERE



# Q30. Try to convert  int("hello")  inside try/except.
#      Catch the ValueError and print "Not a number".
#      Add a  finally  block that prints "Done".
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 12 — String Formatting
# ──────────────────────────────────────────────────────────

# Q31. Use an f-string to print:  "Bilal is 21 years old"
#      using variables name and age.
# YOUR CODE HERE



# Q32. Use the .format() method to print:
#      "Price: 50 dollars"  using a variable price = 50.
# YOUR CODE HERE



# Q33. Use an f-string to print the number 3.14159 rounded
#      to 2 decimal places.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 13 — None
# ──────────────────────────────────────────────────────────

# Q34. Create a variable  result = None
#      Use an if statement to check  if result is None
#      and print "No value yet".
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 14 — User Input
# ──────────────────────────────────────────────────────────

# Q35. Ask the user for their name with input() and greet them.
#      (You may comment this out if running non-interactively.)
# YOUR CODE HERE



# Q36. Ask the user for a number, convert it to int,
#      and print the number multiplied by 2.
# YOUR CODE HERE



# ──────────────────────────────────────────────────────────
# SECTION 15 — Virtual Environment
# ──────────────────────────────────────────────────────────

# Q37. In a COMMENT below, write the command to CREATE a virtual
#      environment named  venv.
# YOUR CODE HERE

# Q38. In a COMMENT below, write the command to ACTIVATE the
#      virtual environment on Windows.
# YOUR CODE HERE

# Q39. In a COMMENT below, write the command to DEACTIVATE a
#      virtual environment.
# YOUR CODE HERE


# ──────────────────────────────────────────────────────────
# BONUS — Putting it together
# ──────────────────────────────────────────────────────────

# Q40. Write a function  safe_divide(a, b)  that:
#        - returns a / b
#        - but uses try/except to return None if b is 0
#      Print safe_divide(10, 2) and safe_divide(10, 0).
# YOUR CODE HERE
