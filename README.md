# JLPT N5 Flashcard Quiz Tool

> This file explains who the project is for, what it should do and how to run it.

## Purpose
Designed for beginner Japanese learners to practice and test core JLPT N5 vocabulary through an interactive command-line quiz, tracking scores and providing immediate feedback.

## Requirements
- R1: Load a predefined list of JLPT N5 vocabulary terms (kanji/kana and English translations).
- R2: Present questions sequentially, accept user guesses, compare answers case-insensitively, and maintain a running score.
- R3: Reject empty inputs or invalid choice bounds without crashing, and calculate a final percentage summary upon completion.

## Setup and use
- Prerequisites: Python 3.10+ and `pytest` (for automated tests).
- Setup: Clone the repository and navigate to the project root.
- Run: `python main.py`
- Play: For each Japanese vocabulary term, enter the letter (A-D) for its English translation. Letter input is case-insensitive; entering the full English option also works. Empty or invalid answers are rejected without advancing the question.
- Run tests: `pytest`

## Author and acknowledgements
- Name / student ID: Aleksei Petukhov / [6280775]
- AI tools used: GitHub Copilot 
- External code/resources: None.

See PLAN.md for the implementation plan and EVIDENCE.md for results and decisions.