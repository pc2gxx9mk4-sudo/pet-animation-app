import streamlit as st
import streamlit.components.v1 as components

# 1. MUST BE THE FIRST COMMAND
st.set_page_config(page_title="Pet Animation Studio", page_icon="🐱", layout="wide")

# 2. FORCE CSS (Background & Fonts)
st.markdown("""
<style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&display=swap');

    /* BACKGROUND COLOR - Forces the whole page to be a gradient */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }

    /* Animation Keyframes */
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* TITLE STYLE */
    h1 {
        font-family: 'Fredoka', sans-serif;
        color: white;
        text-shadow: 2px 2px 4px #000000;
        text-align: center;
    }
    
    /* TEXT STYLE */
    p {
        font-family: 'Fredoka', sans-serif;
        color: white;
        font-size: 1.2rem;
        text-align: center;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
    }
</style>
""", unsafe_allow_html=True)

# 3. HEADER CONTENT
st.title("🐱 Pet Animation Studio")
st.write("Turn your pet into a movie star! Upload a photo below.")

# 4. CENTER THE FORM
# We use columns here. The form goes in the middle (col2).
# col1 and col3 are empty space so you can see the background.
col1, col2, col3 = st.columns([1, 2, 1]) 

with col2:
    # This box makes the form look like it's floating
    st.markdown("### 📝 Fill out the form below:")
    tally_url = "https://tally.so/embed/1AdJk4"
    components.iframe(tally_url, height=800, scrolling=True)
