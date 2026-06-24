import streamlit as st

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="LeaveFlow",
    page_icon="🏢",
    layout="wide"
)

# ==================================
# CUSTOM CSS
# ==================================

st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
    color:white;
}

[data-testid="metric-container"]{
    background-color:#1e293b;
    border:1px solid #334155;
    padding:20px;
    border-radius:15px;
}

div.stButton > button{
    background-color:#3b82f6;
    color:white;
    border-radius:10px;
    height:50px;
    width:100%;
}

</style>
""", unsafe_allow_html=True)

# ==================================
# APP STARTS HERE
# ==================================

st.title("🏢 LeaveFlow")

st.metric("Pending Leaves", 5)