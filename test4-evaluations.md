# Python Practice Test 4 — Student Evaluations

**Test:** `test4.py` — Functions · Range · Arrays · Iterators · Modules · Dates · Math · JSON · RegEx · PIP · Try...Except · String Formatting · None · User Input · Virtual Environment + Bonus (`safe_divide`)
**Total:** 39 questions + 1 bonus (Q40)
**Evaluated:** 2026-10-08
**Method:** Static review of every answer, plus running each file end-to-end (Python 3.14, with `Sam` / `6` piped to the two `input()` questions) and checking the printed output against each question's requirement.

**Marking rule used here:** as announced in Test 3, **a string the question gives you exactly must now be printed exactly.** That means the same words, spelling, capitalisation, and spacing (`"Cannot divide by zero!"`, `"Price: 50 dollars"`, `"Hello, <name>!"`). A trailing full stop added to a required sentence is flagged but not deducted. Commands written as comments (pip, venv) must be ones that would actually work if typed.

## Summary

| Student  | File                | Score         | Grade | Runs cleanly | Notes |
|----------|---------------------|---------------|-------|--------------|-------|
| Shajee   | `test4-shajee.py`   | 37/39 + Bonus | A-    | ✅ | Q8 stops at 2; Q30 missing `finally` |
| Tabraiz  | `test4-tabraiz.py`  | 32/39 + Bonus | C+    | ✅ | Three required strings mistyped; Q19 wrong date format; Q27/Q37 commands wouldn't run |

**Both files run to completion with no errors, and both bonuses are correct** (`5.0` and `None`).

> The other four Test 4 submissions (Abdullah, Mahad, Zarmeen, Zeeshan — submitted 2026-08-10) have not been evaluated yet. This file only covers the two late submissions.

---

## Shajee — 37/39 + Bonus ✅ (Grade: A-)

*Evaluated 2026-10-08 (late submission).*

**Your best paper so far.** It runs clean and every required string is exact. Functions, modules, JSON, RegEx, and try/except are all correct. Two lost marks.

**Problems**
- **Q8 — countdown stops at 2.** `range(10, 1, -1)` excludes the stop value, so `1` never prints. Use `range(10, 0, -1)`. *(–1)*
- **Q30 — no `finally` block.** The `ValueError` is caught, but the question also asked for `finally: print("Done")`, and it's missing. *(–1)*

**Minor notes (no deduction)**
- **Q7 / Q8 share one line.** Both loops use `end=" "` with no closing `print()`, so the output reads `2 4 6 8 10 10 9 8 7 6 5 4 3 2 3`. The last `3` is Q9's `len(fruits)`. Add a bare `print()` after each loop.
- **Trailing full stops** were added to required strings in Q30 (`"Not a number."`), Q31 (`"... years old."`), and Q34 (`"No value yet."`). They're not deducted this time, but match the question exactly.
- **Q38:** `venv/scripts/activate` works in PowerShell. In `cmd` it needs backslashes: `venv\Scripts\activate`.

**Strengths**
- **Q35 calls your own `greet()` from Q1** to greet the user. Reusing a function you already wrote is exactly the point of functions.
- Q2/Q3 `return` values instead of printing inside the function, so the caller decides what to do with the result.
- Q4 uses `sum(numbers)` on `*args`, and Q5 loops over `info.items()` from `**kwargs`. Both are clean.
- Q16 `from math import sqrt` is correct, and Q19 `strftime("%d/%m/%Y")` gives the exact format.
- Q26 uses a raw-string regex `r'\d'`, which is the right habit for regex patterns.
- Q34 uses `is None` rather than `== None`, which is the correct comparison.
- Bonus `safe_divide` catches the *specific* `ZeroDivisionError` instead of a bare `except`.

**Fixes needed**
```python
# Q8
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Q30
try:
    int("hello")
except ValueError:
    print("Not a number")
finally:
    print("Done")
```

