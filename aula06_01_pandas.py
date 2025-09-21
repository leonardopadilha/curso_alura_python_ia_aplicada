import os
import pandas as pd
from google import genai
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv('GEMINI_API_KEY')
client = genai.Client()
MODELO = "gemini-2.0-flash"

"""
Desafio:
1 - Criar um arquivo.txt a partir de uma lista de perguntas vindas de uma lista em Python;
2 - Ler as perguntas desse arquivo.txt e salvá-las em uma lista Python;
3 - Obter respostas de um LLM para cada uma;
4 - Salvar os resultados em um novo arquivo.csv;
5 - Ler o arquivo.csv usando Pandas
"""

"""
lista_perguntas_ia = [
    "O que é aprendizado de máquina e como ele se diferencia da inteligência artificial geral?",
    "Quais são os principais tipos de algoritmos de aprendizado de máquina (supervisionado, não supervisionado, por reforço)?",
    "Explique o conceito de redes neurais e como elas funcionam.",
    "O que é um 'modelo de linguagem grande' (LLM) e quais são alguns exemplos notáveis?",
    "Qual é a diferença entre IA forte e IA fraca?",
    "Como a visão computacional é usada na prática?",
    "O que são 'viés' e 'ética' em inteligência artificial e por que são preocupações importantes?",
    "Qual o papel da IA na robótica e na automação?",
    "Diferencie o aprendizado profundo (deep learning) do aprendizado de máquina tradicional.",
    "O que é o 'teste de Turing' e qual sua relevância na IA?",
]
"""

lista_perguntas = [
    "Qual foi o nome do jardim onde Adão e Eva viveram?",
    "Quem construiu a arca para se salvar do dilúvio?",
    "Quantos dias e noites Jesus jejuou no deserto?",
    "Qual era a idade de Matusalém quando ele morreu?",
    "Quem libertou o povo de Israel do Egito?",
    "Qual apóstolo traiu Jesus por 30 moedas de prata?",
    "Em que cidade Jesus foi crucificado?",
    "Qual profeta foi engolido por um grande peixe?",
    "Quem foi o pai de João Batista?",
    "Qual era a profissão de Mateus antes de seguir Jesus?"
]

with open("perguntas.txt", "w", encoding="utf-8") as arquivo:
  for pergunta in lista_perguntas:
    arquivo.write(pergunta + "\n")


lista_desafio = []
with open("perguntas.txt", "r", encoding = "utf-8") as arquivo:
  for linha in arquivo:
    lista_desafio.append(linha.strip())
  print(lista_desafio)


lista_de_dicionarios_de_respostas = []
for pergunta in lista_desafio:
  resposta = client.models.generate_content(
    model=MODELO,
    contents=f"Gere uma resposta muito sucinta para a pergunta: {pergunta}"
  )
  lista_de_dicionarios_de_respostas.append({"pergunta": pergunta, "resposta": resposta.text})


with open("respostas1.csv", "w", encoding="utf-8") as arquivo:
  arquivo.write("pergunta, resposta\n")
  for pergunta_dict in lista_de_dicionarios_de_respostas:
    arquivo.write(f"{pergunta_dict['pergunta']}, {pergunta_dict['resposta']}\n")

# O pandas sabe separar dicionários em DataFrames.
df_perguntas_e_respostas = pd.DataFrame(lista_de_dicionarios_de_respostas)
df_perguntas_e_respostas.to_csv("resposta2.csv", index=False, encoding="utf-8")
novo_df = pd.read_csv("resposta2.csv")
novo_df.head()
