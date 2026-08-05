# Python Practice Test 3 — Student Evaluations

**Test:** `test3.py` — If...Else · Match · While Loops · For Loops + Bonus mini-project
**Total:** 25 questions + 1 bonus (FizzBuzz + Exam Stats)
**Evaluated:** 2026-08-05
**Method:** Static review of every answer plus running each file end-to-end (Python 3.14.4) and checking the printed output against each question's requirement.

**Marking rule used here:** a question scores if the *printed output* satisfies what was asked. Spelling mistakes in your own labels (`"Final sum:"`, `"Average Score:"`) are free. Spelling mistakes inside a string the question specified exactly (`"Negative"`, `"Fever detected!"`) are flagged this time but will cost a mark from Test 4 onward.

## Summary

| Student  | File                | Score        | Grade | Runs cleanly | Notes |
|----------|---------------------|--------------|-------|--------------|-------|
| Abdullah | `test3-abdullah.py` | 25/25 + Bonus | A+ | ✅ | All correct; question comments deleted again (2nd time) |
| Zeeshan  | `test3-zeeshan.py`  | 25/25 + Bonus | A+ | ✅ | All correct; several required strings misspelled |
| Mahad    | `test3-mahad.py`    | 24/25 + Bonus | A  | ✅ | Q22 pattern collapsed onto one line |
| Zarmeen  | `test3-zarmeen.py`  | 23/25 + Bonus | B+ | ✅ | Q20 prints "rabbit"; Q25 didn't use comprehensions |

**All four files run to completion with no errors, and all four bonus sections produce the correct statistics** (Average `69.6`, Highest `95`, Lowest `45`, Passed `8`, Failed `2`). This is the strongest round so far — the whole group is now finishing the paper.

---

## Abdullah — 25/25 + Bonus ✅ (Grade: A+)

**Every answer correct.** Clean, consistent, easy to mark. FizzBuzz and Exam Stats both exactly to spec.

