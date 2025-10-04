import pandas as pd
import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")

client = anthropic.Anthropic(
  api_key=anthropic_api_key
)

MODELO = "claude-sonnet-4-5"

"""
1. Carregar um arquivo .csv com feedback de clientes (reviews.csv), 
2. Usar um LLM para classificar o sentimento de cada feedback (positivo, negativo, neutro) 
3. Adicionar essa classificação ao DataFrame.
"""

df_reviews = pd.read_csv("reviews.csv")
coluna_reviews = df_reviews["reviewText"]

lista_analises_de_sentimentos = []
for review_numero, resenha in enumerate(coluna_reviews):
    resposta = client.messages.create(
        model=MODELO,
        max_tokens=1024,
        temperature=0,
        messages=[
            {"role": "user", 
             "content": f""" 
             Você irá analisar a resenha que eu te mandarei abaixo, retorne com uma análise de sentimento.
             Você deve responder APENAS com uma das seguintes palavras: 'Positiva', 'Negativa' ou 'Neutra',
             indicando o sentimento relativo aquela resenha específica. 
             
             Exemplos:
             'Eu adorei esse produto' -> Positiva
             'Gostei, mas não é nada de especial' -> Neutra
             'Odiei esse produto' -> Negativa

             Segue a resenha a ser analisada: {resenha}
             """ 
            }
        ]
    )
    lista_analises_de_sentimentos.append(resposta.content[0].text)

# Adicionando a coluna de sentimentos ao DataFrame / A lista deve ser do mesmo tamanho que o DataFrame
df_reviews["sentimentos"] = lista_analises_de_sentimentos 
df_reviews_atualizado = df_reviews[['reviewerID', 'reviewText', 'sentimentos']]
print(df_reviews_atualizado)