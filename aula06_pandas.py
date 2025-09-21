import os
from dotenv import load_dotenv
import anthropic
import pandas as pd
#df = pd.read_csv("medias.csv")
#print(df)

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
  api_key=anthropic_api_key
)

MODELO = "claude-opus-4-1-20250805"

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

lista_perguntas_biblicas = [
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

def criar_arquivo_perguntas(nome_arquivo,lista_perguntas):
  with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    for pergunta in lista_perguntas:
      arquivo.write(pergunta + "\n")
  print(f"Arquivo {nome_arquivo} criado com sucesso!")

def responder_perguntas(nome_arquivo):
  lista_respostas = []

  with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.readlines()

    for pergunta in conteudo:
      resposta = client.messages.create(
        model=MODELO,
        max_tokens=1024,
        temperature=0,
        messages=[
          {"role": "user", "content": f"""
          Responda de maneira bem resumida a seguinte {pergunta}.

          # Formato da Saída
          Qual foi o nome do jardim onde Adão e Eva viveram,Eden
          """}
        ]
      )
      lista_respostas.append(resposta.content[0].text)
    return lista_respostas



if __name__ == "__main__":
  criar_arquivo_perguntas("perguntas.txt", lista_perguntas_biblicas)
  respostas = responder_perguntas("perguntas.txt")

  criar_arquivo_perguntas("respostas.csv", respostas)
  df = pd.read_csv("respostas.csv")
  print(df)