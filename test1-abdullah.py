# ============================================================
#  Python Practice Test — Muhammad Bilal Sajid
#  Topics covered (W3Schools order):
# ============================================================


# ──────────────────────────────────────────────────────────
# SECTION 1 — Syntax & Output
# ──────────────────────────────────────────────────────────

# Q1
print("Hello, I am learning Python!")

# Q2
if True:
    print("Indentation fixed")

# Q3
print("Abdullah")
print("Lahore")
print(2026)

# Q4
print("Python", end="")
print("Rocks")

# Q5
print("one", "two", "three", sep=" | ")

print("\n--- Section 1: Syntax & Output done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Comments
# ──────────────────────────────────────────────────────────

# Q6
# This is my practice file

# Q7
"""
Python is used for web development,
automation, data science,
and software development.
"""

# Q8
# prnt("This line is broken")
print("This line is broken")

print("--- Section 2: Comments done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 3 — Variables
# ──────────────────────────────────────────────────────────

# Q9
name = "Abdullah"

# Q10
age = 22

# Q11
is_intern = True

# Q12
print(name)
print(age)
print(is_intern)

# Q13
x, y, z = 10, 20, 30

# Q14
a = b = c = 0

# Q15
color = "red"
Color = "blue"

print(color)
print(Color)

# Q16
# NameError

# Q17
del y
print("y deleted")

print("--- Section 3: Variables done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Data Types
# ──────────────────────────────────────────────────────────

# Q18
text = "Python"
number = 10
decimal = 3.14
flag = True
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"name": "Abdullah"}
my_set = {1, 2, 3}

print(type(text))
print(type(number))
print(type(decimal))
print(type(flag))
print(type(my_list))
print(type(my_tuple))
print(type(my_dict))
print(type(my_set))

# Q19
print(type(3.14))

# Q20
fruits = ["apple", "banana", "mango"]
print(type(fruits))

# Q21
nothing = None
print(type(nothing))

print("--- Section 4: Data Types done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Numbers
# ──────────────────────────────────────────────────────────

# Q22
p = 20
q = 6

# Q23
print(p + q)
print(p - q)
print(p * q)
print(p / q)
print(p // q)
print(p % q)
print(p ** q)

# Q24
print(type(100))

# Q25
print(type(100.0))

# Q26
c = 3 + 5j
print(c)
print(type(c))

# Q27
print(abs(-456))

# Q28
print(pow(2, 8))

# Q29
import math

print(math.sqrt(144))
print(round(math.pi, 4))

print("--- Section 5: Numbers done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Casting
# ──────────────────────────────────────────────────────────

# Q30
num = int("42")
print(num)
print(type(num))

# Q31
num2 = float(7)
print(num2)
print(type(num2))

# Q32
num3 = int(9.99)
print(num3)

# Q33
print(bool(1))
print(bool(0))

# Q34
user_age = 22
print("You are " + str(user_age) + " years old")

print("--- Section 6: Casting done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 7 — Strings
# ──────────────────────────────────────────────────────────

sentence = "Python is an Amazing Programming Language"

# Q35
print(sentence.upper())

# Q36
print(sentence.lower())

# Q37
print(len(sentence))

# Q38
print(sentence[0])

# Q39
print(sentence[-1])

# Q40
print(sentence[10:21])

# Q41
print(sentence[::-1])

# Q42
print(sentence.replace("Amazing", "Awesome"))

# Q43
print("Python" in sentence)

# Q44
print("Java" not in sentence)

# Q45
print(sentence.split())

# Q46
padded = "     Hello Bilal!     "
print(padded.strip())

# Q47
print(padded.lstrip())

# Q48
print(sentence.count("a"))

# Q49
print(sentence.find("Programming"))

# Q50
print(f"My name is {name} and I am {age} years old.")

# Q51
print("My name is {} and I am {} years old.".format(name, age))

# Q52
first = "Hello"
second = "World"

print(first + second)

# Q53
print(first + " " + second)

# Q54
print("Ha" * 5)

# Q55
print(sentence.startswith("Python"))

# Q56
print(sentence.endswith("Language"))

# Q57
print(sentence.title())

# Q58
print("hELLO wORLD".swapcase())

# Q59
print("PASS".center(60, "-"))

# Q60
text = """This is line 1.
This is line 2.
This is line 3."""

print(text)

print("--- Section 7: Strings done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS — Mini Project
# ──────────────────────────────────────────────────────────

user_name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
fav_number = float(input("Enter your favourite number: "))

user_age = 2026 - birth_year

print("-----------------------------------------------")
print("Name             :", user_name)
print("Age in 2026      :", user_age)
print("Favourite number :", fav_number)
print("Types            :", type(user_name), type(user_age), type(fav_number))
print("-----------------------------------------------")

print("=== All done! Great work! ===")