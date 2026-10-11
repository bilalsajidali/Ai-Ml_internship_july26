# Python Practice Test 1 — Student Evaluations

**Test:** `test1.py` — Python fundamentals (Syntax · Output · Comments · Variables · Data Types · Numbers · Casting · Strings + Bonus mini-project)
**Total:** 60 questions + 1 bonus
**Evaluated:** 2026-07-22
**Method:** Static review of every answer plus running each file end-to-end (bonus inputs piped).

## Summary

| Student  | File                 | Score      | Grade | Runs cleanly | Notes |
|----------|----------------------|------------|-------|--------------|-------|
| Abdullah | `test1-abdullah.py`  | 60/60 + Bonus | A+ | ✅ | Complete and correct throughout |
| Mahad    | `test1-mahad.py`     | 59/60 + Bonus | A  | ✅ | Only deviation: used `f_name` instead of `name` (Q9) |
| Areesha  | `test1-areesha.py`   | 59/60, Bonus incomplete | A- | ✅ | Q16 didn't name the error; bonus stops after the inputs |
| Zeeshan  | `test1-zeeshan.py`   | ~55/60, Bonus incomplete | C+ | ⚠️ | Q34 wrong output, Q51 missing, Q60 not printed, bonus unfinished |
| Zarmeen  | `test1-zarmeen.py`   | 0/60 | — | ❌ | File is empty — nothing submitted |
| Shajee   | `test1-shajee.py`    | 53/60 + Bonus | C+ | ❌ | Crashes at Q29 (`math.pi(4)`); Q55 typo would crash next; 5 more answers wrong or not printed |
| Tabraiz  | `test1-tabraiz.py`   | 52/60, Bonus incomplete | C | ✅ | Case/spelling slips (Q42, Q49), `f_name`, Q16 not named; bonus prints birth year as age |

---

## Abdullah — 60/60 + Bonus ✅ (Grade: A+)

**Excellent.** Every question answered correctly and the file runs with no errors.

**Strengths**
- All 8 data types created and printed correctly (Q18).
- Correct arithmetic, complex numbers, `math` usage (Q22–Q29).
- All string operations correct, including slicing, `replace`, `count`, `find`, f-string and `.format()`.
- Bonus mini-project complete: takes input, computes age, prints the formatted summary with types.

**Minor notes**
- Q40 used `sentence[10:21]` (indices 10–20 inclusive) — a valid reading of "index 10 to 20".

**Verdict:** Model submission. No corrections needed.

---

## Mahad — 59/60 + Bonus ✅ (Grade: A)

**Very strong.** Runs cleanly and the bonus is complete and correct.

**Issue**
- **Q9:** The question asked to create a variable named `name`. Mahad used `f_name = "Mahad"` instead. It works (he consistently uses `f_name` later), but it deviates from the instruction to name the variable `name`. *(–1)*

**Strengths**
- All data types, numbers, casting, and string operations correct.
- Q49 used `.index("Programming")` — valid alternative to `.find()`.
- Bonus mini-project fully implemented with f-strings and types.

**Verdict:** Essentially perfect; just match the exact variable name the question asks for.

---

## Areesha — 59/60, Bonus incomplete ✅ (Grade: A-)

*Evaluated 2026-10-05 (late submission).*

**Strong submission.** The file runs end-to-end with no errors, and every one of Q1–Q60 except Q16 produces the required output.

**Issues**
- **Q16 — error name not given.** The answer was `# name of city is not declared`. That explains the cause correctly, but the question asked for the error's name in the format `# NameError`. *(–1)*
- **Bonus — incomplete.** Only the three `input()` lines are written: name, birth year cast to `int`, and favourite number cast to `float`. There's no age calculation and no summary block, so after the prompts the program prints only the closing line. *(Bonus not awarded)*

**Minor notes (no deduction)**
- **Q3** printed four things (name, age, city, 2026) when it asked for three. It also creates `city = "Lahore"` at the top, so in *this* file `print(city)` (Q16) wouldn't actually raise an error.
- **Q17** re-assigns `x, y, z = 10, 20, 30` before `del y`. That's harmless but not needed, since `y` already exists from Q13. Q46 and Q53 likewise re-declare variables the template already defines.
- **Q18** reuses `a` for the set, which overwrites `a = 0` from Q14. Use a distinct name, e.g. `my_set`, to avoid clobbering earlier variables.
- **Q40** used `sentence[10:20]`, which is accepted (see note below).
- The bonus prompt `"Enter your name ; "` has a semicolon typo. It should be `:`.

**Strengths**
- All 8 data types in Q18 created and printed correctly, plus `NoneType` in Q21.
- Numbers section fully correct: all 7 operators, complex numbers, `abs`, `pow`, `math.sqrt`, and `round(math.pi, 4)`.
- Casting correct, including Q34 with proper spacing: `You are 22 years old`.
- Every string method in Q35–Q60 is correct, including `.format()`, `center()`, `swapcase()`, and a printed multiline string.

