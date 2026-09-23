import streamlit as st
from crewai import Agent, LLM


def create_study_tutor():

    groq_llm = LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=st.secrets["GROQ_API_KEY"],
        base_url="https://api.groq.com/openai/v1"
    )

    tutor = Agent(
        role="Study Tutor",

        goal="Help students understand their study topics clearly.",

        backstory="""
        You are a friendly and patient study tutor.
        You explain difficult topics in very simple language.
        You use simple examples.
        You teach students step by step.
        """,

        llm=groq_llm,

        verbose=True
    )

    return tutor
