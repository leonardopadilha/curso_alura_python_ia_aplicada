import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

google_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client()

MODELO = "gemini-2.0-flash"
chat = client.chats.create(model=MODELO)

mensagem = input("Pergunta: ")
resposta = chat.send_message(mensagem)
print(resposta.text)

for message in chat.get_history():
  print(f"role - {message.role}", end=": ")
  print(message.parts[0].text)

