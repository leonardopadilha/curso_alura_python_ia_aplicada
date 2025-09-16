import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

google_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client()

MODELO = "gemini-2.0-flash"

def generate(modelo, pergunta):
  resposta = client.models.generate_content(
    model=modelo,
    contents=pergunta
  )
  return resposta.text


if __name__ == "__main__":
  pergunta = input("Pergunta: ")
  print(generate(MODELO, pergunta))