# ============================================================
#  Python Practice Test 2 — Muhammad Bilal Sajid
# ============================================================

# ──────────────────────────────────────────────────────────
# SECTION 1 — Booleans
# ──────────────────────────────────────────────────────────

# Q1
is_raining = False
is_sunny = True

print(is_raining)
print(is_sunny)

# Q2
print(10 > 5)
print(10 == 5)
print(10 < 5)
print("hello" == "hello")
print("hello" == "Hello")

# Q3
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool([]))
print(bool([1, 2, 3]))
print(bool(None))

# Q4
score = 75
print(score >= 50)

# Q5
print(isinstance(3.14, float))
print(isinstance("hello", int))

print("--- Section 1: Booleans done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 2 — Operators
# ──────────────────────────────────────────────────────────

a = 15
b = 4

# Q6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Q7
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Q8
print(a > 10 and b > 2)
print(a > 10 and b > 10)
print(a > 10 or b > 10)
print(not (a > 10))

# Q9
n = 100

n += 20
print(n)

n -= 10
print(n)

n *= 2
print(n)

n //= 3
print(n)

n **= 2
print(n)

n %= 7
print(n)

# Q10
x = ["apple"]
y = ["apple"]
z = x

print(x is z)
print(x is y)
print(x is not y)

# Q11
fruits = ["mango", "banana", "apple"]

print("mango" in fruits)
print("grape" in fruits)
print("grape" not in fruits)

# Q12
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

# Q13
cities = ["Karachi", "Lahore", "Islamabad", "Multan", "Peshawar"]

# Q14
print(cities[0])

# Q15
print(cities[-1])

# Q16
print(cities[1:4])

# Q17
cities[1] = "Lahore"

# Q18
print(len(cities))

# Q19
cities.append("Islamabad")

# Q20
cities.insert(2, "Multan")

# Q21
cities.remove("Lahore")

# Q22
print(cities.pop())

# Q23
print(cities.pop(0))

# Q24
cities.sort()
print(cities)

# Q25
cities.reverse()
print(cities)

# Q26
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Q27
nums_copy = numbers.copy()
print(nums_copy)

# Q28
print(5 in numbers)

# Q29
print(numbers.count(1))

# Q30
cities.extend(numbers)
print(cities)

# Q31
cities.clear()
print(cities)

print("--- Section 3: Lists done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 4 — Tuples
# ──────────────────────────────────────────────────────────

# Q32
colors = ("red", "blue", "green", "yellow", "black")

# Q33
print(colors[0])
print(colors[-1])

# Q34

# colors[1] = "pink"
# TypeError
# Tuples cannot be changed because they are immutable.

# Q35
print(len(colors))

# Q36
print("red" in colors)

# Q37
counts_tuple = ("blue", "red", "blue", "green", "blue")
print(counts_tuple.count("blue"))

# Q38
print(counts_tuple.index("green"))

# Q39
point = (10, 20, 30)

x, y, z = point

print(x)
print(y)
print(z)

# Q40
color_list = list(colors)
color_list.append("purple")
colors = tuple(color_list)

print(colors)

# Q41
single = ("only",)

print(single)
print(type(single))

# Q42
for color in colors:
    print(color)

print("--- Section 4: Tuples done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 5 — Sets
# ──────────────────────────────────────────────────────────

# Q43
team_a = {"Alice", "Bob", "Charlie", "Diana"}

# Q44
print(len(team_a))

# Q45
team_a.add("Eve")

# Q46
team_a.add("Bob")
print(team_a)

# Sets only store unique values, so duplicate items are ignored.

# Q47
team_a.remove("Charlie")
print(team_a)

# Q48
team_a.discard("Zara")
print(team_a)

# Q49
team_b = {"Charlie", "Diana", "Frank", "Grace"}

# Q50
print(team_a.union(team_b))

# Q51
print(team_a.intersection(team_b))

# Q52
print(team_a.difference(team_b))

# Q53
print(team_a.symmetric_difference(team_b))

# Q54
print({"Diana"}.issubset(team_a))

# Q55
nums = [1, 2, 2, 3, 3, 3, 4]
print(set(nums))

print("--- Section 5: Sets done ---\n")


# ──────────────────────────────────────────────────────────
# SECTION 6 — Dictionaries
# ──────────────────────────────────────────────────────────

# Q56
student = {
    "name": "Ali",
    "age": 21,
    "city": "Faisalabad",
    "course": "BSCS",
    "is_intern": True
}

# Q57
print(student["name"])

# Q58
print(student.get("city"))

# Q59
student["score"] = 88

# Q60
student["city"] = "Lahore"

# Q61
del student["score"]

# Q62
print(student.keys())

# Q63
print(student.values())

# Q64
print(student.items())

# Q65
print("age" in student)

# Q66
print("grade" in student)

# Q67
print(len(student))

# Q68
for key, value in student.items():
    print(key, ":", value)

# Q69
print(student.pop("is_intern"))

# Q70
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

# Q71
student_backup = student.copy()

student["age"] = 99

print(student["age"])
print(student_backup["age"])

# Q72
student.update({
    "grade": "A",
    "graduation_year": 2026
})

print(student)

print("--- Section 6: Dictionaries done ---\n")


# ──────────────────────────────────────────────────────────
# BONUS — Mini Project
# ──────────────────────────────────────────────────────────

subjects = ["Math", "Science", "English"]
marks = (80, 45, 72)

passed = set()

for sub, mark in zip(subjects, marks):
    if mark >= 50:
        passed.add(sub)

report = {
    "name": "Bilal",
    "subjects": subjects,
    "marks": marks,
    "passed": passed
}

average = sum(marks) / len(marks)

print("==============================")
print("Student Report")
print("==============================")
print("Name :", report["name"])
print("Subjects :", ", ".join(report["subjects"]))
print("Marks :", ", ".join(map(str, report["marks"])))
print("Passed :", report["passed"])
print("Average :", round(average, 2))
print("==============================")

print("=== All done! Great work! ===")