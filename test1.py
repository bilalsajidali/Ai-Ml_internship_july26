## DONT USE INTERNET UNTIL YOU FINISH THE TEST! ##

# ============================================================
#  Python Practice Test — Muhammad Bilal Sajid
#  Topics covered (W3Schools order):
#    Syntax · Output · Comments · Variables · Data Types ·
#    Numbers · Casting · Strings
#
#  Instructions:
#    - Fill in every line marked with:  # YOUR CODE HERE
#    - Do NOT delete any existing code
#    - Run the file when done: python test.py
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — Syntax & Output
# ──────────────────────────────────────────────────────────

# Q1. Print the message:  Hello, I am learning Python!
# YOUR CODE HERE


# Q2. Python uses indentation to define blocks.
#     The code below has an indentation error. Fix it.
# if True:
# YOUR CODE HERE


# Q3. Print three different things on THREE separate lines:
#     your name, your city, and the number 2026
# YOUR CODE HERE


# Q4. Print two words on the SAME line using end="":
#     Output should be:  PythonRocks
# YOUR CODE HERE


# Q5. Use print() with sep argument to produce:  one | two | three
print("one", "two", "three", sep=???)   # <-- replace ??? with correct separator


print("\n--- Section 1: Syntax & Output done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Comments
# ──────────────────────────────────────────────────────────

# Q6. Write a single-line comment that says: This is my practice file
# YOUR CODE HERE (the comment itself is the answer)


# Q7. Write a multi-line comment (triple quotes) explaining what Python is used for.
# YOUR CODE HERE


# Q8. The line below has a bug. Comment it out, then write the correct version.
# prnt("This line is broken")
# YOUR CODE HERE (correct version below)


print("--- Section 2: Comments done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — Variables
# ──────────────────────────────────────────────────────────

# Q9. Create variable  name  with your first name as a string.
# YOUR CODE HERE


# Q10. Create variable  age  with your age as a number.
# YOUR CODE HERE


# Q11. Create variable  is_intern  and set it to True.
# YOUR CODE HERE


# Q12. Print all three variables on separate lines.
# YOUR CODE HERE


# Q13. Assign THREE variables in ONE line:  x = 10, y = 20, z = 30
# YOUR CODE HERE


# Q14. Assign the SAME value 0 to three variables a, b, c in one line.
# YOUR CODE HERE


# Q15. Create  color = "red"  and  Color = "blue" , print both.
#      (shows that Python variable names are case-sensitive)
# YOUR CODE HERE


# Q16. Without running it, what error would this cause?  print(city)
#      Write the error name as a comment.
# YOUR CODE HERE  (example format:  # NameError)


# Q17. Use  del  to delete variable  y  from Q13, then print "y deleted".
# YOUR CODE HERE


print("--- Section 3: Variables done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Data Types
# ──────────────────────────────────────────────────────────

# Q18. Create one variable of each type and print each with type():
#      str, int, float, bool, list, tuple, dict, set
# YOUR CODE HERE


# Q19. Print the type of  3.14
# YOUR CODE HERE


# Q20. Create  fruits = ["apple", "banana", "mango"]  and print its type.
# YOUR CODE HERE


# Q21. Store  None  in a variable and print its type.
# YOUR CODE HERE


print("--- Section 4: Data Types done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Numbers
# ──────────────────────────────────────────────────────────

# Q22. Create:  p = 20   q = 6
# YOUR CODE HERE


# Q23. Print results of all 7 arithmetic operations:  + - * / // % **
# YOUR CODE HERE


# Q24. Print the type of  100
# YOUR CODE HERE


# Q25. Print the type of  100.0
# YOUR CODE HERE


# Q26. Create complex number  c = 3 + 5j  and print it with its type.
# YOUR CODE HERE


# Q27. Print the absolute value of  -456  using abs()
# YOUR CODE HERE


# Q28. Use  pow(2, 8)  and print the result.
# YOUR CODE HERE


# Q29. Import math and:
#      a) Print square root of 144
#      b) Print math.pi rounded to 4 decimal places
# YOUR CODE HERE


print("--- Section 5: Numbers done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Casting
# ──────────────────────────────────────────────────────────

# Q30. Cast the string "42" to an integer. Print result + its type.
# YOUR CODE HERE


# Q31. Cast the integer 7 to a float. Print result + its type.
# YOUR CODE HERE


# Q32. Cast the float 9.99 to an integer. What value do you get? Print it.
# YOUR CODE HERE


# Q33. Cast integer 1 to bool and print it.  Then cast 0 to bool and print it.
# YOUR CODE HERE


# Q34. Fix this line so it prints:  You are 22 years old
user_age = 22
# print("You are " + user_age + " years old")  <-- broken, fix using str() casting
# YOUR CODE HERE (fixed version)


print("--- Section 6: Casting done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 7 — Strings
# ──────────────────────────────────────────────────────────

sentence = "Python is an Amazing Programming Language"

# Q35. Print sentence in ALL UPPERCASE.
# YOUR CODE HERE


# Q36. Print sentence in all lowercase.
# YOUR CODE HERE


# Q37. Print the total length (number of characters) of sentence.
# YOUR CODE HERE


# Q38. Print only the FIRST character using indexing.
# YOUR CODE HERE


# Q39. Print only the LAST character using NEGATIVE indexing.
# YOUR CODE HERE


# Q40. Print characters from index 10 to 20 (slicing).
# YOUR CODE HERE


# Q41. Print sentence REVERSED using slicing  [::-1]
# YOUR CODE HERE


# Q42. Replace "Amazing" with "Awesome" and print the result.
# YOUR CODE HERE


# Q43. Check if "Python" is IN sentence. Print True or False.
# YOUR CODE HERE


# Q44. Check if "Java" is NOT in sentence. Print True or False.
# YOUR CODE HERE


# Q45. Split sentence into a list of words and print the list.
# YOUR CODE HERE


# Q46. Strip whitespace from this string and print clean version:
padded = "     Hello Bilal!     "
# YOUR CODE HERE


# Q47. Use lstrip() to remove only LEFT whitespace from padded.
# YOUR CODE HERE


# Q48. Count how many times the letter "a" appears in sentence (case-sensitive).
# YOUR CODE HERE


# Q49. Find the INDEX of first occurrence of "Programming" in sentence.
# YOUR CODE HERE


# Q50. Use an f-string to print:
#      "My name is <name> and I am <age> years old."
#      (use name and age variables from Section 3)
# YOUR CODE HERE


# Q51. Use .format() to print the same sentence as Q50.
# YOUR CODE HERE


# Q52. Concatenate first + second and print result:
first = "Hello"
second = "World"
# YOUR CODE HERE  → expected output: HelloWorld


# Q53. Print first and second with a space between using concatenation.
# YOUR CODE HERE  → expected output: Hello World


# Q54. Repeat "Ha" five times using the * operator.
# YOUR CODE HERE  → expected output: HaHaHaHaHa


# Q55. Check if sentence STARTS WITH "Python". Print True or False.
# YOUR CODE HERE


# Q56. Check if sentence ENDS WITH "Language". Print True or False.
# YOUR CODE HERE


# Q57. Print sentence in Title Case using title().
# YOUR CODE HERE


# Q58. Use swapcase() on "hELLO wORLD" and print the result.
# YOUR CODE HERE


# Q59. Use center(60, "-") to center the text "PASS" in a 60-character line.
# YOUR CODE HERE


# Q60. Write a MULTILINE string (triple quotes) with 3 lines of text and print it.
# YOUR CODE HERE


print("--- Section 7: Strings done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS — Mini Project (combines everything)
# ──────────────────────────────────────────────────────────

# Ask the user for:
#   - Their name        (string)
#   - Their birth year  (cast to integer)
#   - Their favourite number (cast to float)
#
# Then print a summary like:
# -----------------------------------------------
#  Name             : Bilal
#  Age in 2026      : 22
#  Favourite number : 7.0
#  Types            : <class 'str'>  <class 'int'>  <class 'float'>
# -----------------------------------------------

# YOUR CODE HERE


print("=== All done! Great work! ===")
