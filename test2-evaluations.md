# Python Practice Test 2 — Student Evaluations

**Test:** `test2.py` — Booleans · Operators · Lists · Tuples · Sets · Dictionaries + Bonus mini-project
**Total:** 72 questions + 1 bonus
**Evaluated:** 2026-07-29
**Method:** Static review of every answer plus running each file end-to-end (Python 3.14.4) and checking the printed output against each question's requirement.

## Summary

| Student  | File                | Score       | Grade | Runs cleanly | Notes |
|----------|---------------------|-------------|-------|--------------|-------|
| Mahad    | `test2-mahad.py`    | 72/72 + Bonus | A+ | ✅ | Flawless; bonus matches the target format exactly |
| Abdullah | `test2_abdullah.py` | 72/72 + Bonus | A+ | ✅ | All answers correct, but the question comments were deleted |
| Zeeshan  | `test2-zeeshan.py`  | 71/72 + Bonus | A  | ✅ | Only Q34 used a string literal instead of comments |
| Zarmeen  | `test2-zarmeen.py`  | 66/72, Bonus partial | B- | ✅ | Big improvement over Test 1; 6 answers wrong or not printed |

**All four files run to completion with no errors.** Everyone submitted this time — a clear step up from Test 1.

---

## Mahad — 72/72 + Bonus ✅ (Grade: A+)

**Model submission.** Every question correct, all question text preserved, runs clean.

**Strengths**
- All six sections complete and correct — booleans, every operator family, list mutation sequence, tuples, set algebra, dictionaries.
- Q54 used `{"Diana"} <= team_a` — a valid alternative to `.issubset()`.
- Q68 used an f-string for the key/value loop.
- **Bonus is the best of the four:** builds `report` with the exact required keys, derives `passed` with `zip()` and a `>= 50` check, computes the average with `sum()/len()`, and prints with f-strings and `:.2f`. Output matches the requested layout line for line.

**Minor note (no deduction)**
- **Q40:** your `colors` tuple already contained `"purple"` at Q32, so appending `"purple"` produces it twice in the final tuple. The code is right; just pick 5 starting colors that don't include the one you're about to add.

**Verdict:** Nothing to fix. Excellent work.

---

## Abdullah — 72/72 + Bonus ✅ (Grade: A+)

**All 72 answers are correct** and the file runs with no errors.

**Strengths**
- Clean, consistently formatted, one `print()` per required output — easy to read and mark.
- Correct list-mutation chain through Q17–Q31 (append → insert → remove → pop → sort → reverse → extend → clear).
- Full set algebra correct, including `symmetric_difference()` and `issubset()`.
- Nested dictionary access (Q70) and independent `.copy()` demonstration (Q71) both correct.
- Bonus complete: `passed` built with `zip()`, average correct at `65.67`.

**Instruction not followed (flagged, not deducted)**
- The file header said **"Do NOT delete any existing code"**, but every question comment was removed — only `# Q1`, `# Q2`, … remain. The answers are all correct, so no marks were lost, but keep the question text next time: it makes the file self-checking, and it's how the other three submitted.

**Minor notes**
- **Q17:** your `cities` list already had `"Lahore"` at index 1, so the assignment was a no-op. Correct code, but start with a different city so the change is visible.
- **Bonus:** you used `print("Name :", ...)` and `round(average, 2)`. The output is right, but the hint asked for an f-string — `f"Name    : {report['name']}"` and `f"{average:.2f}"` give you the aligned layout for free.

**Verdict:** Technically perfect. Just keep the provided scaffolding intact.

---

## Zeeshan — 71/72 + Bonus ✅ (Grade: A)

**Strong, near-complete submission** and a big improvement over Test 1 — every section is finished and the bonus is fully implemented.

**Issue**
- **Q34 — used a string, not comments.** *(–1)*
  ```python
  """TypeError tuple does not support the item assignment
  tuples are immutable ..."""
  ```
  The question said **"comments only"**. A triple-quoted block sitting on its own is a *string expression*, not a comment — Python evaluates and discards it. Use `#`:
  ```python
  # TypeError: 'tuple' object does not support item assignment
  # Tuples are immutable — their items cannot be changed after creation.
  ```

**Minor notes (no deduction)**
- **Q3d:** you wrote `bool("python")`; the question said `bool("Python")`. Same result, but match the given value.
- **Q56:** `"is_intern": "yes"` is a *string*. On a test about booleans, prefer `True` — it's also what makes Q69's `pop()` return meaningful.
- **Q33:** `colors[4]` works, but `colors[-1]` is the idiom for "last item".
- **Q41:** your answer sits *above* the `# YOUR CODE HERE` marker. Cosmetic only.
- **Q16:** `cities[1:3]` prints indices 1–2. "Index 1 to 3" is ambiguous — both `[1:3]` and `[1:4]` were accepted.
- Extra `print(cities)` calls through the list section aren't required, but they show your working — keep doing that while learning.

**Strengths**
- All operator sections correct, including bitwise and identity.
- Set algebra fully correct, including `{"Diana"}.issubset(team_a)` in the right order.
- **Bonus is excellent** — you used a *set comprehension* with `zip()`:
  ```python
  report["passed"] = {subject for subject, mark in zip(report["subjects"], report["marks"]) if mark >= 50}
  ```
  That's more advanced than the hint asked for, and the output matches the target format exactly.

**Verdict:** Great turnaround from Test 1. One tiny fix and this is a perfect paper.

---

## Zarmeen — 66/72, Bonus partial ⚠️ (Grade: B-)

