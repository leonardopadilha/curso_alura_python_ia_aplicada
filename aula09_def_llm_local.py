from openai import OpenAI


client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key = 'google-gemma-3-1b'
)

def receber_linha_e_retorna_json(linha):
    resposta_do_llm = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[
            { "role": "system", "content": """Você é um especialista em análise de dados e conversão de dados para JSON.
            Você receberá uma linha de texto que é uma resenha de um aplicativo em um marktplace online.
            Eu quero que você analise essa resenha e me retorne um JSON com as seguintes chaves:
            - 'usuario': O nome do usuário que fez a resenha.
            - 'resenha_original': A resenha no idioma original que você recebeu.
            - 'resenha_pt': A resenha traduzida para o português.
            - 'avaliação': Uma avaliação se essa resenha foi 'Positiva', 'Negativa' ou 'Neutra' (apenas uma dessas opções)

            Exemplo de entrada:
            '654654654654$João da Silva$This is a positive review for the app.
            Exemplo de saída:
            {
                "usuario": "João da Silva,
                "resenha_original": "This is a positive review for the app.",
                "resenha_pt": "Este é um review positivo para o aplicativo.",
                "avaliacao": "Positiva"
            }

            Regra importante: Você deve retornar APENAS o JSON, sem nenhum outro texto adicional.
            """ },

            { "role": "user", "content": f"Resenha: {linha}" }
        ],
        temperature=0.0
    )
    #print(resposta_do_llm.choices[0].message.content)
    return resposta_do_llm.choices[0].message.content