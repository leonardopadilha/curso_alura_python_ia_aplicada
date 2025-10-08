#import os
from openai import OpenAI
#from dotenv import load_dotenv

#load_dotenv()

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key = 'google-gemma-3-1b'
)

pergunta = input("Pergunta: ")

resposta_do_llm = client_openai.chat.completions.create(
    model="google/gemma-3-1b",
    messages=[
        { "role": "system", "content": "Você é um assistente de IA que sempre responde de forma resumida e muito sarcástica." },
        { "role": "user", "content": pergunta }
    ],
    temperature=1.0
)

print(resposta_do_llm.choices[0].message.content)