import os
from time import sleep
from google import genai
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv('GEMINI_API_KEY')

client = genai.Client()

MODELO = "gemini-2.0-flash"

def resumir_email(emails):
  lista_de_resumos = []
  for numero, email in enumerate(emails):
    resposta = client.models.generate_content(
      model=MODELO,
      contents=f"Resuma em apenas uma linha o email: {email}"
    )
    lista_de_resumos.append(f"{numero + 1} - {resposta.text}")
    sleep(3)
    #print(resposta.text)
  return lista_de_resumos


def salvar_resumos(resumos):
  # é possível criar também com "a" ao invés de "w", porém, o "w" sobrescreve o arquivo, já o "a" acrescenta.
  with open("resumos.txt", "w", encoding="utf-8") as arquivo:
    for resumo in resumos:
      arquivo.write(resumo + "\n")
  print("Resumos salvos com sucesso!")


def ler_resumos():
  with open("resumos.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo resumos.txt:")
    print(conteudo)


emails = [
    "Olá João,\n\nGostaria de convidá-lo para a confraternização de fim de ano da empresa, que acontecerá no dia 20 de dezembro às 19h. Contamos com a sua presença!\n\nAtenciosamente,\nEquipe de RH",

    "Prezada Maria,\n\nConfirmo a reunião de alinhamento para amanhã às 10h via Google Meet. Caso precise reagendar, por favor, me avise.\n\nAbraços,\nCarlos",

    "Olá Sr. Paulo,\n\nVerificamos que a fatura do mês de agosto ainda não foi quitada. Solicitamos, por gentileza, que regularize o pagamento até o dia 15.\n\nAtenciosamente,\nEquipe Financeira",

    "Olá Ana,\n\nMuito obrigado pela sua colaboração no projeto! Sua dedicação foi essencial para atingirmos os resultados.\n\nCom gratidão,\nEquipe de Projetos",

    "Prezado Sr. Roberto,\n\nEste é um lembrete da sua consulta médica marcada para dia 22/09 às 14h.\n\nClínica Saúde e Vida",

    "Olá,\n\nEstamos lançando nosso novo smartphone com câmera de 108MP e bateria de longa duração. Aproveite o desconto especial de lançamento!\n\nEquipe TechStore",

    "Olá Fernanda,\n\nSua inscrição no curso de Python foi confirmada com sucesso! As aulas começam no dia 05 de outubro.\n\nEquipe Cursos Online",

    "Prezados,\n\nGostaria de informar que estarei me desligando da empresa a partir do próximo mês. Agradeço a todos pelo apoio durante esses anos.\n\nAbraços,\nLucas",

    "Olá Beatriz,\n\nSeu desempenho no último trimestre foi excelente. Continue com esse ótimo trabalho!\n\nAtenciosamente,\nGestão de Pessoas",

    "Olá cliente,\n\nAproveite nossa promoção relâmpago! Descontos de até 50% em toda a loja até domingo.\n\nEquipe MegaStore",

    "Feliz aniversário, Mariana!\n\nDesejamos muita saúde, paz e sucesso neste novo ciclo.\n\nCom carinho,\nEquipe Amiga",

    "Olá Eduardo,\n\nA reunião marcada para amanhã foi cancelada. Em breve entraremos em contato para reagendar.\n\nAtenciosamente,\nSecretaria",

    "Olá,\n\nSeu pedido será entregue amanhã, dia 16/09, entre 14h e 18h. Acompanhe em tempo real pelo nosso aplicativo.\n\nEquipe Entregas Express",

    "Prezado cliente,\n\nPara concluir seu cadastro, precisamos que nos envie os documentos solicitados até o dia 20.\n\nAtenciosamente,\nEquipe de Cadastro",

    "Olá,\n\nVocê está convidado para a palestra 'Inovação e Tecnologia', que acontecerá no auditório central no dia 25/09 às 19h.\n\nAtenciosamente,\nComissão Organizadora",

    "Parabéns, João!\n\nVocê foi promovido ao cargo de coordenador. Desejamos muito sucesso nessa nova etapa.\n\nEquipe Diretiva",

    "Olá leitor,\n\nNa edição deste mês, trazemos novidades sobre o mercado financeiro e dicas de investimentos.\n\nEquipe Finance News",

    "Prezados pais,\n\nLembramos que a reunião de pais e mestres será no dia 30/09 às 18h.\n\nAtenciosamente,\nDireção Escolar",

    "Olá,\n\nSua reserva no Hotel Paraíso foi confirmada. Check-in em 10/10 às 14h.\n\nEquipe de Reservas",

    "Bem-vindo, Pedro!\n\nEstamos felizes por tê-lo como novo cliente. Aproveite nossos serviços e conte sempre conosco.\n\nAtenciosamente,\nEquipe Suporte"
]


if __name__ == "__main__":
  resumo = resumir_email(emails)
  salvar_resumos(resumo)
  ler_resumos()

