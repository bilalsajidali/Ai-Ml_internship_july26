# Web Basics Practice Test 5 — Student Evaluations

**Test:** `test5.html` — HTML · CSS · JavaScript · Git & GitHub + Bonus (GitHub Pages)
**Total:** 49 questions + 1 bonus (Q50)
**Evaluated:** 2026-09-30
**Method:** I read every answer against the question text, traced the `<script>` block for runtime errors and console output, checked each CSS rule against the spec, and opened the bonus GitHub Pages URL.

**Marking rule used here:** a question scores **1** if the result in the browser (rendered page, console output or behaviour) does what the question asked. A question scores **½** when the technique is right but part of the spec is missing: a required property left out, the wrong input data, or a partial answer. A question scores **0** when it is broken, blank or doesn't run. Wrong *words* inside a string the question gave you exactly now cost marks (as warned in Test 3). Punctuation and capitalization slips are flagged only.

## Summary

| Student | File                | Score           | Grade | Runs cleanly | Notes |
|---------|---------------------|-----------------|-------|--------------|-------|
| Rabiya  | `test5 Rabiya.html` | 39.5/49 + Bonus | B     | ✅           | Strong DOM/events work; Q26–27 functions and Q21 media query broken |

**Section breakdown**

| Section         | Questions | Score   |
|-----------------|-----------|---------|
| 1 — HTML        | Q1–Q12    | 9/12    |
| 2 — CSS         | Q13–Q21   | 7/9     |
| 3 — JavaScript  | Q22–Q36   | 12/15   |
| 4 — Git & GitHub| Q37–Q49   | 11.5/13 |
| **Total**       |           | **39.5/49 (81%)** |
| Bonus — Q50     | GitHub Pages | ✅ Live |

---

## Rabiya — 39.5/49 + Bonus ✅ (Grade: B)

The script runs with no console errors. The interactive section (Q33–Q36) is the strongest part of the paper: the counter, the toggle and the form handler all work first time. Most lost marks come from **reading the question too quickly**: arrays that aren't `nums`, a missing `target`, a missing `border: none`, a paragraph string retyped wrong. The one conceptual gap is **functions** (Q26–Q27).

**Filename:** the instructions asked for `test5-<yourname>.html`. The file was saved as `test5 Rabiya.html`, with a space and no hyphen. Spaces in filenames cause trouble in the terminal and in URLs, so use `test5-rabiya.html` next time.

### Section 1 — HTML (9/12)

| Q | Mark | Comment |
|---|------|---------|
| 1 | 1 | `<title>My Test 5 Page</title>` ✓ |
| 2 | 1 | ✓ |
| 3 | ½ | Text is `This page test HTML,CSS and JavaScript`. The question says **tests**, with a space after the comma and a full stop. Copy the required text from the question; don't retype it. |
| 4 | 0 | Two problems. There is no `target="_blank"`, so the link does **not** open in a new tab. The link text became `Visit GitHub that opens in a NEW tab.` because the instruction was pasted in as the text. It should be `<a href="https://github.com" target="_blank">Visit GitHub</a>`. There is also a stray space at the start of the `href` (browsers forgive it, but remove it). |
| 5 | 1 | ✓ Flag: the alt text should be `Random photo` (lowercase *p*). |
| 6 | 1 | ✓ |
| 7 | 1 | ✓ |
| 8 | ½ | The table structure is right, but the header row uses `<td>`. Header cells should be `<th>`, which is what makes them a header row: bold, centered, and read as headers by screen readers. |
| 9 | 1 | ✓ |
| 10 | 1 | ✓ Labels are correctly linked with `for`. Flag: the label should be `Email:` (with a colon). |
| 11 | 1 | ✓ |
| 12 | 0 | Left blank. Example answer: *a block element starts on a new line and takes the full width, while an inline element stays in the line of text and is only as wide as its content.* |

### Section 2 — CSS (7/9)

| Q | Mark | Comment |
|---|------|---------|
| 13 | 1 | ✓ |
| 14 | 1 | ✓ |
| 15 | 1 | ✓ |
| 16 | 1 | ✓ All five properties are present. |
| 17 | ½ | The color changes to red, but `text-decoration: none;` is missing, so the underline stays. |
| 18 | 1 | ✓ |
| 19 | ½ | `border: none;` is missing, so the buttons keep the browser's default grey border. |
| 20 | 1 | ✓ `display: none` is the right choice, because `visibility: hidden` would still take up space. |
| 21 | 0 | **The media query never runs.** `and(max-width:600px)` has no space after `and`. CSS then reads `and(` as a function name, the whole query becomes invalid, and it is ignored. You can check this by narrowing the browser window: the cards never stack. Fix: `@media (max-width: 600px) { ... }` (you can drop `only screen`, but if you keep it, put a space after `and`). |

### Section 3 — JavaScript (12/15)

