import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config
st.set_page_config(page_title="Pet Animation Studio", page_icon="🐱", layout="centered")

# 2. FORCE STYLING (The "Nuclear" Fix)
st.markdown("""
<style>
    /* 1. FORCE BACKGROUND CHANGE (Overrides Dark Mode) */
    .stApp {
        background: linear-gradient(120deg, #a1c4fd 0%, #c2e9fb 100%, #ffc3a0 100%) !important;
        background: -webkit-linear-gradient(to right, #ff9a9e, #fecfef, #feada6) !important;
        background: linear-gradient(to right, #ff9a9e, #fecfef, #feada6) !important;
    }

    /* 2. FORCE TEXT COLOR (Make text dark so it's readable) */
    h1, h2, h3, p, span, div {
        color: #333333 !important;
        font-family: 'Helvetica', sans-serif;
    }
    
    /* 3. STYLE THE TITLE SPECIFICALLY */
    h1 {
        text-align: center;
        font-weight: 800;
        color: #2c3e50 !important;
        padding-bottom: 20px;
    }
    
    /* 4. STYLE THE DESCRIPTION TEXT */
    .stMarkdown p {
        text-align: center;
        font-size: 18px !important;
    }

</style>
""", unsafe_allow_html=True)

# 3. Main Content
st.title("🐱 Pet Animation Studio")
st.write("Turn your pet into a movie star! Upload a photo below, and we will generate a custom animation for you.")

# 4. Embed Tally Form
# Note: This white box comes from Tally.so. To make it transparent, you must edit the design on Tally.so.
tally_url = "https://tally.so/embed/1AdJk4"
components.iframe(tally_url, height=900, scrolling=True)
