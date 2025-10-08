"""
1 - Carregar um arquivo .txt, onde cada linha será um elemento de uma lista do Python
2 - Mandá-la ao modelo que você está rodando localmente para extrair, em formato JSON, onde cada item terá
"usuário", "resenha original", "resenha_pt", "avaliação" (Positiva, Negativa ou Neutra)
3 - Transformar a resposta do modelo em uma lista de dicionários Python
4 - Criar uma função que, dada uma lista de dicionários, percorre a lista e faz 2 coias:
    4.1 - Conta a quantidade de avaliações positivas, negativas e neutras
    4.2 - Une cada item dessa lista em uma variável do tipo string com algum separador. Ao final, retorna ambas as coisas
"""
import json
from aula09_def_llm_local import receber_linha_e_retorna_json

# Etapa 1
lista_resenhas = []
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_resenhas.append(linha.strip())

# Etapa 2 e 3
lista_de_resenha_json = []
for resenha in lista_resenhas:
    resenha_json = receber_linha_e_retorna_json(resenha)
    resenha_json_limpa = resenha_json.replace("```json", "").replace("```", "")
    resenha_dict = json.loads(resenha_json_limpa) # Converter o JSON para um dicionário
    lista_de_resenha_json.append(resenha_dict)


def contador_e_juntador(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0
    lista_dicionarios_str = []

    for dicionario in lista_de_dicionarios:
        if dicionario["avaliacao"] == "Positiva":
            contador_positivas += 1
        elif dicionario["avaliacao"] == "Negativa":
            contador_negativas += 1
        else:
            contador_neutras += 1

        lista_dicionarios_str.append(str(dicionario))

    textos_unidos = "#####".join(lista_dicionarios_str)
    return contador_positivas, contador_negativas, contador_neutras, textos_unidos


pos, neg, neut, textos = contador_e_juntador(lista_de_resenha_json)
print(f"Positivas: {pos}, Negativas: {neg}, Neutras: {neut}")
print(textos)