# ============================================================
#  Python Practice Test 2 — Muhammad Bilal Sajid
#  Topics covered (W3Schools order):
#    Booleans · Operators · Lists · Tuples · Sets · Dictionaries
#
#  Instructions:
#    - Fill in every line marked with:  # YOUR CODE HERE
#    - Do NOT delete any existing code
#    - Run the file when done: python test2.py
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — Booleans
# ──────────────────────────────────────────────────────────

# Q1. Create two variables:  is_raining = False   is_sunny = True
#     Print both.
# YOUR CODE HERE


# Q2. Print the boolean result of these expressions (just print each one):
#     a)  10 > 5
#     b)  10 == 5
#     c)  10 < 5
#     d)  "hello" == "hello"
#     e)  "hello" == "Hello"
# YOUR CODE HERE


# Q3. Use  bool()  to evaluate these values — print each result:
#     a)  bool(0)
#     b)  bool(1)
#     c)  bool("")         ← empty string
#     d)  bool("Python")
#     e)  bool([])         ← empty list
#     f)  bool([1, 2, 3])
#     g)  bool(None)
# YOUR CODE HERE


# Q4. Create a variable  score = 75
#     Print whether score is greater than or equal to 50  (True/False)
# YOUR CODE HERE


# Q5. isinstance() returns a bool. Use it to:
#     a) Check if  3.14  is a float  → print True/False
#     b) Check if  "hello"  is an int  → print True/False
# YOUR CODE HERE