**Verdict:** Your best result so far, and the file ran cleanly this time. Keep running the file before you submit; that's what made the difference.

---

## Tabraiz — 32/39 + Bonus ✅ (Grade: C+)

*Evaluated 2026-10-08 (late submission).*

**Runs clean, and the logic is right almost everywhere.** Functions, iterators, JSON, RegEx, and try/except/finally all work. But under this test's exact-string rule, three answers lose a mark for mistyped text, and two of the comment answers wouldn't work if typed.

**Problems**
- **Q1 — string not exact.** Prints `Hello,Bilal`. Required: `Hello, Bilal!` (space after the comma, and `!`). *(–1)*
- **Q19 — wrong date format.** `strftime("%x")` gives the locale default, here `10/08/26` (MM/DD/YY). Required: DD/MM/YYYY → `strftime("%d/%m/%Y")`. *(–1)*
- **Q27 — wrong package.** `pip install request` installs a *different* package. The one asked for is `requests` (with an **s**). *(–1)*
- **Q29 — string not exact.** `"Cannot divided by zero"`. Required: `"Cannot divide by zero!"`. *(–1)*
- **Q32 — string not exact.** `"price : 50 dollars"`. Required: `"Price: 50 dollars"`. *(–1)*
- **Q35 — doesn't greet.** `print(name)` just echoes the input. "Greet them" means something like `print(f"Hello, {name}!")`, or call your `greet(name)` from Q1. *(–1)*
- **Q37 — typo in the command.** `pyhton -m venv venv` won't run. It should be `python -m venv venv`. *(–1)*

**Minor notes (no deduction)**
- **Q3 — `print` inside the function instead of `return`.** `power(5)` prints `25`, so the output is fine. But `print(power(5))`, which is what the question literally says, would print `25` and then `None`. Functions should `return` their result and let the caller print it, as you did correctly in Q2.
- **Q34:** `if result == None:` works, but `is None` is the correct way to compare with `None`.
- **Q38:** `< virtual environment name> /scripts/activate` is a template, not a command. Q37 named the environment `venv`, so `venv\Scripts\activate`.

**Strengths**
- Q4 adds up `*args` with a manual loop, so you clearly understand what `*numbers` actually is.
- Q30 is complete with `try` / `except ValueError` / `finally`, and the output is exactly `Not a number` / `Done`.
- Q31 and Q34 strings are exact.
- Q8 `range(10, 0, -1)` reaches `1` correctly.
- Q13 builds the iterator and uses `next()` correctly. Q26 `[0-9]` with `findall` is correct.
- The bonus `safe_divide` is correct and catches the specific `ZeroDivisionError`.

**Fixes needed**
```python
# Q1
print(f"Hello, {name}!")

# Q19
print(date.strftime("%d/%m/%Y"))

# Q27
# pip install requests

# Q29
print("Cannot divide by zero!")

# Q32
print("Price: {} dollars".format(price))

# Q35
name = input("Enter your name: ")
greet(name)

# Q37
# python -m venv venv
```

**Verdict:** The logic is a B+ paper. The typing turns it into a C+. You were warned about this in Test 3, and it cost five marks here: three required strings and two commands. **Copy-paste the required text from the question** instead of retyping it.

---

## Overall Observations (late submissions)

- **Both papers run cleanly.** For Shajee, that's the first time in four tests, and it's the main reason for the A-.
- **The exact-string rule mattered.** Shajee lost nothing to it. Tabraiz lost three marks to retyped strings (`Hello,Bilal`, `Cannot divided`, `price :`) and two more to mistyped commands (`request`, `pyhton`). Copy the required text from the question.
- **`range()` excludes its stop value.** `range(10, 1, -1)` ends at 2, so to count down to 1 the stop must be 0.
- **`return`, don't `print`, inside functions** (Tabraiz Q3). A function that prints can't pass its result on to anything else.
- **Comments that are commands must be runnable.** `pip install request` and `pyhton -m venv` would both fail or do the wrong thing in a real terminal.
