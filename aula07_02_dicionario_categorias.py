import pandas as pd
import os
from dotenv import load_dotenv
import anthropic
import json

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

resposta_json_categoria = client.messages.create(
    model=MODELO,
    max_tokens=1024,
    temperature=0,
    messages=[
        {"role": "user", 
            "content": f"""
            Você é um analista de dados. Vou te passar muitas resenhas negativas de análises de um produto, o tipo de análise
            está na coluna 'sentimentos'. Utilizando como base a coluna 'reviewText' encontre 5 categorias diferentes para 
            os tipos de sentimentos Negativos.

            Cada categoria deve ser definida por APENAS uma palavra. Quero que elas estejam em letra minúscula e sem 
            acentos gráficos.

            Depois, quero que você retorne APENAS um texto em formato JSON, contendo três chaves:
            - 'resenha_original': Irá conter de forma resumida a resenha original.
            - 'resenha_pt': Irá conter a mesma descrição do campo 'resenha_original', porém, em português.
            - 'categoria': Irá conter a categoria dentre as 5 definidas por você em que a resenha se encaixa.

            {{'resenha_original': 'I didn't like the color of the product',
            'resenha_pt': 'Eu não gostei da cor do produto',
            'categoria': 'design'}}

            Realize essa tarefas apenas os 5 primeiros registros do DataFrame.

            Aqui estão as resenhas: {df_reviews_atualizado}
            """ 
        }
    ]
)
json_categorias_negativas = resposta_json_categoria.content[0].text
json_categorias_negativas_limpo = json_categorias_negativas.replace("```json", "").replace("```", "")
dicionario_categorias_negativas = json.loads(json_categorias_negativas_limpo) # Converter o JSON para um dicionário
print(dicionario_categorias_negativas)