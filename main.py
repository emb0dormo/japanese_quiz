"""Command-line interface for the JLPT N5 vocabulary quiz."""

import sys

from quiz import Quiz


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")
    quiz = Quiz()
    print("JLPT N5 Vocabulary Quiz")

    while not quiz.is_complete:
        question = quiz.current_question
        assert question is not None

        print(f"\nQuestion {quiz.current_index + 1}/{quiz.total_questions}")
        print(f"What does {question.prompt} mean?")
        for label, option in question.options:
            print(f"  {label}. {option}")

        while True:
            try:
                answer = input("Your answer (A-D): ")
                correct = quiz.submit_answer(answer)
            except ValueError as error:
                print(error)
                continue
            except EOFError:
                print("\nInput ended before the quiz was complete.")
                return

            if correct:
                print("Correct!")
            else:
                print(f"Not quite. The correct answer is {question.correct_answer}.")
            print(f"Score: {quiz.score}/{quiz.current_index}")
            break

    print(
        f"\nFinal score: {quiz.score}/{quiz.total_questions} "
        f"({quiz.percentage:.1f}%)."
    )


if __name__ == "__main__":
    main()
