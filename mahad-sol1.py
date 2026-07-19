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


print("Hello, I am learning Python!")  


# Q2. Python uses indentation to define blocks.
#     The code below has an indentation error. Fix it.
if True:
    print("Fixed Indentation Error!")  

# Q3. Print three different things on THREE separate lines:
#     your name, your city, and the number 2026
# YOUR CODE HERE
print("Mahad Bin Atif")
print("Lahore")
print(2026)

# Q4. Print two words on the SAME line using end="":
#     Output should be:  PythonRocks
# YOUR CODE HERE
print("Python",end="")
print("Rocks")


# Q5. Use print() with sep argument to produce:  one | two | three
# YOUR CODE HERE
print("one", "two", "three", sep=" | ")   # <-- replace ??? with correct separator


print("\n--- Section 1: Syntax & Output done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Comments
# ──────────────────────────────────────────────────────────

# Q6. Write a single-line comment that says: This is my practice file
# YOUR CODE HERE
# This is my practice file


# Q7. Write a multi-line comment (triple quotes) explaining what Python is used for.
# YOUR CODE HERE
"""
Python is a programming language used in various workflows such as web development, data analysis, artificial intelligence, automations etc
"""


# Q8. The line below has a bug. Comment it out, then write the correct version.
# prnt("This line is broken")
# YOUR CODE HERE
print("This line is broken")



print("--- Section 2: Comments done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — Variables
# ──────────────────────────────────────────────────────────

# Q9. Create variable  name  with your first name as a string.
# YOUR CODE HERE
f_name="Mahad"


# Q10. Create variable  age  with your age as a number.
# YOUR CODE HERE
age=22


# Q11. Create variable  is_intern  and set it to True.
# YOUR CODE HERE
is_intern=True


# Q12. Print all three variables on separate lines.
# YOUR CODE HERE
print(f_name)
print(age)
print(is_intern)


# Q13. Assign THREE variables in ONE line:  x = 10, y = 20, z = 30
# YOUR CODE HERE
x,y,z=10,20,30

# Q14. Assign the SAME value 0 to three variables a, b, c in one line.
# YOUR CODE HERE
a,b,c=0,0,0

# Q15. Create  color = "red"  and  Color = "blue" , print both.
#      (shows that Python variable names are case-sensitive)
# YOUR CODE HERE
color="Red"
Color="Blue"
print(color)
print(Color)

# Q16. Without running it, what error would this cause?  print(city)
#      Write the error name as a comment.
# YOUR CODE HERE  (example format:  # NameError)
# NameError


# Q17. Use  del  to delete variable  y  from Q13, then print "y deleted".
# YOUR CODE HERE
del y
print("y deleted")

print("--- Section 3: Variables done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Data Types
# ──────────────────────────────────────────────────────────

# Q18. Create one variable of each type and print each with type():
#      str, int, float, bool, list, tuple, dict, set
# YOUR CODE HERE
v_str="Hello"
v_int=10
v_float=3.14
v_bool=True
v_list=[1,2,3]
v_tuple=(1,2,3)
v_dict={"name":"Mahad","age":22}
v_set={1,2,3}
print(type(v_str))
print(type(v_int))
print(type(v_float))
print(type(v_bool))
print(type(v_list))
print(type(v_tuple))
print(type(v_dict))
print(type(v_set))

# Q19. Print the type of  3.14
# YOUR CODE HERE
print(type(3.14))

# Q20. Create  fruits = ["apple", "banana", "mango"]  and print its type.
# YOUR CODE HERE
fruits = ["apple", "banana", "mango"]
print(type(fruits))

# Q21. Store  None  in a variable and print its type.
# YOUR CODE HERE
v_none = None
print(type(v_none))

print("--- Section 4: Data Types done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Numbers
# ──────────────────────────────────────────────────────────

# Q22. Create:  p = 20   q = 6
# YOUR CODE HERE
p = 20
q = 6

# Q23. Print results of all 7 arithmetic operations:  + - * / // % **
# YOUR CODE HERE
print(p+q)
print(p-q)
print(p*q)
print(p/q)
print(p//q)
print(p%q)
print(p**q)

# Q24. Print the type of  100
# YOUR CODE HERE
print(type(100))

# Q25. Print the type of  100.0
# YOUR CODE HERE
print(type(100.0))

# Q26. Create complex number  c = 3 + 5j  and print it with its type.
# YOUR CODE HERE
c=3+5j
print(c)
print(type(c))

# Q27. Print the absolute value of  -456  using abs()
# YOUR CODE HERE
print(abs(-456))

# Q28. Use  pow(2, 8)  and print the result.
# YOUR CODE HERE
print(pow(2, 8))

# Q29. Import math and:
#      a) Print square root of 144
#      b) Print math.pi rounded to 4 decimal places
# YOUR CODE HERE
import math
#a
print(math.sqrt(144))
#b
print(round(math.pi, 4))

print("--- Section 5: Numbers done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Casting
# ──────────────────────────────────────────────────────────

# Q30. Cast the string "42" to an integer. Print result + its type.
# YOUR CODE HERE
v_str="42"
var_int=int(v_str)
print(var_int)
print(type(var_int))

# Q31. Cast the integer 7 to a float. Print result + its type.
# YOUR CODE HERE
v_int=7
v_float=float(v_int)
print(v_float)
print(type(v_float))

# Q32. Cast the float 9.99 to an integer. What value do you get? Print it.
# YOUR CODE HERE
v_float=9.99
v_int=int(v_float)
print(v_int)

# Q33. Cast integer 1 to bool and print it.  Then cast 0 to bool and print it.
# YOUR CODE HERE
v_int=1
v_bool=bool(v_int)
print(v_bool)

v_int=0
v_bool=bool(v_int)
print(v_bool)

# Q34. Fix this line so it prints:  You are 22 years old
user_age = 22
# print("You are " + user_age + " years old")  <-- broken, fix using str() casting
# YOUR CODE HERE (fixed version)
print("You are "+str(user_age)+" years old")


print("--- Section 6: Casting done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 7 — Strings
# ──────────────────────────────────────────────────────────

sentence = "Python is an Amazing Programming Language"

# Q35. Print sentence in ALL UPPERCASE.
# YOUR CODE HERE
print(sentence.upper())

# Q36. Print sentence in all lowercase.
# YOUR CODE HERE
print(sentence.lower())

# Q37. Print the total length (number of characters) of sentence.
# YOUR CODE HERE
print(len(sentence))

# Q38. Print only the FIRST character using indexing.
# YOUR CODE HERE
print(sentence[0])

# Q39. Print only the LAST character using NEGATIVE indexing.
# YOUR CODE HERE
print(sentence[-1])

# Q40. Print characters from index 10 to 20 (slicing).
# YOUR CODE HERE
print(sentence[10:20])

# Q41. Print sentence REVERSED using slicing  [::-1]
# YOUR CODE HERE
print(sentence[::-1])

# Q42. Replace "Amazing" with "Awesome" and print the result.
# YOUR CODE HERE
print(sentence.replace("Amazing", "Awesome"))

# Q43. Check if "Python" is IN sentence. Print True or False.
# YOUR CODE HERE
print("Python" in sentence)

# Q44. Check if "Java" is NOT in sentence. Print True or False.
# YOUR CODE HERE
print("Java" not in sentence)

# Q45. Split sentence into a list of words and print the list.
# YOUR CODE HERE
print(sentence.split())

# Q46. Strip whitespace from this string and print clean version:
padded = "     Hello Bilal!     "
# YOUR CODE HERE
print(padded.strip())

# Q47. Use lstrip() to remove only LEFT whitespace from padded.
# YOUR CODE HERE
print(padded.lstrip())

# Q48. Count how many times the letter "a" appears in sentence (case-sensitive).
# YOUR CODE HERE
print(sentence.count("a"))

# Q49. Find the INDEX of first occurrence of "Programming" in sentence.
# YOUR CODE HERE
print(sentence.index("Programming"))

# Q50. Use an f-string to print:
#      "My name is <name> and I am <age> years old."
#      (use name and age variables from Section 3)
# YOUR CODE HERE
print(f"My name is {f_name} and I am {age} years old.")

# Q51. Use .format() to print the same sentence as Q50.
# YOUR CODE HERE
print("My name is {} and I am {} years old.".format(f_name, age))

# Q52. Concatenate first + second and print result:
first = "Hello"
second = "World"
# YOUR CODE HERE  → expected output: HelloWorld
print(first+second)

# Q53. Print first and second with a space between using concatenation.
# YOUR CODE HERE  → expected output: Hello World
print(first+" "+second)


# Q54. Repeat "Ha" five times using the * operator.
# YOUR CODE HERE  → expected output: HaHaHaHaHa
print("Ha"*5)

# Q55. Check if sentence STARTS WITH "Python". Print True or False.
# YOUR CODE HERE
print(sentence.startswith("Python"))

# Q56. Check if sentence ENDS WITH "Language". Print True or False.
# YOUR CODE HERE
print(sentence.endswith("Language"))

# Q57. Print sentence in Title Case using title().
# YOUR CODE HERE
print(sentence.title())

# Q58. Use swapcase() on "hELLO wORLD" and print the result.
# YOUR CODE HERE
print("hELLO wORLD".swapcase())

# Q59. Use center(60, "-") to center the text "PASS" in a 60-character line.
# YOUR CODE HERE
print("PASS".center(60, "-"))

# Q60. Write a MULTILINE string (triple quotes) with 3 lines of text and print it.
# YOUR CODE HERE
multi_line = """This is line one.
This is line two.
This is line three."""
print(multi_line)

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
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
favourite_number = float(input("Enter your favourite number: "))

age_in_2026 = 2026 - birth_year

print("-" * 10)
print(f" Name: {name}")
print(f" Age in 2026: {age_in_2026}")
print(f" Favourite number: {favourite_number}")
print(f" Types: {type(name)}  {type(birth_year)}  {type(favourite_number)}")
print("-" * 10)

print("=== All done! Great work! ===")