# Implementation plan

> This file records my project-specific steps reviewed before coding.

## Steps
1. Create core data structures in `quiz.py` to hold the N5 vocabulary dictionary and initialize the quiz session state.
2. Implement the CLI question loop in `main.py` fulfilling R1 and R2, presenting cards and tracking scores.
3. Implement robust input sanitization and boundary checking in `quiz.py` to handle empty strings or invalid selections per R3.
4. Create an automated test suite in `test_quiz.py` using `pytest` to verify scoring logic and boundary validation.
5. Perform a full end-to-end walkthrough run of the quiz to judge overall usability and playability.

## Later changes, if any
None.