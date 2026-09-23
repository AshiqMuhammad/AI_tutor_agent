```python
import streamlit as st

from agent import create_study_tutor
from task import create_study_task
from crew import run_study_tutor


# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Study Tutor AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

    /* Main background */
    .stApp {
        background-color: #0B1120;
        color: #E5E7EB;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1F2937;
    }

    /* Main heading */
    .main-title {
        font-size: 48px;
        font-weight: 700;
        color: #F9FAFB;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #9CA3AF;
        margin-bottom: 30px;
    }

    /* Feature cards */
    .feature-card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .feature-title {
        font-size: 18px;
        font-weight: 600;
        color: #F9FAFB;
    }

    .feature-text {
        font-size: 14px;
        color: #9CA3AF;
    }

    /* Input box */
    textarea {
        background-color: #111827 !important;
        color: #F9FAFB !important;
        border: 1px solid #374151 !important;
        border-radius: 12px !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: 600;
        background: linear-gradient(90deg, #6366F1, #8B5CF6);
        color: white;
        transition: 0.3s;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #4F46E5, #7C3AED);
        transform: translateY(-2px);
    }

    /* Answer box */
    .answer-box {
        background-color: #111827;
        border: 1px solid #312E81;
        border-radius: 16px;
        padding: 25px;
        margin-top: 25px;
    }

    .answer-title {
        color: #A78BFA;
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6B7280;
        font-size: 13px;
        margin-top: 50px;
        padding: 20px;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("## 📚 Study Tutor AI")

    st.markdown("---")

    st.markdown("### 🎓 Learning Modes")

    st.write("💡 Explain Concepts")
    st.write("📝 Practice Questions")
    st.write("🧠 Understand Difficult Topics")
    st.write("📖 Learn Step by Step")

    st.markdown("---")

    st.markdown("### 🤖 AI Tutor")

    st.write(
        "Your personal AI tutor for understanding "
        "academic concepts in simple language."
    )

    st.markdown("---")

    st.caption("Powered by CrewAI + Groq + Streamlit")


# =========================
# HEADER
# =========================

st.markdown(
    '<div class="main-title">📚 Study Tutor AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your personal AI tutor for learning difficult concepts '
    'in a simple and understandable way.'
    '</div>',
    unsafe_allow_html=True
)


# =========================
# FEATURE CARDS
# =========================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">💡 Simple Explanations</div>
        <div class="feature-text">
            Understand difficult topics using simple language.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🧠 Step-by-Step Learning</div>
        <div class="feature-text">
            Learn concepts gradually with clear examples.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📝 Practice</div>
        <div class="feature-text">
            Get practice questions to test your knowledge.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# QUESTION SECTION
# =========================

st.markdown("### Ask Your Tutor")

question = st.text_area(
    "Enter your question",
    placeholder="Example: Explain Newton's second law in simple words...",
    height=150,
    label_visibility="collapsed"
)


# =========================
# ASK BUTTON
# =========================

if st.button("🚀 Ask Study Tutor"):

    if question.strip() == "":

        st.warning("Please enter a question first.")

    else:

        with st.spinner("🤖 Your AI tutor is thinking..."):

            try:

                tutor = create_study_tutor()

                task = create_study_task(
                    tutor,
                    question
                )

                answer = run_study_tutor(
                    tutor,
                    task
                )

                # =========================
                # ANSWER
                # =========================

                st.markdown("""
                <div class="answer-box">
                    <div class="answer-title">
                        🤖 Tutor's Answer
                    </div>
                """, unsafe_allow_html=True)

                st.write(answer)

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:

                st.error(
                    "Something went wrong. Please check your API key "
                    "and CrewAI configuration."
                )

                st.caption(str(e))


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

    📚 Study Tutor AI
    
    <br><br>
    
    Built with Streamlit • CrewAI • Groq

</div>
""", unsafe_allow_html=True)
```