**Fix needed**
```python
# Q16
# NameError

# Bonus — finish it
age_in_2026 = 2026 - birth_year
print("-----------------------------------------------")
print("Name             :", name)
print("Age in 2026      :", age_in_2026)
print("Favourite number :", favourite_number)
print("Types            :", type(name), type(age_in_2026), type(favourite_number))
print("-----------------------------------------------")
```

**Verdict:** Fundamentals are strong. Answer in exactly the format each question asks for, and finish the bonus. With the summary block added, this would be an A.

---

## Zeeshan — ~55/60, Bonus incomplete ⚠️ (Grade: C+)

Runs without crashing, but several answers are wrong, missing, or don't produce the required output.

**Problems**
- **Q34 — wrong output.** `print("you are" + str(user_age) + "years old")` prints `you are22years old`. Required: `You are 22 years old` (missing spaces around the number, and lowercase "you"). *(–1)*
- **Q51 — missing.** The `.format()` answer was left blank; nothing printed. *(–1)*
- **Q60 — not printed.** A triple-quoted multiline string is written but never passed to `print()`, so nothing appears. Question said "and print it." *(–1)*
- **Bonus — incomplete.** Only the three `input()` lines are present. No age calculation and no summary block, so the program ends silently after the prompts. *(Bonus not awarded)*

**Correct work**
- Sections 1–5 solid: syntax, output, comments, variables, data types, and numbers all correct.
- Good string handling (Q35–Q50): upper/lower, length, indexing, slicing, replace, membership, split, strip, count, `find`, f-string.
- Q18 covered all 8 types with inline comments.

**Fixes needed**
```python
# Q34
print("You are " + str(user_age) + " years old")

# Q51
print("My name is {} and I am {} years old.".format(name, age))

# Q60 — assign then print
lines = """i am learning python
it is a very popular programming language
it will help me a lot in my career"""
print(lines)

# Bonus — finish it
age_in_2026 = 2026 - birth_year
print("-----------------------------------------------")
print("Name             :", name)
print("Age in 2026      :", age_in_2026)
print("Favourite number :", favourite_number)
print("Types            :", type(name), type(age_in_2026), type(favourite_number))
print("-----------------------------------------------")
```

**Verdict:** Good grasp of the fundamentals, but finish every question and always verify the printed output matches the spec.

---

## Zarmeen — 0/60 ❌ (No submission)

**`test1-zarmeen.py` is completely empty** — no code was written. Nothing to evaluate.

**Action:** Please submit your attempt. Start from a copy of `test1.py` and fill in each `# YOUR CODE HERE` line.

---

## Shajee — 53/60 + Bonus ❌ crashes (Grade: C+)

*Evaluated 2026-10-08 (late submission).*

**The file crashes at Q29 with a `TypeError`**, so nothing from Q29b to the end, bonus included, actually runs. I fixed the two crashing lines in a scratch copy to mark the rest. The bonus turned out to be complete and correct.

**Problems**
- **Q4 — `end` used the wrong way.** `print("Python", end="Rocks")` does print `PythonRocks`, but it leaves no newline behind, so Q5's output gets glued on: `PythonRocksone | two | three`. `end=""` is meant for joining two separate prints: `print("Python", end="")` then `print("Rocks")`. *(–1)*
- **Q14 — wrong variable names.** You wrote `x = y = z = 0` instead of `a = b = c = 0`. That also overwrites Q13's `x, y, z`, so Q17's `del y` deletes a `0` instead of the `20` from Q13. *(–1)*
- **Q15 — not printed.** `color` and `Color` are created but never printed. *(–1)*
- **Q18 — incomplete.** Only 7 of the 8 types are created (no `set`), and none of them is printed with `type()`. *(–1)*
- **Q26 — value not printed, wrong name.** The question asked for `c = 3 + 5j` printed together with its type. You named it `t` and printed only `type(t)`. *(–1)*
- **Q29b — crash.** `math.pi(4)` → `TypeError: 'float' object is not callable`. `math.pi` is a number, not a function: `round(math.pi, 4)`. *(–1)*
- **Q55 — would crash too.** `sentence.startwith(...)` → `AttributeError`. The method is `startswith`. Q29 crashes first so this line never runs, but it is the next crash waiting. *(–1)*

**Minor notes (no deduction)**
- **Q3 / Q12:** `print(name, "\n", age, "\n", is_intern)` puts a separator space after each newline, so lines come out as `" 20"`, `" True"`. Use one `print()` per line or `sep="\n"`.
- **Q13:** `x = 10; y = 20; z = 30` is three statements squeezed onto one line. Q13 is about multiple assignment: `x, y, z = 10, 20, 30`.
- **Q11 / Q18:** `bool(True)`, `int(9)`, and `str("hello")` wrap a literal in its own type, which does nothing.
- **Q43 / Q44 / Q55 / Q56:** `if ...: print(True) else: print(False)` can just be `print("Python" in sentence)`. The expression is already a boolean.

**Strengths**
- The strings section is otherwise fully correct, including `.format()`, `center()`, `swapcase()`, `index()`, and a printed multiline string.
- Casting (Q30–Q34) is correct, and Q34 has the exact spacing: `You are 22 years old`.
- All 7 arithmetic operators are printed.
- The bonus is complete. It computes the age (22 for 2004) and prints all three types.

