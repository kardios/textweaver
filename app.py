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
