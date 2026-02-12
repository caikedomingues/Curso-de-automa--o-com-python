
                                       # Passo a passo da aula

# -> pegar a informação que queremos (valor do dolar)

# -> Enviar um aviso via email caso o valor do dolar abaixe.

# -> Deploy: colocar o sistema no ar usando o heroku.

# Observação: Como pretendemos subir esse sistema no heroku, precisamos
# utilizar o formato .py, pois o heroku necessita de um arquivo executavel
# e que não dependa de uma pessoa executando linha por linha (célula por
# célula no caso do notebook jupyter). Outro ponto que torna o notebbok
# incompativel é a presença de codigos que constroem a interface do
# jupyter notebook.

# Import da biblioteca request que tem como objetivo enviar requisições
# a servidores de sites e APIS.
import requests

# Biblioteca que tem como objetivo conectar o python ao nosso sistema de
# arquivos.
import os

# Função da biblioteca dotenv que tem como objetivo carregar as
# variáveis de ambientes no nosso código.
from dotenv import load_dotenv

# Ira carregar as variáveis de ambientes que contém a senha da nossa
# api, a senha de app do nosso email e o endereço do email que enviara
# as mensagens.
load_dotenv()

# A função getenv da biblioteca os que tem como
# objetivo acessar as variáveis de ambientes 
# carregadas no código.
CHAVE_API = os.getenv('CHAVE_API')

EMAIL = os.getenv('EMAIL')

SENHA = os.getenv('SENHA')

# Link que realiza a requisição a API que retornara a cotação atual do dolar. O link da API deve conter
# a cotação atual e a chave de acesso a api (chave da api). A função get do request é responsável
# por se comunicar com o servidor da API.
requisicao = requests.get(f"https://economia.awesomeapi.com.br/json/last/USD-BRL?token={CHAVE_API}")

# Quando utilizamos o print em uma requisição, a função retorna para a gente o status
# atual do servidor. Se for 200, significa que o seu link de acesso esta correto e o
# servidor esta pronto para receber requisições
print(requisicao)

# podemos verificar também as informações retornadas pela requisição usando dentro
# do print a função json do request que retorna um dicionario com as informações
# retornadas pela requisição. Nesse caso em especifico, ele retornara um dicionário
# que contém outro dicionário com valores. Eu acredito que cada moeda tenha um
# dicionário com valores especificos em cada chave (que provavelmente são padrões
# para todas as moedas/cotações). 
print(requisicao.json())

# Variável que ira conter o valor da chave 'bid' que contém o valor atual 
# da cotação do dolar. Como os dados estão em formato de texto, vamos converte-lo
# para float que é o ideal para lidar com valores financeiros.
cotacao = float(requisicao.json()["USDBRL"]["bid"])

# Ira imprimir a atual cotação
print(cotacao)

# Biblioteca que tem como objetivo se conectar com o servidor de emails e
# enviar mensagens.
import smtplib

# Módulo da biblioteca email que tem como objetivo lidar com a estrutura e
# organização das mensagens
import email.message

# Função que irá enviar emails. A função ira receber como argumento o valor
# armazenado na variável cotação apos a realização de uma requisição.
def enviar_email(cotacao):
    
    # Ira conter a mensagem do email
    corpo_email = f"<p>O dolar está abaixo de 5,30. Cotação atual:{cotacao}</p>"
    
    # Instancia da classe Message do módulo message que ira cuidar da estrutura
    # da mensagem. 
    msg = email.message.Message()
    
    # Ira definir o assunto
    msg['Subject'] = "Dolar abaixo de 5,30"
    
    # Ira definir o remetente
    msg['From'] = f"{EMAIL}"
    
    # Ira definir o destinatário
    msg['To'] = f"{EMAIL}"
    
    # Ira conter a senha de app do email que enviara os dados
    password = f"{SENHA}"  
    
    # ira definir o cabeçalho do email em HTML 
    msg.add_header('Content-Type', 'text/html')
    
    # Ira na mensagem o corpo do email
    msg.set_payload(corpo_email)
    
    # Ira acessar o servidor de email do gmail que envia mensagens, ou seja, ele estabelece uma conexão com o protocolo de saida de e-mails,
    # dessa forma ele abre a comunicação com o servidor do Google.
    s = smtplib.SMTP('smtp.gmail.com: 587')
    
    # Cria um canal de tls, que é um canal seguro para envio de dados
    # sensiveis como a senha de login do email
    s.starttls()
    
    # Ira realizar o login no email que enviará as mensagens. A função
    # ira receber como argumento o endereço e a senha do email.
    s.login(msg['From'], password)
    
    # Ira enviar as mensagens codificando o conteudo em formato de 
    # string no padrão utf-8. A função recebe como argumento o
    # email to remetente e o email do destinatário. 
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    print("Email enviado com sucesso!")



if cotacao < 5.30:
    
    # Se a cotação do dolar for menor que 5.30, vamos chamar
    # a função de envio de email com o valor da cotação sendo
    # passado como argumento.
    enviar_email(cotacao)
    
    

    
    