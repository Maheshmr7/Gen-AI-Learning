import streamlit as st

# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="EduAI Report Card",
    page_icon="🎓",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.big-title {
    text-align:center;
    font-size:48px;
    font-weight:bold;
    color:#4CAF50;
}

.sub-title {
    text-align:center;
    font-size:20px;
    color:gray;
    margin-bottom:30px;
}

.card {
    padding:20px;
    border-radius:15px;
    background-color:#1e1e1e;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

st.markdown(
    "<div class='big-title'>🎓 EduAI Student Report Card</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Generate intelligent student performance reports</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# =====================================
# STUDENT INFORMATION
# =====================================

with st.container(border=True):

    st.subheader("👨‍🎓 Student Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        student_name = st.text_input(
            "Student Name"
        )

    with col2:
        student_class = st.text_input(
            "Class"
        )

    with col3:
        roll_no = st.text_input(
            "Roll Number"
        )

# =====================================
# START BUTTON
# =====================================

if "show_marks" not in st.session_state:
    st.session_state.show_marks = False

if st.button("🚀 Start Evaluation"):

    st.session_state.show_marks = True

# =====================================
# MARKS ENTRY SECTION
# =====================================

if st.session_state.show_marks:

    st.markdown("---")

    with st.container(border=True):

        st.subheader("📚 Enter Subject Marks")

        col1, col2 = st.columns(2)

        with col1:

            english = st.number_input(
                "English",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Enter Marks"
            )

            maths = st.number_input(
                "Maths",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Enter Marks"
            )

            science = st.number_input(
                "Science",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Enter Marks"
            )

        with col2:

            evs = st.number_input(
                "EVS",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Enter Marks"
            )

            computer = st.number_input(
                "Computer Science",
                min_value=0,
                max_value=100,
                value=None,
                placeholder="Enter Marks"
            )

    # =====================================
    # GENERATE REPORT
    # =====================================

    if st.button("📋 Generate Report Card"):

        marks = [
            english,
            maths,
            science,
            evs,
            computer
        ]

        if None in marks:

            st.error("Please enter all subject marks")

        else:

            total = sum(marks)

            percentage = total / 5

            # =====================================
            # GRADE
            # =====================================

            if percentage >= 90:
                grade = "A+ 🏆"
                feedback = "Outstanding Performance"

            elif percentage >= 80:
                grade = "A 🥇"
                feedback = "Excellent Work"

            elif percentage >= 70:
                grade = "B 👍"
                feedback = "Very Good"

            elif percentage >= 60:
                grade = "C 📚"
                feedback = "Good"

            elif percentage >= 50:
                grade = "D ⚠️"
                feedback = "Needs Improvement"

            else:
                grade = "F ❌"
                feedback = "Failed"

            st.markdown("---")

            st.header("📊 Student Performance Dashboard")

            # =====================================
            # TOP METRICS
            # =====================================

            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.metric(
                    "Student",
                    student_name
                )

            with col2:
                st.metric(
                    "Total Marks",
                    total
                )

            with col3:
                st.metric(
                    "Percentage",
                    f"{percentage:.2f}%"
                )

            with col4:
                st.metric(
                    "Grade",
                    grade
                )

            st.markdown("---")

            # =====================================
            # SUBJECT CARDS
            # =====================================

            st.subheader("📚 Subject Performance")

            c1, c2, c3, c4, c5 = st.columns(5)

            c1.metric("English", english)
            c2.metric("Maths", maths)
            c3.metric("Science", science)
            c4.metric("EVS", evs)
            c5.metric("Computer", computer)

            st.markdown("---")

            # =====================================
            # PROGRESS
            # =====================================

            st.subheader("📈 Overall Progress")

            st.progress(int(percentage))

            if percentage >= 90:
                st.success(feedback)
                st.balloons()

            elif percentage >= 80:
                st.success(feedback)

            elif percentage >= 70:
                st.info(feedback)

            elif percentage >= 60:
                st.warning(feedback)

            else:
                st.error(feedback)

            st.markdown("---")

            # =====================================
            # AI FEEDBACK
            # =====================================

            st.subheader("🤖 AI Teacher Feedback")

            if percentage >= 90:
                st.success(
                    f"{student_name} demonstrates exceptional academic performance and strong subject mastery."
                )

            elif percentage >= 80:
                st.info(
                    f"{student_name} is performing very well with excellent overall consistency."
                )

            elif percentage >= 70:
                st.info(
                    f"{student_name} has a solid foundation and should focus on improving weaker subjects."
                )

            elif percentage >= 60:
                st.warning(
                    f"{student_name} requires additional practice and revision to improve overall performance."
                )

            else:
                st.error(
                    f"{student_name} needs significant academic support and regular study habits."
                )

            st.markdown("---")

            st.success("✅ Report Card Generated Successfully")