**Fixes needed**
```python
# Q4
print("Python", end="")
print("Rocks")

# Q14
a = b = c = 0

# Q15
print(color, Color)

# Q18 — add the set and print every type
h = {1, 2, 3}
print(type(a), type(b), type(c), type(d), type(e), type(f), type(g), type(h))

# Q26
c = 3 + 5j
print(c, type(c))

# Q29b
print(round(math.pi, 4))

# Q55
print(sentence.startswith("Python"))
```

**Verdict:** You know most of this material. The marks were lost because the file was never run before submitting; the Q29 crash shows up the first time you do. Run the file and read every line of output against the question.

---

## Tabraiz — 52/60, Bonus incomplete ✅ (Grade: C)

*Evaluated 2026-10-08 (late submission).*

**Runs end to end with no errors**, but eight answers print the wrong thing or nothing. The bonus prints the birth year where the age should be.

**Problems**
- **Q5 — separator missing spaces.** `sep="|"` prints `one|two|three`. Required: `one | two | three` → `sep=" | "`. *(–1)*
- **Q9 — wrong variable name.** `f_name` instead of `name`. Mahad lost the same mark. *(–1)*
- **Q12 — not on separate lines.** `print(f_name, age, is_intern)` prints all three on one line. *(–1)*
- **Q16 — error not named.** `# error:"city"is not defined` gives the message, but the question asked for the error's name: `# NameError`. Areesha lost the same mark. *(–1)*
- **Q35 / Q36 — lowercase missing.** Q35 is left blank, and the answer under Q36 prints `.upper()`, so the lowercase version is never printed. *(–1)*
- **Q42 — nothing replaced.** `replace("amaizing", "awesm")` searches for "amaizing", which isn't in the sentence (it says "Amazing": capital A, different spelling). Nothing matches, so the original sentence prints unchanged. *(–1)*
- **Q49 — wrong case.** `find("programming")` returns `-1` because the sentence contains "Programming" with a capital P. *(–1)*
- **Q59 — wrong fill character.** `center(60, " ")` uses a space, but the question specified `"-"`. *(–1)*
- **Bonus — age not calculated.** The birth year is stored in `age` and printed as-is: `Age in 2026: 2004`. It needs `2026 - birth_year`. *(Bonus not awarded)*

**Instruction not followed (flagged, not deducted)**
- The header says **"Do NOT delete any existing code"**, but several template lines were commented out or moved: `user_age = 22` (Q34), the `sentence = ...` line (moved under Q36), the Q5 template line, and `print("--- Section 7: Strings done ---\n")`.
- Q3 and Q4 are indented inside Q2's `if True:` block. They only run because that condition happens to be `True`. Bring them back to the left margin.

**Minor notes**
- **Q1** prints a leading space: `" Hello, I am learning Python!"`.
- **Q6** comment typo: "practics".

**Strengths**
- **Q18 is complete:** all 8 types created and printed with `type()`. Two other students missed parts of this one.
- The numbers section is fully correct, including `round(math.pi, 4)`.
- Q43, Q44, Q55, and Q56 print the boolean expression directly, which is cleaner than an `if/else`.
- Casting (Q30–Q33) is correct.

**Fixes needed**
```python
# Q5
print("one", "two", "three", sep=" | ")

# Q9 / Q12
name = "Tabraiz"
print(name)
print(age)
print(is_intern)

# Q16
# NameError

# Q35 / Q36
print(sentence.upper())
print(sentence.lower())

# Q42
print(sentence.replace("Amazing", "Awesome"))

# Q49
print(sentence.find("Programming"))

# Q59
print("PASS".center(60, "-"))

# Bonus
birth_year = int(input("Enter your birth year: "))
age_in_2026 = 2026 - birth_year
```

**Verdict:** The concepts are right. Almost every lost mark is a case or typing slip (`amaizing`, `programming`, `"|"`, `" "`). Python compares text exactly, so copy strings straight from the question.

---

## Overall Observations

- **Common strength:** Sections 1–5 (syntax, output, comments, variables, data types, numbers) were handled well by everyone who submitted.
- **Common weak spot to watch:** casting into string concatenation (Q34) — remember spaces inside the quoted text and wrap numbers in `str()`.
- **Unfinished bonus is recurring:** Zeeshan and Areesha both stopped after the `input()` calls. The summary block is what ties the exercise together.
- **Reminder for all:** an answer only counts if it *prints* the required output. Writing a string/expression without `print()` (e.g., Zeeshan's Q60) produces nothing.
- **Q40 note:** "index 10 to 20" is ambiguous; both `[10:20]` and `[10:21]` were accepted.
- **Late submissions (2026-10-08) — Shajee and Tabraiz.** Neither ran their file closely enough before submitting. Shajee's crashes at Q29, and Tabraiz's runs but prints the wrong value in several places. The fix is the same for both: run the file and check each printed line against its question.
