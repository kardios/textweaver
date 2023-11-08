# Import necessary libraries
import streamlit as st
import openai
import os
import requests
import time
import json

# Retrieve the Perplexity AI Pro API key from the environment variable
API_KEY1 = os.environ["PERPLEXITY_AI_PRO_KEY"]
API_KEY2 = os.environ["OPENAI_KEY"]
openai.api_key = API_KEY2

# Define a function to interact with the LLM for conversation
def chatgpt_conversation(conversation_log):
  response = openai.ChatCompletion.create(
    model = "gpt-4-1106-preview",
    temperature = 0,
    messages = conversation_log
  )
  conversation_log.append({
    'role': response.choices[0].message.role,
    'content': response.choices[0].message.content.strip()
  })
  return conversation_log

# Create a Streamlit interface header
st.write("**TextWeaver** :memo: AI-Powered Writing Experiment :memo: **Sherwood Analytica**")
st.write("**:red[May produce unsuitable or incorrect answers. You bear full responsibility over how you use the output.]**")

# Set the initial temperature and model ID
temperature = 0
model_id = "llama-2-70b-chat"

choose_instruction = st.selectbox("**Choose** an instruction", ('Summarize', 'Bias Check', 'Contrarian', 'Alternative', 'Reflection', 'Customise'))

instruction = ''
if choose_instruction  == 'Summarize':
  instruction = "Read the text below and produce an informative and coherent summary. Include the main ideas and key details from the text. Think step by step."
elif choose_instruction == 'Bias Check':
  instruction = "Read the text below and highlight any possible biases."
elif choose_instruction == 'Contrarian':
  instruction = "Read the text below and offer contrarian views."
elif choose_instruction == 'Alternative':
  instruction = "Read the text below and highlight any missing or incomplete angles."
elif choose_instruction == 'Reflection':
  instruction = "Read the text below and draw similiarities and differences to historical events in the last century."
elif choose_instruction  == 'Customise':
  instruction = "Read the text below and propose follow-up actions."

instruction_text = st.text_input("**Refine** the instruction", instruction)
context_text = st.text_area("**Enter** the text to process using the above instruction")
st.write("**Press** button to proceed")
if st.button('Let\'s Go with **Llama-2**'):
  
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
    "authorization": "Bearer " + API_KEY1
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

if st.button('Let\'s Go with **OpenAI**'):
  start = time.time()
  conversations = []
  conversations.append({'role': 'system', 'content': "Be precise and concise."})
  conversations.append({'role': 'user', 'content': instruction_text + "\n\n" + context_text})
  conversations = chatgpt_conversation(conversations)
  answer = conversations[-1]['content']
  st.write("**Answer**")
  st.write(answer)
  end = time.time()
  st.write("Time to generate: " + str(round(end-start,2)) + " seconds")
  st.divider()
