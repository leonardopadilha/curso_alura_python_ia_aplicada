import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

client = Groq()

MODELO = "openai/gpt-oss-20b"

def gerar_resposta_groq(pergunta):
  completion = client.chat.completions.create(
      model=MODELO,
      messages=[
        {
          "role": "user",
          "content": pergunta
        }
      ],
      temperature=1, # 0 - Menos criativo possível, 2 - Mais criativo possível
      max_completion_tokens=8192,
      reasoning_effort="medium",
      stream=True,
      stop=None
  )

  for chunk in completion:
      print(chunk.choices[0].delta.content or "", end="")


if __name__ == "__main__":
  pergunta = input("Pergunta: ")
  gerar_resposta_groq(pergunta)