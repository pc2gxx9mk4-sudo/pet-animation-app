import streamlit as st
import streamlit.components.v1 as components

# 1. Page Config (Title, Icon)
st.set_page_config(page_title="Pet Animation Studio", page_icon="🐱")

# 2. Main Title
st.title("🐱 Pet Animation Studio")
st.write("Turn your pet into a movie star! Upload a photo below, and we will generate a custom animation for you.")

# 3. Embed the Tally Form
# REPLACE THE URL BELOW with your specific Tally Embed URL
tally_url = "https://tally.so/embed/YOUR_FORM_ID?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"

# This creates the window for the form
components.iframe(tally_url, height=800, scrolling=True)