print("--- Section 1: Booleans done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Operators
# ──────────────────────────────────────────────────────────

a = 15
b = 4

# --- Arithmetic Operators ---
# Q6. Print results of:  a+b,  a-b,  a*b,  a/b,  a//b,  a%b,  a**b
# YOUR CODE HERE


# --- Comparison Operators ---
# Q7. Print results of:
#     a)  a == b
#     b)  a != b
#     c)  a > b
#     d)  a < b
#     e)  a >= b
#     f)  a <= b
# YOUR CODE HERE


# --- Logical Operators ---
# Q8. Print results of:
#     a)  a > 10 and b > 2
#     b)  a > 10 and b > 10
#     c)  a > 10 or b > 10
#     d)  not (a > 10)
# YOUR CODE HERE


# --- Assignment Operators ---
# Q9. Start with  n = 100
#     a) Use  +=  to add 20, print n
#     b) Use  -=  to subtract 10, print n
#     c) Use  *=  to multiply by 2, print n
#     d) Use  //=  to floor divide by 3, print n
#     e) Use  **=  to raise to power 2, print n
#     f) Use  %=  with 7, print n
# YOUR CODE HERE


# --- Identity Operators ---
# Q10. x = ["apple"]   y = ["apple"]   z = x
#      a) Print  x is z        → should be True  (same object)
#      b) Print  x is y        → should be False (different objects, same value)
#      c) Print  x is not y    → should be True
# YOUR CODE HERE


# --- Membership Operators ---
# Q11. fruits = ["mango", "banana", "apple"]
#      a) Print  "mango" in fruits
#      b) Print  "grape" in fruits
#      c) Print  "grape" not in fruits
# YOUR CODE HERE


# --- Bitwise Operators ---
# Q12. p = 6   q = 3
#      Print results of:  p & q,  p | q,  p ^ q,  ~p,  p << 1,  p >> 1
#      (just print the numbers — no need to explain binary)
# YOUR CODE HERE


print("--- Section 2: Operators done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — Lists
# ──────────────────────────────────────────────────────────

# Q13. Create a list  cities  with 5 city names (any cities you like).
# YOUR CODE HERE


# Q14. Print the first city using indexing.
# YOUR CODE HERE


# Q15. Print the LAST city using negative indexing.
# YOUR CODE HERE


# Q16. Print cities from index 1 to 3 (slicing).
# YOUR CODE HERE


# Q17. Change the second city (index 1) to "Lahore".
# YOUR CODE HERE


# Q18. Print the length of the list.
# YOUR CODE HERE


# Q19. Add a new city "Islamabad" to the END of the list using append().
# YOUR CODE HERE


# Q20. Insert "Multan" at index 2 using insert().
# YOUR CODE HERE


# Q21. Remove the city "Lahore" from the list using remove().
# YOUR CODE HERE


# Q22. Use  pop()  to remove and print the LAST item in the list.
# YOUR CODE HERE


# Q23. Use  pop(0)  to remove the FIRST item and print what was removed.
# YOUR CODE HERE


# Q24. Sort the list alphabetically and print it.
# YOUR CODE HERE


# Q25. Reverse the list and print it.
# YOUR CODE HERE


# Q26. Create a second list  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#      a) Print the minimum value
#      b) Print the maximum value
#      c) Print the sum of all values
# YOUR CODE HERE


# Q27. Copy the  numbers  list into a new variable  nums_copy  using copy().
#      Print nums_copy.
# YOUR CODE HERE


# Q28. Check if  5  is in  numbers  and print True or False.
# YOUR CODE HERE


# Q29. Count how many times  1  appears in  numbers.
# YOUR CODE HERE


# Q30. Use  extend()  to join  cities  and  numbers  into  cities  list.
#      Print the result.
# YOUR CODE HERE


# Q31. Clear the entire  cities  list using clear() and print it.
#      (should print an empty list: [])
# YOUR CODE HERE


print("--- Section 3: Lists done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Tuples
# ──────────────────────────────────────────────────────────

# Q32. Create a tuple  colors  with 5 color names.
# YOUR CODE HERE


# Q33. Print the first and last color using indexing.
# YOUR CODE HERE


# Q34. Try to change the second color to "pink".
#      It will crash — write the error name as a comment instead of running it.
#      Then explain in a comment WHY tuples cannot be changed.
# YOUR CODE HERE  (comments only, no crash)


# Q35. Print the length of  colors  using len().
# YOUR CODE HERE


# Q36. Check if "red" is in  colors  and print True or False.
# YOUR CODE HERE


# Q37. Count how many times "blue" appears in this tuple:
counts_tuple = ("blue", "red", "blue", "green", "blue")
# YOUR CODE HERE


# Q38. Find the index of "green" in  counts_tuple.
# YOUR CODE HERE


# Q39. Unpack the tuple  point = (10, 20, 30)  into three variables x, y, z.
#      Print each variable separately.
# YOUR CODE HERE


# Q40. Convert  colors  tuple into a list, add "purple", then convert back to tuple.
#      Print the final tuple.
# YOUR CODE HERE


# Q41. Create a SINGLE-ITEM tuple  single = ("only",)
#      Print it and print its type.
#      (remember: a trailing comma is required!)
# YOUR CODE HERE


# Q42. Loop through  colors  and print each color on a new line.
# YOUR CODE HERE


print("--- Section 4: Tuples done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Sets
# ──────────────────────────────────────────────────────────

# Q43. Create a set  team_a = {"Alice", "Bob", "Charlie", "Diana"}
# YOUR CODE HERE


# Q44. Print the length of  team_a.
# YOUR CODE HERE


# Q45. Add "Eve" to  team_a  using add().
# YOUR CODE HERE


# Q46. Try adding "Bob" again — print the set. What do you notice?
#      Write a comment explaining why duplicates don't appear in sets.
# YOUR CODE HERE


# Q47. Remove "Charlie" using remove() and print the set.
# YOUR CODE HERE


# Q48. Use discard() to try removing "Zara" (who is NOT in the set).
#      Print the set. (discard() won't crash unlike remove())
# YOUR CODE HERE


# Q49. Create  team_b = {"Charlie", "Diana", "Frank", "Grace"}
# YOUR CODE HERE


# Q50. Print the UNION of team_a and team_b  (all members from both).
# YOUR CODE HERE


# Q51. Print the INTERSECTION of team_a and team_b  (members in BOTH teams).
# YOUR CODE HERE


# Q52. Print the DIFFERENCE  team_a - team_b  (in a but not in b).
# YOUR CODE HERE


# Q53. Print the SYMMETRIC DIFFERENCE  (members in either team, but NOT both).
# YOUR CODE HERE


# Q54. Check if  {"Diana"}  is a SUBSET of  team_a.  Print True or False.
# YOUR CODE HERE


# Q55. Convert the list  [1, 2, 2, 3, 3, 3, 4]  to a set to remove duplicates.
#      Print the result.
# YOUR CODE HERE


print("--- Section 5: Sets done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Dictionaries
# ──────────────────────────────────────────────────────────

# Q56. Create a dictionary  student  with these keys:
#        name, age, city, course, is_intern
#      Fill in your own values.
# YOUR CODE HERE


# Q57. Print the value of the  "name"  key.
# YOUR CODE HERE


# Q58. Print the value of  "city"  using the  .get()  method.
# YOUR CODE HERE


# Q59. Add a new key  "score"  with value  88  to  student.
# YOUR CODE HERE


# Q60. Update the  "city"  value to  "Lahore".
# YOUR CODE HERE


# Q61. Delete the  "score"  key using  del.
# YOUR CODE HERE


# Q62. Print ALL keys of  student  using  .keys()
# YOUR CODE HERE


# Q63. Print ALL values of  student  using  .values()
# YOUR CODE HERE


# Q64. Print ALL key-value pairs using  .items()
# YOUR CODE HERE


# Q65. Check if  "age"  exists as a key in  student.  Print True or False.
# YOUR CODE HERE


# Q66. Check if  "grade"  exists as a key in  student.  Print True or False.
# YOUR CODE HERE


# Q67. Print the number of keys in  student  using  len().
# YOUR CODE HERE


# Q68. Loop through  student  and print each key and its value like:
#      name  :  Bilal
#      age   :  22
#      ...
# YOUR CODE HERE


# Q69. Use  pop("is_intern")  to remove that key and print what was returned.
# YOUR CODE HERE


# Q70. Create a NESTED dictionary  company  like this structure:
#      company = {
#          "name": "PITB",
#          "location": "Lahore",
#          "department": {
#              "name": "Data Center",
#              "employees": 10
#          }
#      }
#      Then print:
#        a) The company name
#        b) The department name  (nested access)
#        c) Number of employees  (nested access)
# YOUR CODE HERE


# Q71. Copy  student  into  student_backup  using  .copy()
#      Change "age" in  student  to 99.
#      Print age from BOTH dictionaries to show the copy is independent.
# YOUR CODE HERE


# Q72. Use  .update()  to merge this data into  student:
#      {"grade": "A", "graduation_year": 2026}
#      Print the updated student dictionary.
# YOUR CODE HERE


print("--- Section 6: Dictionaries done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS — Mini Project
# ──────────────────────────────────────────────────────────

# Build a simple Student Report using everything from this test.
#
# 1. Create a dictionary  report  with keys:
#       name, subjects (a LIST of 3 subject names),
#       marks (a TUPLE of 3 marks matching each subject),
#       passed (a SET of subjects where mark >= 50)
#
# 2. Print a formatted report like:
#    ================================
#     Student Report
#    ================================
#     Name    : Bilal
#     Subjects: Math, Science, English
#     Marks   : 80, 45, 72
#     Passed  : {'Math', 'English'}
#     Average : 65.67
#    ================================
#
# Hints:
#   - Use zip(subjects, marks) to pair them
#   - Use sum() and len() for average
#   - Use an f-string for formatting

# YOUR CODE HERE


print("=== All done! Great work! ===")
