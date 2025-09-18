import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

google_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client()

MODELO = "gemini-2.0-flash"
chat = client.chats.create(model=MODELO)

prompt = input("Digite sua pergunta: ")
while prompt.lower() != "fim":
  resposta = chat.send_message(prompt)
  print(resposta.text)
  
  prompt = input("\nDigite sua pergunta: ")