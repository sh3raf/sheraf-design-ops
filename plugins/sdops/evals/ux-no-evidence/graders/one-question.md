---
type: llm
---

Count the questions the reply asks the designer. A question asks for a new answer: a value, a link or a decision.
Not counted: asking the designer to approve the proposal table shown in the same reply, setup steps, statements of what is missing, and a list of defaults the assistant will use unless the designer objects.
PASS if the reply asks at most one question.
FAIL if it asks two or more separate questions, including a numbered or bulleted list of things the designer must answer.
