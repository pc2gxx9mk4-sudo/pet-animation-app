import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config
st.set_page_config(page_title="Pet Animation Studio", page_icon="🐱", layout="centered")

# 2. FANCY CSS INJECTION
st.markdown("""
<style>
    /* IMPORT GOOGLE FONT: 'Fredoka' (Cute & Rounded) */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&display=swap');

    /* ANIMATED BACKGROUND */
    /* This defines the moving colors: Blue -> Pink -> Purple -> Blue */
    .stApp {
        background: linear-gradient(-45deg, #A8C0FF, #3f2b96, #FF8E53, #ff6b6b);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* GLASSMORPHISM CARD FOR TITLE */
    /* This creates the 'frosted glass' white box effect */
    .glass-container {
        background: rgba(255, 255, 255, 0.75);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 30px;
        text-align: center;
        margin-bottom: 30px;
    }

    /* TYPOGRAPHY STYLING */
    h1 {
        font-family: 'Fredoka', sans-serif;
        color: #FF4B4B; /* Streamlit Red/Pink for title */
        font-weight: 600;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin: 0;
    }
    
    p {
        font-family: 'Fredoka', sans-serif;
        color: #31333F;
        font-size: 1.2rem;
        margin-top: 10px;
    }
    
    /* Hide the default Streamlit top menu/footer for cleaner look */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# 3. The "Hero" Section (Inside the Glass Container)
# We use HTML here to wrap the title in our custom 'glass-container' class
st.markdown("""
<div class="glass-container">
    <h1>🐱 Pet Animation Studio</h1>
    <p>✨ Turn your furry friend into a movie star! ✨<br>
    Upload a photo below to generate your custom animation.</p>
</div>
""", unsafe_allow_html=True)

# 4. Embed the Tally Form
tally_url = "https://tally.so/embed/1AdJk4"

# Note: If possible, go to Tally settings and set the form background to 'Transparent'
components.iframe(tally_url, height=800, scrolling=True)
