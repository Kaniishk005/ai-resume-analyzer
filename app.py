import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from matcher import calculate_match
from skill_gap import find_missing_skills
from recommender import recommend_learning


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Resume Analyzer",
    layout="wide",
    page_icon="📄"
)

# ---------------- HEADER ----------------
st.markdown("""
<h1 style='text-align: center;'>Resume Analyzer</h1>

<hr>
""", unsafe_allow_html=True)


# ---------------- INPUT SECTION ----------------
st.subheader("Input Details")

input_col1, input_col2 = st.columns(2)

with input_col1:
    uploaded_resume = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

with input_col2:
    job_description = st.text_area(
        "Paste Job Description",
        height=200,
        placeholder="Paste the job description here..."
    )


# ---------------- HELPER: SKILL CHIPS ----------------
def show_skill_chips(skills, color):
    if not skills:
        st.write("—")
        return

    html = ""
    for skill in skills:
        html += f"""
        <span style="
            background-color:{color};
            color:white;
            padding:6px 14px;
            margin:4px;
            border-radius:20px;
            display:inline-block;
            font-size:14px;
        ">
        {skill.title()}
        </span>
        """
    st.markdown(html, unsafe_allow_html=True)


# ---------------- PROCESSING ----------------
if uploaded_resume and job_description:

    # Resume processing
    resume_raw = extract_resume_text(uploaded_resume)
    resume_clean = clean_text(resume_raw)
    resume_skills = extract_skills(resume_clean)

    # Job description processing
    jd_clean = clean_text(job_description)
    jd_skills = extract_skills(jd_clean)

    # Matching & analysis
    resume_for_match = " ".join(resume_skills)
    jd_for_match = " ".join(jd_skills)
    match_percent = calculate_match(resume_for_match, jd_for_match)
    missing_skills = find_missing_skills(resume_skills, jd_skills)
    recommendations = recommend_learning(missing_skills)

    st.divider()

    # ---------------- MATCH SCORE ----------------
    st.subheader("Resume–Job Match")

    score_col1, score_col2 = st.columns([1, 3])

    with score_col1:
        st.metric("Match Score", f"{match_percent}%")

    with score_col2:
        st.progress(match_percent / 100)

    st.divider()

    # ---------------- SKILLS SECTION ----------------
    skills_col1, skills_col2 = st.columns(2)

    with skills_col1:
        st.subheader("✅ Detected Resume Skills")
        show_skill_chips(resume_skills, "#2E7D32")

    with skills_col2:
        st.subheader("❌ Missing Skills")
        show_skill_chips(missing_skills, "#C62828")

    st.divider()

    # ---------------- RECOMMENDATIONS ----------------
    st.subheader("📚 Personalized Learning Recommendations")

    if recommendations:
        for skill, suggestion in recommendations.items():
            st.info(f"**{skill.title()}** — {suggestion}")
    else:
        st.success("Your profile matches the job requirements very well!")

    st.divider()

    # ---------------- RAW RESUME TEXT ----------------
    with st.expander("🔍 View Extracted Resume Text"):
        st.text(resume_raw)

else:
    st.info("Upload a resume and paste a job description to start the analysis.")
