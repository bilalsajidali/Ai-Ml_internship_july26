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

print("Hello, I am learning Python")

# Q2. Python uses indentation to define blocks.
#     The code below has an indentation error. Fix it.
# if True:
# YOUR CODE HERE

if True:
    print("no indentation error")

# Q3. Print three different things on THREE separate lines:
#     your name, your city, and the number 2026
# YOUR CODE HERE

print("Name: Zarmeen \nCity: Lahore \nNumber: 2026")

# Q4. Print two words on the SAME line using end="":
#     Output should be:  PythonRocks
# YOUR CODE HERE

print("Python", end="")
print("Rocks")

# Q5. Use print() with sep argument to produce:  one | two | three
print("one", "two", "three", sep=" | ")   # <-- replace ??? with correct separator

print("\n--- Section 1: Syntax & Output done ---\n")

# ──────────────────────────────────────────────────────────
# SECTION 2 — Comments
# ──────────────────────────────────────────────────────────

# Q6. Write a single-line comment that says: This is my practice file
# YOUR CODE HERE (the comment itself is the answer)

#This is my practice file

# Q7. Write a multi-line comment (triple quotes) explaining what Python is used for.
# YOUR CODE HERE

"""  Python is a high level programming language used for Artificial Intelligence, 
Machine Learning and Data Science.  """

# Q8. The line below has a bug. Comment it out, then write the correct version.
# prnt("This line is broken")
# YOUR CODE HERE (correct version below)

print("This line is correct")

print("--- Section 2: Comments done ---\n")

# ──────────────────────────────────────────────────────────
# SECTION 3 — Variables
# ──────────────────────────────────────────────────────────

# Q9. Create variable  name  with your first name as a string.
# YOUR CODE HERE

name = "zarmeen"

# Q10. Create variable  age  with your age as a number.
# YOUR CODE HERE

age = 21

# Q11. Create variable  is_intern  and set it to True.
# YOUR CODE HERE

is_intern = True

# Q12. Print all three variables on separate lines.
# YOUR CODE HERE

print(name, age, is_intern)

# Q13. Assign THREE variables in ONE line:  x = 10, y = 20, z = 30
# YOUR CODE HERE

x,y,z = 10,20,30

# Q14. Assign the SAME value 0 to three variables a, b, c in one line.
# YOUR CODE HERE

a = b = c = 0

# Q15. Create  color = "red"  and  Color = "blue" , print both.
#      (shows that Python variable names are case-sensitive)
# YOUR CODE HERE

color = "red"
Color = "blue"
print(color, Color)

# Q16. Without running it, what error would this cause?  print(city)
#      Write the error name as a comment.
# YOUR CODE HERE  (example format:  # NameError)

# error: 'city' is not defined

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

name = "zarmeen"
age = 21
cgpa = 3.66
is_intern = True
subject = ["oop","dsa","os"]
number = (1,2,3)
letter = {
    "L1" : "a",
    "L2" : "b"
}
cr = {2,3,4,2,6,8,4}

print(name, type(name))
print(age, type(age))
print(cgpa, type(cgpa))
print(is_intern, type(is_intern))
print(subject, type(subject))
print(number, type(number))
print(letter, type(letter))
print(cr, type(cr))

# Q19. Print the type of  3.14
# YOUR CODE HERE

num = 3.14
print(type(num))

# Q20. Create  fruits = ["apple", "banana", "mango"]  and print its type.
# YOUR CODE HERE

fruits = ["apple", "banana", "mango"] 
print(type(fruits))

# Q21. Store  None  in a variable and print its type.
# YOUR CODE HERE

number = None
print(type(number))

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
 
print("sum = ", p+q)
print("diff = ", p-q)
print("product = ", p*q)
print("div = ", p/q)
print("fl div = ", p//q)
print("mod = ", p%q)
print("exp = ", p**q)

# Q24. Print the type of  100
# YOUR CODE HERE
print(type(100))

# Q25. Print the type of  100.0
# YOUR CODE HERE
print(type(100.0))

# Q26. Create complex number  c = 3 + 5j  and print it with its type.
# YOUR CODE HERE

c = 3+5j
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
print(math.sqrt(144))
print(round(math.pi, 4))

print("--- Section 5: Numbers done ---\n")

# ──────────────────────────────────────────────────────────
# SECTION 6 — Casting
# ──────────────────────────────────────────────────────────

# Q30. Cast the string "42" to an integer. Print result + its type.
# YOUR CODE HERE

num1 = int("42")
print(num1, type(num1))

# Q31. Cast the integer 7 to a float. Print result + its type.
# YOUR CODE HERE

num2 = float(7)
print(num2, type(num2))

# Q32. Cast the float 9.99 to an integer. What value do you get? Print it.
# YOUR CODE HERE

num3 = int(9.99)
print(num3)

# Q33. Cast integer 1 to bool and print it.  Then cast 0 to bool and print it.
# YOUR CODE HERE

num4 = bool(1)
print(num4)
num4 = bool(0)
print(num4)

# Q34. Fix this line so it prints:  You are 22 years old
#user_age = 22
# print("You are " + user_age + " years old")  <-- broken, fix using str() casting
# YOUR CODE HERE (fixed version)
user_age = str(22)
print("You are " + user_age + " years old")


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
print(sentence[10:21])

# Q41. Print sentence REVERSED using slicing  [::-1]
# YOUR CODE HERE
print(sentence[::-1])

# Q42. Replace "Amazing" with "Awesome" and print the result.
# YOUR CODE HERE

print(sentence.replace("Amazing","Awesome"))

# Q43. Check if "Python" is IN sentence. Print True or False.
# YOUR CODE HERE

print("Python" in sentence)

# Q44. Check if "Java" is NOT in sentence. Print True or False.
# YOUR CODE HERE

print("Java" not in sentence)

# Q45. Split sentence into a list of words and print the list.
# YOUR CODE HERE

words = sentence.split()
print(words)

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

print(f"My name is {name} and I am {age} years old.")

# Q51. Use .format() to print the same sentence as Q50.
# YOUR CODE HERE

print("My name is {} and I am {} years old.".format(name,age))

# Q52. Concatenate first + second and print result:
first = "Hello"
second = "World"
# YOUR CODE HERE  → expected output: HelloWorld

print(first+second)

# Q53. Print first and second with a space between using concatenation.
# YOUR CODE HERE  → expected output: Hello World

print(first+ " "+ second)

# Q54. Repeat "Ha" five times using the * operator.
# YOUR CODE HERE  → expected output: HaHaHaHaHa

print("ha"*5)

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
string1 = "hELLO wORLD"
print(string1.swapcase())

# Q59. Use center(60, "-") to center the text "PASS" in a 60-character line.
# YOUR CODE HERE
string = "pass"
print(string.center(60,"-"))

# Q60. Write a MULTILINE string (triple quotes) with 3 lines of text and print it.
# YOUR CODE HERE

mul_string = """ this is line1.
this line2. 
this is line3 """

print(mul_string)

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
name = input("Enter Name:")
age = 2026 - int(input("Enter birth year:"))
fav_num = float(input("Enter favourite number:"))

print("-"*40)
print("Name:  ", name, "\nAge in 2026: ", age, "\nFavourite number: ", fav_num)
#print("Age in 2026:", age)
print("Types:  ", type(name), type(age), type(fav_num))
print("-"*40)




print("=== All done! Great work! ===")

