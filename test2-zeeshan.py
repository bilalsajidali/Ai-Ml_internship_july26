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
is_raining=False
is_sunny=True
print(is_raining)
print(is_sunny)


# Q2. Print the boolean result of these expressions (just print each one):
#     a)  10 > 5
#     b)  10 == 5
#     c)  10 < 5
#     d)  "hello" == "hello"
#     e)  "hello" == "Hello"
# YOUR CODE HERE
print(10>5)
print(10==5)
print(10<5)
print("hello" == "hello")
print("hello" == "Hello")


# Q3. Use  bool()  to evaluate these values — print each result:
#     a)  bool(0)
#     b)  bool(1)
#     c)  bool("")         ← empty string
#     d)  bool("Python")
#     e)  bool([])         ← empty list
#     f)  bool([1, 2, 3])
#     g)  bool(None)
# YOUR CODE HERE
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("python"))
print(bool([]))
print(bool([1,2,3]))
print(bool(None))


# Q4. Create a variable  score = 75
#     Print whether score is greater than or equal to 50  (True/False)
# YOUR CODE HERE
score = 75
print(score >= 50)


# Q5. isinstance() returns a bool. Use it to:
#     a) Check if  3.14  is a float  → print True/False
#     b) Check if  "hello"  is an int  → print True/False
# YOUR CODE HERE
print(isinstance(3.14, float))
print(isinstance("hello", int))

