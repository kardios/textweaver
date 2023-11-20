# Import necessary libraries
import streamlit as st
import os
import requests
import time
import json

# Retrieve the Perplexity AI Pro API key from the environment variable
API_KEY = os.environ["PERPLEXITY_AI_PRO_KEY"]

# Create a Streamlit interface header
st.write("**TextWeaver** :memo: AI-Powered Writing Experiment :memo: **Sherwood Analytica**")
st.write("**:red[May produce unsuitable or incorrect answers. You bear full responsibility over how you use the output.]**")

# Set the initial temperature and model ID
temperature = 0
model_id = "llama-2-70b-chat"

choose_instruction = st.selectbox("**Choose** an instruction", ('Shorten the text into a summary', 'Identify possible biases in the text', 'Seek views disagreeing with the text', 'Find angles missing from the text', 'Compare the text with historical events', 'Generate question-answer pairs', 'Customise your own unique prompt'))

instruction = ''
if choose_instruction  == 'Shorten the text into a summary':
  instruction = "Produce an informative and coherent summary. Include the main ideas and key details from the text."
elif choose_instruction == 'Identify possible biases in the text':
  instruction = "Highlight possible biases in the text."
elif choose_instruction == 'Seek views disagreeing with the text':
  instruction = "Offer perspectives that disagree with the text."
elif choose_instruction == 'Find angles missing from the text':
  instruction = "Offer perspectives that are missing from the text."
elif choose_instruction == 'Compare the text with historical events':
  instruction = "Draw similiarities and differences to historical events in the last century."
elif choose_instruction  == 'Generate question-answer pairs':
  instruction = "Generate question-answer pairs from the text."
elif choose_instruction  == 'Customise your own unique prompt':
  instruction = "Propose follow-up actions."

instruction_text = st.text_input("**Refine** the instruction", instruction)
context_text = st.text_area("**Enter** the text to process using the above instruction")
st.write("**Press** button to proceed")
if st.button('Let\'s Go with **Llama-2**'):
  
  start = time.time()

  instruction = "Read the INPUT below. " + instruction + "\n\nINPUT:"
  
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
    st.write("**Answer**")
    answer = data['choices'][0]['message']['content']
    st.write(answer)
    st.divider()
    st.write("Model:", data['model'])
    st.write("Prompt Tokens:", data['usage']['prompt_tokens'])
    st.write("Completion Tokens:", data['usage']['completion_tokens'])
    st.write("Total Tokens:", data['usage']['total_tokens'])
    st.write("Time to generate: " + str(round(end-start,2)) + " seconds")
  else:
    st.write(data['error']['message'])
