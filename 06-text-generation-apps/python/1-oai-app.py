from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI()
deployment = "gpt-5-mini"

# add your completion code
<<<<<<< HEAD:06-text-generation-apps/python/1-oai-app.py
prompt = "Complete the following: Once upon a time there was a man who lived in Nigeria"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)
=======
prompt = "Complete the following: Once upon a time there was a"
# make a request using the Responses API
response = client.responses.create(model=deployment, input=prompt, store=False)
>>>>>>> upstream/main:06-text-generation-apps/python/oai-app.py

# print response
print(response.output_text)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
