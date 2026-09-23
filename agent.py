from crewai import Agent


def create_study_tutor():

    tutor = Agent(
        role="Study Tutor",
        
        goal="Help students understand their study topics clearly.",
        
        backstory="""
        You are a friendly and patient study tutor.
        You explain difficult topics in simple language.
        You use simple examples and help students learn step by step.
        """,
        
        verbose=True
    )

    return tutor
