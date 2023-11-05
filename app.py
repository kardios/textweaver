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
input_text = st.text_area("**Enter** the text you would like to process using the prompt in the box and press the **Let\'s Go** button to proceed. :red[Be mindful that as this is an AI-powered app, you may receive unsuitable or incorrect answers. You should take full responsibility over how you use the generated output.]")
