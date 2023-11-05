# Import necessary libraries
import streamlit as st
import os
import requests
import time

# Retrieve the Perplexity AI Pro API key from the environment variable
API_KEY = os.environ["PERPLEXITY_AI_PRO_KEY"]

# Set the initial temperature and model ID
temperature = 0
model_id = "mistral-7b-instruct"

# Create a Streamlit interface header
st.write("**TextWeaver** :scroll: :lower_left_ballpoint_pen: :computer: AI-Powered Writing Experiment by **Sherwood Analytica**")
input_text = st.text_area("**Enter** the text you would like to process using the prompt in the box and press the **Let\'s Go** button to proceed.\n:red[You may get unsuitable or incorrect answers and should take full responsibility over how you use the generated output.]")
