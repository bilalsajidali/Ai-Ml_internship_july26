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

## Overall Observations

- **Common strength:** Sections 1–5 (syntax, output, comments, variables, data types, numbers) were handled well by everyone who submitted.
- **Common weak spot to watch:** casting into string concatenation (Q34) — remember spaces inside the quoted text and wrap numbers in `str()`.
- **Unfinished bonus is recurring:** Zeeshan and Areesha both stopped after the `input()` calls. The summary block is what ties the exercise together.
- **Reminder for all:** an answer only counts if it *prints* the required output. Writing a string/expression without `print()` (e.g., Zeeshan's Q60) produces nothing.
- **Q40 note:** "index 10 to 20" is ambiguous; both `[10:20]` and `[10:21]` were accepted.