print("--- Section 1: Booleans done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Operators
# ──────────────────────────────────────────────────────────

a = 15
b = 4

# --- Arithmetic Operators ---
# Q6. Print results of:  a+b,  a-b,  a*b,  a/b,  a//b,  a%b,  a**b
# YOUR CODE HERE
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

# --- Comparison Operators ---
# Q7. Print results of:
#     a)  a == b
#     b)  a != b
#     c)  a > b
#     d)  a < b
#     e)  a >= b
#     f)  a <= b
# YOUR CODE HERE
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# --- Logical Operators ---
# Q8. Print results of:
#     a)  a > 10 and b > 2
#     b)  a > 10 and b > 10
#     c)  a > 10 or b > 10
#     d)  not (a > 10)
# YOUR CODE HERE
print( a > 10 and b > 2)
print(a > 10 and b > 10)
print(a > 10 or b > 10)
print(not (a > 10))

# --- Assignment Operators ---
# Q9. Start with  n = 100
#     a) Use  +=  to add 20, print n
#     b) Use  -=  to subtract 10, print n
#     c) Use  *=  to multiply by 2, print n
#     d) Use  //=  to floor divide by 3, print n
#     e) Use  **=  to raise to power 2, print n
#     f) Use  %=  with 7, print n
# YOUR CODE HERE
n=100
n+=20
print(n)
n-=10
print(n)
n*=2
print(n)
n//=3
print(n)
n**=2
print(n)
n%=7
print(n)


# --- Identity Operators ---
# Q10. x = ["apple"]   y = ["apple"]   z = x
#      a) Print  x is z        → should be True  (same object)
#      b) Print  x is y        → should be False (different objects, same value)
#      c) Print  x is not y    → should be True
# YOUR CODE HERE
x = ["apple"]
y = ["apple"]
z = x
print(x is z)
print(x is y)
print(x is not y)


# --- Membership Operators ---
# Q11. fruits = ["mango", "banana", "apple"]
#      a) Print  "mango" in fruits
#      b) Print  "grape" in fruits
#      c) Print  "grape" not in fruits
# YOUR CODE HERE
fruits = ["mango", "banana", "apple"]
print("mango" in fruits)
print("grape" in fruits)
print("grape" not in fruits)


# --- Bitwise Operators ---
# Q12. p = 6   q = 3
#      Print results of:  p & q,  p | q,  p ^ q,  ~p,  p << 1,  p >> 1
#      (just print the numbers — no need to explain binary)
# YOUR CODE HERE
p = 6
q = 3
print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(p << 1)
print(p >> 1)

print("--- Section 2: Operators done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — Lists
# ──────────────────────────────────────────────────────────

# Q13. Create a list  cities  with 5 city names (any cities you like).
# YOUR CODE HERE
cities = ["lahore", "karachi", "Islamabad", "Bahawalpur", "Multan"]

# Q14. Print the first city using indexing.
# YOUR CODE HERE
print(cities[0])

# Q15. Print the LAST city using negative indexing.
# YOUR CODE HERE
print(cities[-1])

# Q16. Print cities from index 1 to 3 (slicing).
# YOUR CODE HERE
print(cities[1:3])

# Q17. Change the second city (index 1) to "Lahore".
# YOUR CODE HERE
cities[1] = "Lahore"
print(cities)

# Q18. Print the length of the list.
# YOUR CODE HERE
print(len(cities))

# Q19. Add a new city "Islamabad" to the END of the list using append().
# YOUR CODE HERE
cities.append("Islamabad")
print(cities)

# Q20. Insert "Multan" at index 2 using insert().
# YOUR CODE HERE
cities.insert(2, "Multan")
print(cities)

# Q21. Remove the city "Lahore" from the list using remove().
# YOUR CODE HERE
cities.remove("Lahore")
print(cities)

# Q22. Use  pop()  to remove and print the LAST item in the list.
# YOUR CODE HERE
print(cities.pop())
print(cities)

# Q23. Use  pop(0)  to remove the FIRST item and print what was removed.
# YOUR CODE HERE
print(cities.pop(0))
print(cities)

# Q24. Sort the list alphabetically and print it.
# YOUR CODE HERE
cities.sort()
print(cities)

# Q25. Reverse the list and print it.
# YOUR CODE HERE
cities.reverse()
print(cities)

# Q26. Create a second list  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#      a) Print the minimum value
#      b) Print the maximum value
#      c) Print the sum of all values
# YOUR CODE HERE
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Q27. Copy the  numbers  list into a new variable  nums_copy  using copy().
#      Print nums_copy.
# YOUR CODE HERE
nums_copy = numbers.copy()
print(nums_copy)

# Q28. Check if  5  is in  numbers  and print True or False.
# YOUR CODE HERE
print(5 in numbers)

# Q29. Count how many times  1  appears in  numbers.
# YOUR CODE HERE
print(numbers.count(1))

# Q30. Use  extend()  to join  cities  and  numbers  into  cities  list.
#      Print the result.
# YOUR CODE HERE
cities.extend(numbers)
print(cities)

# Q31. Clear the entire  cities  list using clear() and print it.
#      (should print an empty list: [])
# YOUR CODE HERE
cities.clear()
print(cities)


print("--- Section 3: Lists done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Tuples
# ──────────────────────────────────────────────────────────

# Q32. Create a tuple  colors  with 5 color names.
# YOUR CODE HERE
colors=("blue","green","white","black","red")


# Q33. Print the first and last color using indexing.
# YOUR CODE HERE
print(colors[0])
print(colors[4])

# Q34. Try to change the second color to "pink".
#      It will crash — write the error name as a comment instead of running it.
#      Then explain in a comment WHY tuples cannot be changed.
# YOUR CODE HERE  (comments only, no crash)
"""TypeError tuple does not support the item assignment
tuples are immutable it means we cannot change 
the item value once we have created"""
 
# Q35. Print the length of  colors  using len().
# YOUR CODE HERE
print(len(colors))

# Q36. Check if "red" is in  colors  and print True or False.
# YOUR CODE HERE

print("red" in colors)
# Q37. Count how many times "blue" appears in this tuple:
counts_tuple = ("blue", "red", "blue", "green", "blue")
# YOUR CODE HERE
print(counts_tuple.count("blue"))

# Q38. Find the index of "green" in  counts_tuple.
# YOUR CODE HERE
print(counts_tuple.index("green"))

# Q39. Unpack the tuple  point = (10, 20, 30)  into three variables x, y, z.
#      Print each variable separately.
# YOUR CODE HERE
point = (10, 20, 30)
x,y,z=point
print(x)
print(y)
print(z)

# Q40. Convert  colors  tuple into a list, add "purple", then convert back to tuple.
#      Print the final tuple.
# YOUR CODE HERE
colors_list = list(colors)
colors_list.append("purple")
colors = tuple(colors_list)
print(colors)

# Q41. Create a SINGLE-ITEM tuple  single = ("only",)
#      Print it and print its type.
single=("only",)
print(single)
print(type(single))
#      (remember: a trailing comma is required!)
# YOUR CODE HERE


# Q42. Loop through  colors  and print each color on a new line.
# YOUR CODE HERE
for color in colors:
    print(color)


print("--- Section 4: Tuples done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Sets
# ──────────────────────────────────────────────────────────

# Q43. Create a set  team_a = {"Alice", "Bob", "Charlie", "Diana"}
# YOUR CODE HERE
team_a= {"Alice", "Bob", "Charlie", "Diana"}

# Q44. Print the length of  team_a.
# YOUR CODE HERE
print(len(team_a))

# Q45. Add "Eve" to  team_a  using add().
# YOUR CODE HERE
team_a.add("Eve")
print(team_a)

# Q46. Try adding "Bob" again — print the set. What do you notice?
#      Write a comment explaining why duplicates don't appear in sets.
# YOUR CODE HERE
team_a.add("Bob")
print(team_a)
# Sets do not allow duplicate values, so adding Bob again keeps only one copy.

# Q47. Remove "Charlie" using remove() and print the set.
# YOUR CODE HERE
team_a.remove("Charlie")
print(team_a)



# Q48. Use discard() to try removing "Zara" (who is NOT in the set).
#      Print the set. (discard() won't crash unlike remove())
# YOUR CODE HERE
team_a.discard("Zara")
print(team_a)

# Q49. Create  team_b = {"Charlie", "Diana", "Frank", "Grace"}
# YOUR CODE HERE
team_b = {"Charlie", "Diana", "Frank", "Grace"}


# Q50. Print the UNION of team_a and team_b  (all members from both).
# YOUR CODE HERE
print(team_a.union(team_b))

# Q51. Print the INTERSECTION of team_a and team_b  (members in BOTH teams).
# YOUR CODE HERE
print(team_a.intersection(team_b))

# Q52. Print the DIFFERENCE  team_a - team_b  (in a but not in b).
# YOUR CODE HERE
print(team_a.difference(team_b))

# Q53. Print the SYMMETRIC DIFFERENCE  (members in either team, but NOT both).
# YOUR CODE HERE
print(team_a.symmetric_difference(team_b))

# Q54. Check if  {"Diana"}  is a SUBSET of  team_a.  Print True or False.
# YOUR CODE HERE
print({"Diana"}.issubset(team_a))

# Q55. Convert the list  [1, 2, 2, 3, 3, 3, 4]  to a set to remove duplicates.
#      Print the result.
# YOUR CODE HERE
print(set([1, 2, 2, 3, 3, 3, 4]))



print("--- Section 5: Sets done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Dictionaries
# ──────────────────────────────────────────────────────────

# Q56. Create a dictionary  student  with these keys:
#        name, age, city, course, is_intern
#      Fill in your own values.
# YOUR CODE HERE
student={
    "name":"zeeshan",
    "age":20,
    "city":"Lahore",
    "course":"python",
    "is_intern":"yes"
}

# Q57. Print the value of the  "name"  key.
# YOUR CODE HERE
print(student["name"])

# Q58. Print the value of  "city"  using the  .get()  method.
# YOUR CODE HERE
print(student.get("city"))

# Q59. Add a new key  "score"  with value  88  to  student.
# YOUR CODE HERE
student["score"] = 88

# Q60. Update the  "city"  value to  "Lahore".
# YOUR CODE HERE
student["city"] = "Lahore"

# Q61. Delete the  "score"  key using  del.
# YOUR CODE HERE
del student["score"]

# Q62. Print ALL keys of  student  using  .keys()
# YOUR CODE HERE
print(student.keys())

# Q63. Print ALL values of  student  using  .values()
# YOUR CODE HERE
print(student.values())

# Q64. Print ALL key-value pairs using  .items()
# YOUR CODE HERE
print(student.items())

# Q65. Check if  "age"  exists as a key in  student.  Print True or False.
# YOUR CODE HERE
print("age" in student)

# Q66. Check if  "grade"  exists as a key in  student.  Print True or False.
# YOUR CODE HERE
print("grade" in student)

# Q67. Print the number of keys in  student  using  len().
# YOUR CODE HERE
print(len(student))


# Q68. Loop through  student  and print each key and its value like:
#      name  :  Bilal
#      age   :  22
#      ...
# YOUR CODE HERE
for key, value in student.items():
    print(f"{key} : {value}")


# Q69. Use  pop("is_intern")  to remove that key and print what was returned.
# YOUR CODE HERE
print(student.pop("is_intern"))


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
company = {
    "name": "PITB",
    "location": "Lahore",
    "department": {
        "name": "Data Center",
        "employees": 10
    }
}
print(company["name"])
print(company["department"]["name"])
print(company["department"]["employees"])


# Q71. Copy  student  into  student_backup  using  .copy()
#      Change "age" in  student  to 99.
#      Print age from BOTH dictionaries to show the copy is independent.
# YOUR CODE HERE
student_backup = student.copy()
student["age"] = 99
print(student["age"])
print(student_backup["age"])


# Q72. Use  .update()  to merge this data into  student:
#      {"grade": "A", "graduation_year": 2026}
#      Print the updated student dictionary.
# YOUR CODE HERE
student.update({"grade": "A", "graduation_year": 2026})
print(student)

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
report = {
    "name": "Bilal",
    "subjects": ["Math", "Science", "English"],
    "marks": (80, 45, 72),
    "passed": set()
}

report["passed"] = {subject for subject, mark in zip(report["subjects"], report["marks"]) if mark >= 50}
average = sum(report["marks"]) / len(report["marks"])

print("================================")
print(" Student Report")
print("================================")
print(f" Name    : {report['name']}")
print(f" Subjects: {', '.join(report['subjects'])}")
print(f" Marks   : {', '.join(map(str, report['marks']))}")
print(f" Passed  : {report['passed']}")
print(f" Average : {average:.2f}")
print("================================")


print("=== All done! Great work! ===")
