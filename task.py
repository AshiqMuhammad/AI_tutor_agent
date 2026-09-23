from crewai import Task


def create_study_task(tutor, question):

    task = Task(
        description=f"""
        A student has asked this question:

        {question}

        Explain the answer in very simple language.

        Follow these steps:

        1. Explain the concept.
        2. Give a simple example.
        3. Give the important formula if needed.
        4. Give one small practice question.
        """,

        expected_output="""
        A clear and beginner-friendly explanation
        with an example and a practice question.
        """,

        agent=tutor
    )

    return task
