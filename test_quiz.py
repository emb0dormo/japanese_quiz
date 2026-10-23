import pytest

from quiz import CHOICE_LABELS, Quiz


def test_quiz_loads_vocabulary_as_four_choice_questions() -> None:
    quiz = Quiz()

    assert quiz.total_questions >= 4
    assert quiz.current_question is not None
    assert tuple(label for label, _ in quiz.current_question.options) == CHOICE_LABELS


@pytest.mark.parametrize("answer", ["", "   "])
def test_empty_answer_is_rejected_without_advancing(answer: str) -> None:
    quiz = Quiz()

    with pytest.raises(ValueError, match="cannot be empty"):
        quiz.submit_answer(answer)

    assert quiz.current_index == 0
    assert quiz.score == 0


@pytest.mark.parametrize("answer", ["E", "0", "5", "not an option"])
def test_invalid_answer_is_rejected_without_advancing(answer: str) -> None:
    quiz = Quiz()

    with pytest.raises(ValueError, match="available options"):
        quiz.submit_answer(answer)

    assert quiz.current_index == 0
    assert quiz.score == 0


def test_letter_answer_is_case_insensitive_and_scores_correctly() -> None:
    quiz = Quiz()
    question = quiz.current_question
    assert question is not None

    assert quiz.submit_answer(question.correct_label.lower()) is True
    assert quiz.current_index == 1
    assert quiz.score == 1


def test_translation_answer_is_case_insensitive() -> None:
    quiz = Quiz()
    question = quiz.current_question
    assert question is not None

    assert quiz.submit_answer(question.correct_answer.upper()) is True
    assert quiz.score == 1


def test_wrong_valid_answer_advances_without_scoring() -> None:
    quiz = Quiz()
    question = quiz.current_question
    assert question is not None
    wrong_label = next(
        label for label, _ in question.options if label != question.correct_label
    )

    assert quiz.submit_answer(wrong_label) is False
    assert quiz.current_index == 1
    assert quiz.score == 0


def test_final_percentage_and_completed_quiz_state() -> None:
    quiz = Quiz({"a": "one", "b": "two", "c": "three", "d": "four"})

    for question in quiz.questions:
        quiz.submit_answer(question.correct_label)

    assert quiz.is_complete
    assert quiz.current_question is None
    assert quiz.score == 4
    assert quiz.percentage == 100.0
    with pytest.raises(RuntimeError, match="already complete"):
        quiz.submit_answer("A")


def test_quiz_requires_enough_choices() -> None:
    with pytest.raises(ValueError, match="At least four distinct"):
        Quiz({"a": "one", "b": "two", "c": "three"})


def test_quiz_requires_distinct_translations() -> None:
    with pytest.raises(ValueError, match="At least four distinct"):
        Quiz({"a": "same", "b": "same", "c": "same", "d": "same"})
