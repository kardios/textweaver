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
st.write("**:red[May produce unsuitable or incorrect answers. You bear full responsibility over how you use the output.]**")

choose_instruction = st.selectbox("Choose an instruction", ('Summarize', 'Main Points', 'Alternative', 'Improvement', 'Customise'))

instruction = ''
if choose_instruction  == 'Summarize':
  instruction = "Read the text below and produce an informative and coherent summary. Include the main ideas and key details from the text. Think step by step."
elif choose_instruction  == 'Main Points':
  instruction = "Read the text below and summarize the main ideas and key details into bullet points. Recognize the overall structure of the text and create bullet points that reflect this structure. The output should be presented in a clear and organized way. Do not start with any titles."
elif choose_instruction  == 'Alternative':
  instruction = "Read the text below and highlight any missing or incomplete angles."
elif choose_instruction  == 'Improvement':
  instruction = "Read the text below and suggest critical areas for improvement."
elif choose_instruction  == 'Customise':
  instruction = "Read the text below and propose follow-up actions."

instruction_text = st.text_input("**Refine** the instruction", instruction)
context_text = st.text_area("**Enter** the text you would like to process using the prompt in the box below and press the **Let\'s Go** button to proceed.")

if st.button('Let\'s Go!'):
  st.write("You pressed the button!")
