# Checks and decisions

> This file records what I checked, what actually happened, and why I accepted or changed the work. It does not repeat setup instructions or the implementation plan.

## Concrete checks

| Check / requirement | Given | When | Expected result | Actual result / pass or fail |
|---|---|---|---|---|
| C1 / R1 — vocabulary and questions | The default N5 vocabulary list. | Start the quiz and inspect its questions. | Vocabulary includes Japanese terms and English translations; each question presents four labeled choices. | The quiz loaded 12 vocabulary questions with four choices each.  |
| C2 / R2 — correct answer and score | A question is active and its correct A-D letter is known. | Submit the correct letter, including lowercase input. | The answer is accepted case-insensitively, feedback is shown, and the score increases by one. | Automated test confirmed lowercase correct-letter input scores one point.  |
| C3 / R3 — empty and invalid input | The first question is active. | Submit a blank answer and then an invalid choice (`E`). | Each input is rejected without advancing the question or changing the score. | CLI walkthrough displayed validation messages for both inputs; the first question remained active until a valid answer.  |
| C4 / R3 — completion and percentage | All 12 questions have been answered. | Complete the quiz with correct answers. | The quiz ends and displays the final score and percentage. | CLI displayed `Final score: 12/12 (100.0%).`  |

## Two review decisions

- Plan decision: I used A-D multiple choice in order to have boundaries and it's for learning and not actual testing japanese knowledge
- Code decision: I kept question data, answer validation, and scoring in `quiz.py`, separate from input/output in `main.py`. This makes the quiz rules testable without running the CLI and lets invalid answers be rejected without advancing the question.

## Automated tests

- Test file and behaviour checked: `test_quiz.py`; vocabulary and choices, answer validation, case-insensitive answers, scoring, completion, percentage calculation, and insufficient distinct translations.
- Command I ran: `python -m pytest` from the project directory.
- Final result: **13 tests passed** using Python 3.11.9 and pytest 9.1.1.
- Correction and rerun: The first attempt could not run because pytest was not installed in the configured environment. After installing pytest, the full test suite passed. The first CLI walkthrough also exposed a Windows console encoding issue; after configuring UTF-8 output, the walkthrough displayed Japanese correctly.

## Realistic use and final judgment

- Task I tried: Start the quiz, enter blank and invalid input, then answer each vocabulary question with its correct A-D choice.
- Outcome: Invalid inputs were rejected without skipping the question. Japanese text displayed, all 12 questions completed, and the final score was 12/12 (100.0%).
- Judgment: Done for the stated functional requirements based on the automated tests and the command-line walkthrough. The walkthrough confirms the quiz can be completed
- Remaining limitation or unfinished work: The vocabulary set contains 12 terms and the correct answer position cycles A, B, C, D in a predictable pattern. Expanding the vocabulary and randomizing answer positions would make practice less predictable.