**Strengths**
- Section 1 and 2 flawless — the grade ladder, the three-way sign check, the nested `logged_in`/`is_admin`, and both `match` statements including `|` alternation.
- Q11 and Q19 both increment *before* the `continue` test, so neither loop can hang. This is the trap in `continue` + `while` and you avoided it cleanly.
- **Q22 is the only fully correct pattern in the group** — the inner loop uses `end=" "` and the bare `print()` sits at the *outer* level, which is exactly what produces the staircase.
- Q25 both comprehensions correct.
- Part B builds `highest`/`lowest` by seeding from `scores[0]` — the right way (see Zarmeen's note for why the alternative is fragile).

**Instruction not followed (flagged again, not deducted)**
- The header said **"Do NOT delete any existing code"**, but every question comment was stripped out — even the `Topics covered` header block. **This is the same note you got on Test 2.** Your answers are perfect, so no marks are lost, but I can't check your file against the question text without opening the original side by side. Fill in *under* each `# YOUR CODE HERE` and leave everything else alone.

**Minor notes**
- **Q4:** `if age >= 18 and has_id == True:` — `has_id` is already a boolean, so `and has_id` is enough. Comparing a bool to `True` is redundant.
- **Q18:** you print numbers 1–14 and then `"Found it! Stopping."`, so 15 itself never appears. The wording ("print each number before breaking") allows this reading and the other three printed 15 — both were accepted.

**Verdict:** Technically perfect for the second test running. Keep the scaffolding intact and this is unimprovable.

---

## Zeeshan — 25/25 + Bonus ✅ (Grade: A+)

**Every question logically correct**, question comments preserved, file runs clean. Strongest structural work in the group alongside Abdullah.

**Spelling — free this time, marks next time**
- **Q1:** variable is `temprature`, and the output is `"Fever detected"` / `"Temprature is normal"`. The question specified `"Fever detected!"` (with `!`) and *temperature*.
- **Q3:** prints `"Negitive"` — the question said `"Negative"`. Also `"positive"` lowercase where the question wrote `"Positive"`.
- **Q4:** the `else` branch prints just `"denied"`, not `"Entry denied"`. It never runs with `age = 20`, so nothing shows — but if the inputs changed, the output would be wrong.

None of these cost a mark, because the logic is right in every case. But an automated marker (or a real API contract) compares strings exactly, so build the habit now: **copy the required text out of the question rather than retyping it.**

**Strengths**
- Q11 handles the classic `continue` hazard by incrementing inside the skip branch *before* `continue` — a different fix from Abdullah's and equally valid.
- Q18 prints 15 *then* the message — the most literal reading of the question.
- Q22 pattern correct. Q21 `for...else` correct. Q20 `pass` correct with an accurate comment.
- Both Q25 comprehensions correct and idiomatic.
- Part B seeds `highest`/`lowest` from `scores[0]` and counts with a proper `if/else` pair.

**Minor notes**
- **Q2:** inconsistent indentation — the `if` body is indented 1 space, every `elif` body 3. Python accepts it because each block is internally consistent, but pick 4 spaces and stay there.
- Spacing like `temprature >37` and `score>=80` is legal but hard to read; put one space either side of every operator.

**Verdict:** Full marks and the cleanest loop reasoning in the group. Fix the typing accuracy and you're at Abdullah's level.

---

## Mahad — 24/25 + Bonus ✅ (Grade: A)

**Best-presented submission** — every answer is labelled `Q1`, `Q2`, … and separated by blank lines, so the terminal output reads like a marked paper. One real bug.

**Issue**

- **Q22 — the pattern prints on a single line.** *(–1)*
  ```python
  for i in range(1, 6):
      for j in range(1, i + 1):
          print(j, end=" ")
  print("\n")          # ← outside BOTH loops
  ```
  Output:
  ```
  1 1 2 1 2 3 1 2 3 4 1 2 3 4 5
  ```
  Expected:
  ```
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5
  ```
  `end=" "` suppresses the newline on every `print`, so *something* has to put it back at the end of each row. That something is a bare `print()` indented to the **outer** loop — it runs once per row:
  ```python
  for i in range(1, 6):
      for j in range(1, i + 1):
          print(j, end=" ")
      print()          # ← one level in: fires after each row
  ```
  This is the single most important thing on this paper, because it's the whole point of nested loops: **the inner loop builds a row, the outer loop ends it.**

**Minor notes (no deduction)**

- **Q21 — backslash typo.** `print(f"Odd found: {num}/n")` prints `Odd found: 17/n`. You wanted `\n` (backslash), not `/n` (forward slash). Since a `print()` already ends with a newline, just drop it: `print(f"Odd found: {num}")`.
- **Bonus Part A — extra formatting.** You print `Index 1 -> 1`, `Index 3 -> Fizz`, … The question asked for just `Fizz` / `Buzz` / `FizzBuzz` / the number. The classification logic is 100% correct, so no deduction — but FizzBuzz is an interview staple and it is always asked for in its bare form.
- **Q23** prints all nine grid numbers on one line. "Print every number" doesn't forbid that, so it's accepted — but the same `print()` fix from Q22 would give you a 3×3 layout that actually looks like a grid.
- **`\n` inside every message.** `print("Fever detected!\n")` works, but the newline is presentation, not part of the message. `print("Fever detected!")` followed by `print()` separates the two ideas.

**Strengths**
- The `print("Q1")` … `print("Q25")` labelling is genuinely good practice — keep it.
- Q12's `while True` / `break` is exactly right, including printing `"Attempt N: wrong"` only on the non-breaking path.
- Q16 labels the three `range()` outputs `a)`, `b)`, `c)` — nice touch when one question has three parts.
- Q20's `pass` comment is the clearest of the four: it explains that an empty block is a `SyntaxError` and `pass` is the filler.
- Part B is the most complete: you even count the elements manually (`score_count += 1`) instead of using `len()`, which is more in the spirit of "no built-ins".

**Verdict:** One indentation level away from full marks. Fix Q22 and re-run it.

---

## Zarmeen — 23/25 + Bonus ⚠️ (Grade: B+)

**Continued improvement — Test 1 blank, Test 2 66/72, now 23/25 with a fully working bonus.** Sections 1, 2 and 3 are essentially perfect. Both lost marks are in Section 4 and both come from the same habit: *the code produces roughly the right thing, so it doesn't get checked against the exact requirement.*

**Problems**

- **Q20 — `pass` doesn't skip anything.** *(–1)*
  ```python
  for a in animals:
      if a == "rabbit":
          pass
      print(a)          # ← runs for EVERY animal, rabbit included
  ```
  Your output prints `rabbit`, which is exactly what the question asked you to suppress. `pass` means **"do nothing"** — it is not `continue` and it is not `skip`. Once the `if` body finishes (by doing nothing), execution falls straight through to `print(a)` because that line is at the *loop* level, not inside an `else`. The question wanted:
  ```python
  for a in animals:
      if a == "rabbit":
          pass          # placeholder — do nothing for this item
      else:
          print(a)      # ← indented under else, so rabbit never reaches it
  ```
  Also move your explanation comment next to the `pass` itself, not after the loop.

- **Q25 — neither part used a list comprehension.** *(–1)* The question's title is *"List comprehension — two tasks"*; that's the skill being tested.

  a) You used an accumulator loop:
  ```python
  numbers = []
  for x in range(1,11):
      sq = x**2
      numbers.append(sq)
  ```
  Correct output, but the comprehension is the one line it compresses to: `squares = [x**2 for x in range(1, 11)]`

  b) This one is more serious:
  ```python
  for n in source:
      if n%2 != 0:
          source.remove(n)     # mutating the list you're looping over
  ```
  **It printed `[6, 12, 18, 24]` — the right answer — by luck.** Removing items from a list while iterating it shifts every later element down one index while the loop's internal counter keeps moving up, so items get skipped. It happened to work because the odd numbers in `source` alternate. Change `source` to `[3, 5, 6, 12]` and it breaks. Never mutate a list you are iterating. Build a new one instead:
  ```python
  evens = [n for n in source if n % 2 == 0]
  ```
  Also: `numbers = []` here overwrites the `numbers = [4, 8, 12, 17, 20]` from Q21. Harmless in a linear script, but pick distinct names.

