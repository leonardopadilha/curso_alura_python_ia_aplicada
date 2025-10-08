import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

api_key = os.getenv("OPENAI_API_KEY")

MODELO = "gpt-4o-mini"
pergunta = input("Pergunta: ")

response = client.responses.create(
    model=MODELO,
    input=pergunta,
)

print(response.output_text)