Console output when the page loads:
```
Rabiya 20
Rabiya is 20 years old
string number boolean object
7
3  8  1  9  4
[4, 6, 10, 20]
[5, 10, 20]
Web Development
B
```

| Q | Mark | Comment |
|---|------|---------|
| 22 | 1 | ✓ |
| 23 | 1 | ✓ |
| 24 | 1 | ✓ It correctly shows that `typeof null` is `"object"`, which is a well-known JavaScript quirk. Printing `typeof 42` directly would have been enough; the extra variables aren't needed. |
| 25 | ½ | The explanation is correct. However, the results are only written in a comment, and the question says **print** them: `console.log(5 == "5", 5 === "5");`. Also note that JavaScript's boolean is `false`, not `False` (that's Python). |
| 26 | ½ | The function is correct, but **it is commented out**, so it never runs and `square(6)` (36) never prints. It looks like you commented it out because Q27 also used the name `square` and the two clashed. The real fix is to give Q27 its own name (see below). |
| 27 | 0 | Three problems. It's named `square` instead of `squareArrow`. It `return n` instead of `n * n`, so it prints **7 instead of 49**. The question asked for `squareArrow(7)`. Correct version: `const squareArrow = (n) => n * n; console.log(squareArrow(7));` |
| 28 | 1 | ✓ Correct use of `for...of` with `nums`. |
| 29 | ½ | `.map()` is used correctly, but on a **new array `[2,3,5,10]`** instead of `nums`. Expected output: `[6, 16, 2, 18, 8]`. |
| 30 | ½ | `.filter()` is used correctly, but again on a new array `[5,10,2,20,1]` instead of `nums`. Expected output: `[8, 9, 4]`. Q28–Q30 are meant to build on each other using the same `nums`. |
| 31 | 1 | ✓ |
| 32 | 1 | ✓ Prints `B` for 78 marks. |
| 33 | 1 | ✓ |
| 34 | 1 | ✓ Clean: the counter lives outside the listener and uses a template literal for the text. |
| 35 | 1 | ✓ Correct `classList.toggle("hidden")`, and it works together with your Q20 `.hidden` class. |
| 36 | 1 | ✓ Uses `preventDefault()`, reads both values, checks for empty fields and writes into `#output`. This is the best answer on the paper. Flag: the message should be `Thanks, <name>! We will email <email>.` Your version is missing the `!` and the final `.`. |

### Section 4 — Git & GitHub (11.5/13)

| Q | Mark | Comment |
|---|------|---------|
| 37 | 1 | ✓ Stronger wording: *Git is the version-control tool that tracks history locally; GitHub is a website that hosts Git repositories online for sharing and collaboration.* |
| 38 | 1 | ✓ `git init` |
| 39 | 1 | ✓ `git status` |
| 40 | ½ | `git add.` has no space, so Git replies *"'add.' is not a git command"*. It must be `git add .` The commit line is correct. |
| 41 | 1 | ✓ `git log` |
| 42 | 1 | ✓ Accepted. Next time use the URL the question gave you: `git remote add origin https://github.com/<you>/my-project.git` |
| 43 | 1 | ✓ `git push -u origin main` |
| 44 | 1 | ✓ `git clone <URL>` |
| 45 | 1 | ✓ `git pull` |
| 46 | ½ | `git switch -c feature-login` is the correct answer. However, you also wrote `git branch feature-login` above it. If you run both in order, the second command fails because the branch already exists, and the question asked for **one step**. Give only the one command. `git checkout -b feature-login` is also accepted. |
| 47 | 1 | ✓ |
| 48 | 1 | ✓ Good answer: explains both what a merge conflict is and how to fix it (edit → `add` → `commit`). |
| 49 | ½ | The purpose is correct, but the **example is missing**. For Python, typical entries are `__pycache__/`, `.env`, `venv/` and `*.pyc`. |

### Bonus — Q50 ✅

https://rrk-14.github.io/Test5-Rabiya/ is live. It shows the correct title, the heading, the cards, the form and the buttons. Well done for getting a real site deployed.

---

### Top 5 fixes (in order of impact)
1. **Functions (Q26–Q27):** give each function its own name, and make sure the arrow function returns `n * n`. Never comment out a correct answer to avoid a name clash; rename instead.
2. **Use the data the question gives you (Q29–Q30):** use `nums`, not a new array.
3. **Media query spacing (Q21):** use `and (max-width: 600px)`, because `and(` silently breaks the whole rule.
4. **Read every bullet in the question (Q4, Q17, Q19, Q49):** each one of these lost marks for a single missing property or attribute.
5. **Copy required strings from the question (Q3, Q10, Q36):** from here on, punctuation slips in required text will also start costing marks.

**Verdict:** A solid pass. The DOM and event-handling work (Q33–Q36) is genuinely good, and deploying to GitHub Pages is a real achievement. With a careful re-read of each question before moving on, this paper would have scored above 45/49. Revise functions and arrow functions before Test 6.