**Minor notes (no deduction)**

- **Q2 — spelling.** `"Garde B"`, `"Garde C"`, `"Garde D"`, `"Garde F"` — *Grade*, and only the first one is spelled right. The question asked for just `"C"`; adding a label is fine, but check what you print.
- **Q2 — redundant conditions.** `elif score >= 80 and score <= 89:` — by the time an `elif` is reached, every condition above it was already `False`, so `score >= 90` is known false and `score <= 89` is guaranteed. `elif score >= 80:` is enough. This is the whole reason `elif` exists.
- **Q3:** prints `"negative"` / `"zero"` lowercase where the question capitalised them.
- **Q4:** `if (age >= 18 and has_id == True):` — the parentheses aren't needed, and `has_id` is already a boolean. `if age >= 18 and has_id:`
- **Q18:** prints `"Found it! Stopping"` — missing the full stop.
- **Bonus Part B — fragile seed values.**
  ```python
  Lowest_score = 100
  Highest_score = 0
  ```
  These only work because you know the scores sit between 0 and 100. Feed it `[120, 130]` and `Highest_score` is right but a list of all-negative numbers would report `0` as the highest. Seed from real data: `highest = scores[0]` and `lowest = scores[0]` — the other three all did this.
  Variable names should also be lowercase: `lowest_score`, not `Lowest_score` (capitalised names are conventionally reserved for classes).
- **Q17:** the leftover `#multiple = 7` comment can go.

**Strengths**
- **Sections 1–3 are fully correct**, including both `match` statements, `while...else`, `while True` + `break`, and the `continue` skip in Q11 (with the increment placed before `continue`, so no infinite loop).
- Q22's nested pattern is **correct** — you put `print("")` at the outer-loop level, which is exactly the thing Mahad missed.
- Q21 `for...else` correct.
- Bonus Part A FizzBuzz correct, with the `and` case tested first — the ordering that trips most people up.
- Bonus Part B numbers all correct, and the `print("="*10, ...)` section headers make the output readable.

**Verdict:** Your control flow is solid now — the loops and conditionals are no longer the problem. What's left is precision: **read the question's title as part of the requirement** (Q25 said "list comprehension"), and **trace what your code prints for every input, not just the given one** (Q20, Q25b). Those two habits are the gap between B+ and A.

---

## Overall Observations

- **Everyone finished, everyone's file runs, and all four bonuses are numerically correct.** Test 1 → Test 2 → Test 3 is a clear upward line for the whole group.
- **Sections 1–3 were near-perfect across all four papers.** `if/elif/else`, `match` with `|`, `while True` + `break`, and `while...else` are now solid group-wide. Notably, **all four** avoided the infinite-loop trap in Q11 (`continue` before the increment) — that's the single most common beginner bug with `while` loops and nobody hit it.
- **The one real dividing line was Q22 (nested loops).** The rule to memorise: with `print(x, end=" ")`, the **inner** loop prints a row and a bare `print()` at the **outer** level ends it. Get the indentation of that `print()` wrong and you get one long line (Mahad) instead of a staircase. Abdullah, Zeeshan and Zarmeen all had it right.
- **`pass` is not `continue`.** `pass` is a do-nothing placeholder that keeps a block syntactically legal; execution continues to the next line as normal. To actually skip work, put the work in an `else` (or use `continue`). Zarmeen's Q20 is the worked example.
- **Never mutate a list while looping over it** (Zarmeen Q25b). It silently skips elements. Build a new list with a comprehension.
- **Match the exact strings a question gives you.** `"Negitive"`, `"Garde C"`, `"Fever detected"` without the `!` — three of the four papers retyped a specified string and got it wrong. Copy-paste from the question.
- **`if flag == True:` → `if flag:`.** Three of you wrote the long form. A boolean is already the condition.
- **Keep the provided file intact** (Abdullah, second reminder). Fill in under `# YOUR CODE HERE`; don't delete the question text.
- **Seed min/max from the data, not from guessed bounds** — `highest = scores[0]`, not `highest = 0`.
