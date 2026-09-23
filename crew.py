from crewai import Crew


def run_study_tutor(tutor, task):

    crew = Crew(
        agents=[tutor],
        tasks=[task],
        verbose=True,
        memory=False
    )

    result = crew.kickoff()

    return result
