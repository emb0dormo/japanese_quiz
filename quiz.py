"""Vocabulary data and quiz state for the JLPT N5 command-line quiz."""

from dataclasses import dataclass


VOCABULARY: dict[str, str] = {
    "水 (みず)": "water",
    "人 (ひと)": "person",
    "学校 (がっこう)": "school",
    "先生 (せんせい)": "teacher",
    "友達 (ともだち)": "friend",
    "食べる (たべる)": "to eat",
    "飲む (のむ)": "to drink",
    "大きい (おおきい)": "big",
    "小さい (ちいさい)": "small",
    "今日 (きょう)": "today",
    "明日 (あした)": "tomorrow",
    "本 (ほん)": "book",
}

CHOICE_LABELS = ("A", "B", "C", "D")


@dataclass(frozen=True)
class Question:
    """A vocabulary question and its four labeled translation choices."""

    prompt: str
    options: tuple[tuple[str, str], ...]
    correct_label: str
    correct_answer: str


class Quiz:
    """Build and track a sequential multiple-choice vocabulary quiz."""

    def __init__(self, vocabulary: dict[str, str] | None = None) -> None:
        self._vocabulary = dict(vocabulary if vocabulary is not None else VOCABULARY)
        translations = list(dict.fromkeys(self._vocabulary.values()))
        if len(translations) < len(CHOICE_LABELS):
            raise ValueError("At least four distinct translations are required.")

        self.questions = tuple(
            self._make_question(index, prompt, answer, translations)
            for index, (prompt, answer) in enumerate(self._vocabulary.items())
        )
        self.current_index = 0
        self.score = 0

    @staticmethod
    def _make_question(
        index: int, prompt: str, answer: str, translations: list[str]
    ) -> Question:
        distractors = [translation for translation in translations if translation != answer]
        start = index % len(distractors)
        selected = [
            distractors[(start + offset) % len(distractors)]
            for offset in range(len(CHOICE_LABELS) - 1)
        ]
        correct_position = index % len(CHOICE_LABELS)
        choices = selected[:correct_position] + [answer] + selected[correct_position:]
        options = tuple(zip(CHOICE_LABELS, choices))
        return Question(
            prompt=prompt,
            options=options,
            correct_label=CHOICE_LABELS[correct_position],
            correct_answer=answer,
        )

    @property
    def current_question(self) -> Question | None:
        """Return the next question, or None when the quiz is complete."""
        if self.is_complete:
            return None
        return self.questions[self.current_index]

    @property
    def is_complete(self) -> bool:
        return self.current_index >= len(self.questions)

    @property
    def total_questions(self) -> int:
        return len(self.questions)

    @property
    def percentage(self) -> float:
        if not self.questions:
            return 0.0
        return self.score / len(self.questions) * 100

    def submit_answer(self, answer: str) -> bool:
        """Validate and submit a letter or translation; return whether it is right."""
        if self.is_complete:
            raise RuntimeError("The quiz is already complete.")

        normalized = answer.strip().casefold()
        if not normalized:
            raise ValueError("Answer cannot be empty.")

        question = self.current_question
        assert question is not None
        answer_by_label = {label.casefold(): label for label, _ in question.options}
        label_by_answer = {
            option.casefold(): label for label, option in question.options
        }

        if normalized in answer_by_label:
            selected_label = answer_by_label[normalized]
        elif normalized in label_by_answer:
            selected_label = label_by_answer[normalized]
        else:
            choices = ", ".join(CHOICE_LABELS)
            raise ValueError(f"Choose one of the available options: {choices}.")

        is_correct = selected_label == question.correct_label
        if is_correct:
            self.score += 1
        self.current_index += 1
        return is_correct
