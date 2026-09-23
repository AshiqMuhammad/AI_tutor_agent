import os
import streamlit as st
from crewai import Agent, LLM


def create_study_tutor():

    # Get Groq API key from Streamlit Secrets
    groq_api_key = st.secrets["GROQ_API_KEY"]

    # Give the key to CrewAI
    os.environ["GROQ_API_KEY"] = groq_api_key

    # Create Groq LLM
    groq_llm = LLM(
        model="groq/openai/gpt-oss-20b",
        api_key=groq_api_key,
        base_url="https://api.groq.com/openai/v1",
        temperature=0.3
    )

    # Create Study Tutor Agent
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

        allow_delegation=False,

        verbose=True
    )

    return tutor