**Huge improvement — Test 1 was blank, this is a nearly complete submission** that runs without crashing. Most of the work is correct. The mistakes cluster around one habit: *computing a value but not printing it*, and *calling methods on the wrong object*.

**Problems**

- **Q22 — printed the wrong item.** *(–1)*
  ```python
  cities.pop()
  print(cities[-1])     # prints "rome" — the NEW last item
  ```
  `pop()` **returns** the item it removed. You threw that away and printed whatever ended up last instead. The removed item was `"Islamabad"`.
  ```python
  print(cities.pop())
  ```

- **Q37 — not printed.** *(–1)* `counts_tuple.count("blue")` computes `3`, but nothing is displayed. Wrap it: `print(counts_tuple.count("blue"))`

- **Q38 — not printed.** *(–1)* Same issue: `counts_tuple.index("green")` → `print(counts_tuple.index("green"))`

- **Q54 — subset check is backwards.** *(–1)*
  ```python
  print(team_a.issubset({"Diana"}))   # False — asks "is team_a inside {Diana}?"
  ```
  `A.issubset(B)` means "is **A** contained in **B**". The question asked whether `{"Diana"}` is a subset of `team_a`:
  ```python
  print({"Diana"}.issubset(team_a))   # True
  ```

- **Q56 — missing a required key.** *(–1)* The question listed five keys: `name, age, city, course, is_intern`. Your dictionary has four — **`course` is missing**. This is why Q67 printed `4` instead of `5`.

- **Q69 — printed the dictionary, not the return value.** *(–1)*
  ```python
  student.pop("is_intern")
  print(student)          # prints the whole dict
  ```
  The question said *"print what was returned"*:
  ```python
  print(student.pop("is_intern"))   # True
  ```

- **Q71 — changed the wrong dictionary.** *(–1, folded into the count above as the Q69/Q71 pair)*
  ```python
  student_backup = student.copy()
  student_backup.update({"age" : 99})   # you changed the BACKUP
  ```
  The question said change `"age"` in **`student`** to 99. Your output reads `student: 21 / backup: 99` — the reverse of what was asked. It still demonstrates independence, but follow the instruction as written:
  ```python
  student["age"] = 99
  ```

**Bonus — partially correct**

It runs and the numbers are right (average `68.33`), but three things miss the spec:
- The key is `"subject"`, not **`"subjects"`** as required.
- `passed` is **hardcoded** as `{"physics","maths"}`. The task and hint asked you to *derive* it with `zip()` and a `mark >= 50` test — that's the actual skill being tested.
- Subjects and marks print as a raw list/tuple (`['physics', 'chemistry', 'maths']`, `(72, 48, 85)`) instead of the comma-separated form in the sample output.

```python
report = {
    "name": "zarmeen",
    "subjects": ["physics", "chemistry", "maths"],
    "marks": (72, 48, 85),
    "passed": set()
}
for subject, mark in zip(report["subjects"], report["marks"]):
    if mark >= 50:
        report["passed"].add(subject)

print(f"Subjects  :   {', '.join(report['subjects'])}")
print(f"Marks     :   {', '.join(map(str, report['marks']))}")
```

**Two things to watch (no deduction)**

- **Q55 — don't shadow built-in names.**
  ```python
  list = [1, 2, 2, 3, 3, 3, 4]   # 'list' is now your list, not the built-in type
  ```
  This only avoided breaking because your last `list(...)` call was back at Q40. Use `nums` or `numbers_list` instead.

- **Nested quotes in f-strings.** You wrote `f"student dict age: {student["age"]}"`. This is legal only in **Python 3.12+** — on 3.11 or older it's a `SyntaxError`. It ran fine here (3.14.4), but for portability use the other quote style: `f"student dict age: {student['age']}"`

**Correct work**
- Sections 1 and 2 are **fully correct** — booleans, `bool()` truthiness, all arithmetic, comparison, logical, assignment, identity, membership and bitwise operators.
- `p, q = 6, 3` (Q12) is nice, idiomatic tuple unpacking.
- The whole list-mutation sequence Q17–Q31 is right apart from Q22.
- Set operations Q43–Q53 all correct; Q46 explanation is right.
- Nested dictionary access (Q70) correct.
- Labelled output like `print("number of keys: ", len(student))` is good practice.

**Verdict:** Genuinely strong recovery — the concepts are clearly there. Your single biggest habit to fix is: **if a question says "print", the answer must end up inside `print()`.** Three of your six lost marks were values you computed correctly but never displayed.

---

## Overall Observations

- **Everyone submitted, and everyone's file runs.** That's the biggest improvement over Test 1.
- **Common strength:** Sections 1 and 2 (booleans and operators) were near-perfect across all four papers. Set algebra was also handled well by everyone.
- **Recurring weak spot — `print()` the result.** Same lesson as Test 1: a computed value that is never printed scores nothing (Zarmeen Q37, Q38). Check your terminal output against the question, not just your code.
- **Recurring weak spot — methods that *return* vs. methods that *mutate*.** `pop()` returns the removed item; `sort()`, `reverse()`, `append()` and `clear()` change the list in place and return `None`. Q22 and Q69 both test exactly this.
- **Argument order matters:** `A.issubset(B)` asks "is A inside B" (Zarmeen Q54). When a method reads like a sentence, check which object is the subject.
- **Read the key list carefully** — Q56 named five keys; missing one silently changes the answers to Q62, Q63, Q64 and Q67.
- **Q16 note:** "index 1 to 3" is ambiguous; both `[1:3]` and `[1:4]` were accepted for everyone.
- **Keep the provided file intact.** Fill in under each `# YOUR CODE HERE` and leave the question comments in place (see Abdullah's note).
