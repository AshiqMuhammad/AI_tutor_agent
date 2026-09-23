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

    /* Main title */
    .main-title {
        font-size: 46px;
        font-weight: 700;
        color: #F9FAFB;
        margin-bottom: 6px;
    }

    /* Subtitle */
    .subtitle {
        font-size: 17px;
        color: #9CA3AF;
        margin-bottom: 28px;
    }

    /* Feature cards */
    .feature-card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 16px;
        padding: 20px;
        min-height: 120px;
        margin-bottom: 20px;
    }

    .feature-title {
        font-size: 18px;
        font-weight: 600;
        color: #F9FAFB;
        margin-bottom: 8px;
    }

    .feature-text {
        font-size: 14px;
        color: #9CA3AF;
        line-height: 1.5;
    }

    /* Question label */
    .question-title {
        font-size: 24px;
        font-weight: 600;
        color: #F9FAFB;
        margin-top: 15px;
        margin-bottom: 12px;
    }

    /* Text area */
    textarea {
        background-color: #111827 !important;
        color: #F9FAFB !important;
        border: 1px solid #374151 !important;
        border-radius: 12px !important;
    }

    /* Ask button */
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

    /* Answer heading */
    .answer-title {
        background-color: #111827;
        border: 1px solid #312E81;
        border-bottom: none;
        border-radius: 16px 16px 0 0;
        padding: 20px 24px 10px 24px;
        color: #A78BFA;
        font-size: 22px;
        font-weight: 600;
        margin-top: 30px;
    }

    /* Answer content */
    .answer-content {
        background-color: #111827;
        border: 1px solid #312E81;
        border-top: none;
        border-radius: 0 0 16px 16px;
        padding: 10px 24px 24px 24px;
        color: #E5E7EB;
        line-height: 1.7;
        margin-bottom: 30px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #6B7280;
        font-size: 13px;
        padding: 25px 0 10px 0;
        border-top: 1px solid #1F2937;
        margin-top: 50px;
    }

    .footer-title {
        color: #9CA3AF;
        font-size: 15px;
        font-weight: 600;
        margin-bottom: 6px;
    }

    /* Remove unnecessary Streamlit spacing */
    div[data-testid="stVerticalBlock"] {
        gap: 0.5rem;
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
            Understand difficult topics using simple and clear language.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🧠 Step-by-Step Learning</div>
        <div class="feature-text">
            Learn concepts gradually with examples and explanations.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col3:

    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📝 Practice</div>
        <div class="feature-text">
            Get practice questions to check your understanding.
        </div>
    </div>
    """, unsafe_allow_html=True)


# =========================
# QUESTION SECTION
# =========================

st.markdown(
    '<div class="question-title">Ask Your Tutor</div>',
    unsafe_allow_html=True
)

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

                # Create AI tutor
                tutor = create_study_tutor()

                # Create task
                task = create_study_task(
                    tutor,
                    question
                )

                # Run CrewAI
                answer = run_study_tutor(
                    tutor,
                    task
                )

                # =========================
                # ANSWER
                # =========================

                st.markdown(
                    '<div class="answer-title">🤖 Tutor\'s Answer</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="answer-content">',
                    unsafe_allow_html=True
                )

                st.write(answer)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error("The tutor could not generate an answer.")

                st.markdown("### 🔍 Error Details")

                st.exception(e)


# =========================
# FOOTER
# =========================

st.markdown("""
<div class="footer">

    <div class="footer-title">
        📚 Study Tutor AI
    </div>

    <div>
        Your personal AI tutor for simple and effective learning.
    </div>

    <div style="margin-top: 10px;">
        Built with Streamlit • CrewAI • Groq
    </div>

</div>
""", unsafe_allow_html=True)
