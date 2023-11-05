# Import necessary libraries
import streamlit as st
import os
import requests
import time
import json

# Retrieve the Perplexity AI Pro API key from the environment variable
API_KEY = os.environ["PERPLEXITY_AI_PRO_KEY"]

# Set the initial temperature and model ID
temperature = 0
model_id = "llama-2-70b-chat"

# Create a Streamlit interface header
st.write("**TextWeaver** :lower_left_ballpoint_pen: :computer: :scroll: AI-Powered Writing Experiment by **Sherwood Analytica**")
st.write("**:red[May produce unsuitable or incorrect answers. You bear full responsibility over how you use the output.]**")

choose_instruction = st.selectbox("**Choose** an instruction", ('Summarize', 'Main Points', 'Alternative', 'Improvement', 'Customise'))

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
context_text = st.text_area("**Enter** the text you would like to process using the prompt in the box")
st.write("**Press** button to proceed")
if st.button('Let\'s Go!'):
  
  start = time.time()
  
  url = "https://api.perplexity.ai/chat/completions"
  
  payload = {
    "model": model_id,
    "messages": [
      {
        "role": "system", 
        "content": "Be precise and concise."
      }, 
      {
        "role": "user",
        "content": instruction_text + "\n\n" + context_text
      }
    ], 
    "temperature": temperature
  }
  headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + API_KEY
  }
  
  response = requests.post(url, json=payload, headers=headers)
  data = json.loads(response.text)

  end = time.time()
  
  if data.get('error') == None:
    st.divider()
    st.write("**Answer**")
    answer = data['choices'][0]['message']['content']
    st.write(answer)
    st.divider()
    st.write("Model:", data['model'])
    st.write("Prompt Tokens:", data['usage']['prompt_tokens'])
    st.write("Completion Tokens:", data['usage']['completion_tokens'])
    st.write("Total Tokens:", data['usage']['total_tokens'])
    st.write("Time to generate: " + str(round(end-start,2)) + " seconds")
    st.divider()
  else:
    st.write(data['error']['message'])
