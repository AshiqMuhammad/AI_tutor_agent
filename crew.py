from crewai import Crew, Process


def run_study_tutor(tutor, task):

    crew = Crew(
        agents=[tutor],
        tasks=[task],
        process=Process.sequential,
        memory=False,
        verbose=True
    )

    result = crew.kickoff()

    return result
