
# Objetivo da Aula: Acessar o site da sci-hub, baixar os pdfs da lista
# no arquivo csv através do doi de cada arquivo e registrar o log de sucesso
# ou erro em um arquivo de texto.

# Biblioteca de automação que tem como objetivo controlar o mouse e os
# teclados do seu computador. Vamos utilizar essa biblioteca. 
import pyautogui as pa

# Biblioteca nativa do python que tem como objetivo manipular o tempo
# no python. Vamos utilzar essa biblioteca para criar intervalos entre
# os processos, pois, o python é bem mais rápido que o computador, logo,
# para evitar erros de elementos não encontrados, devemos criar pequenos
# intervalos que possibilitam que o computador tenha o tempo necessário
# para carregar toda a página. 
import time

# Biblioteca de analise de dados que tem como objetivo acessar e
# manipular datasets. Vamos usar essa biblioteca para acessar os
# valores presentes no arquivo csv. 
import pandas as pd

# Biblioteca que tem como objetivo permitir que o python acesse
# e manipule os arquivos do sistema operacional. Vamos utilizar essa
# função para transferir os arquivos baixados para a pasta papers.
import os

# A biblioteca glob serve para buscar e listar caminhos de arquivos ou
# pasta no seu computador que sigam um determinado padrão. Pense nela
# como o sistema de busca do nosso windows Explorer, mas feito puramente
# em código.
import glob

# função da biblioteca pandas que tem como objetivo acessar os valores de
# um dataset. A função recebe como argumento o caminho do arquivo que será
# carregado na memória do computador. A função tem como retorno um objeto
# dataframe que possui todos os valores do dataset e os métodos necessários para a manipulação dos dados.

# Observação: o r indica para o python que ele deve apenas ler o arquivo
# passado. É necessário usar esse r para dizer ao python que as contras
# barras (\) não são comandos e sim separadores de pastas no caminho
#  do arquivo.
arquivo = pd.read_excel(r"C:\Users\caike\Documents\Curso-de-automa--o-com-python\Economizando 15 horas de trabalho\papers_id.xlsx")

# Ira printar os valores do arquivo
print(arquivo)

# Método do objeto DataFrame que retorna as principais informações
# dos dados do dataset
arquivo.info()

# Ira conter apenas os valores da coluna DOI que identifica cada arquivo
# pdf no sci-hub.
lista_doi = arquivo["DOI"]

# Atributo da biblioteca pyautogui que defini um valor para a pausa 
# do script.
pa.PAUSE = 0.5

# Função que irá abrir o menu de aplicativos do windows, digitar o
# chrome na barra de busca, abrir o chrome e escolher uma conta.
def abrir_navegador():
    
    # apertar o win
    # digitar microsoft edge
    # apertar enter
    
    # Ira pressionar o botão windows que contém os aplicativos baixados
    # no nosso computador.
    pa.press("win")
    
    # Irá escrever o "chrome" na barra de busca de aplicativos do windows
    pa.write("chrome")
    
    # Ira pressionar o enter na barra de busca
    pa.press("enter")
    
    # Ira dar um intervalo de 3 segundos antes de continaur o script.
    time.sleep(3)
    
    # Ira clicar na conta escolhida de acordo com as coordenadas.
    pa.click(x=1312, y=471)
    
    # Ira dar um enter na conta escolhida
    pa.press("enter")
    
    # Ira dar um intervalo de 3 segundos antes de iniciar a execução da
    # próxima função.
    time.sleep(3)  

# Função que irá acessar a barra de busca do navegador, digitar
# o endereço do sci-hub e pressionar o enter
def abrir_scihub():

    # Função que tem como objetivo criar e acessar atalhos.
    # Vamos acessar o atalho ctrl + l que acessa a barra de
    # busca do navegador.
    pa.hotkey("ctrl", "l")
    
    # Ira escrever o endereço do site no navegador.
    pa.write("https://www.sci-hub.in/")
    
    # Ira pressionar o enter 
    pa.press("enter")
    
    # Ira dar um intervalo de 4 segundos antes de executar a próxima função.
    time.sleep(4)

# Função que ira pesquisar os numeros dos doi na barra de busca do scihub. A função ira receber
# como argumento o valor do doi que deve ser pesquisado.
def pesquisar_doi(doi):
    
    # Ira escrever o doi na barra de pesquisa
    pa.write(doi)
    
    # Ira pressionar o enter na pesquisa
    pa.press("enter")
    
    # Ira dar um intervalo de 10 segundos antes de executar a próxima função.
    time.sleep(10)

# Função que irá realizar o download de cada arquivo encontrado no site da sci-hub
def fazer_download():

    # Clicar no botão download
    # dar enter (confirmar o download)
    # esperar alguns segundos
    # apertar esc para fechar a janela de download do chrome.
    
    # Ira pressionar o esc que irá remover a janela de tradução de idiomas do google.
    pa.press("esc")
    
    # Ira clicar no botão de download do arquivo 
    pa.click(x=1825, y=157)
    
    # Ira dar um intervalo de 2 segundos para garantir que a tela de donwload apareça
    time.sleep(2)
    
    # Irá pressionar enter para o sistema baixar o arquivo pdf encontrado.
    pa.press("enter")
    
    # Ira dar um esc que irá fechar a janela que mostras os downloads realizados.
    pa.press("esc")
    
    # Ira dar um intervalo de 5 segundos antes de iniciar a transferência dos arquivos
    # baixados para a página de destino.
    time.sleep(5)
    
    # Ira listar os arquivos presentes na pasta de download
    lista_arquivos = os.listdir("C:/Users/caike/Downloads")
    
    # For que ira percorrer a lista de arquivos presentes na pasta de downloads
    for arquivo in lista_arquivos:
        
        # Ira verificar se há extensão é um pdf (ira verificar se no nome do arquivo tem a palavra "pdf")
        if "pdf" in arquivo:
            # Se essa condição for verdadeira, vamos usar a função rename da biblioteca os que tem como objetivo renomear e transferir arquivos
            # de um local para o outro. A função recebe como argumento o caminho atual do arquivo e o caminho de destino do arquivo.
            # Observação: Caso, vc queira apenas transferir o arquivo (sem renomea-lo), você deve manter o nome original no caminho de destino. 
             os.rename(f"C:/Users/caike/Downloads/{arquivo}", f"C:/Users/caike/Documents/Curso-de-automa--o-com-python/Economizando 15 horas de trabalho/papers/{arquivo}")
    
    # Ira dar um intervalo de 3 segundos antes de iniciar a execução da próxima função.
    time.sleep(3)
  
# Ira pegar a data de inclusão do ultimo arquivo. Vamos utilizar esse valor para verificar
# se novos downloads foram realizados. A função irá receber como argumento a pasta que os
# downloads ficarão armazenados.
def pegar_ultimo_arquivo(pasta):

    # Esse trecho ira listar todos os arquivos e subspastas do diretório
    # especificado.
    
    # path: módulo da biblioteca os que contém as funções join e getctime.
    
    # join: Função que tem como objetivo concatenar strings. Basicamente
    # ele vai juntar o caminho da pasta com o "*" que no glob significa
    # que a função deve retornar todos os arquivos encontrados na pasta
    lista_arquivos = glob.glob(os.path.join(pasta, "*"))
    
    # Ira pegar a data do arquivo mais recente.
    # max: Função nativa do python que retorna o maior valor de um conjunto de valores.
    
    # lista_arquivos: Ira conter os arquivos e diretórios da pasta
    # especificada
    
    # getctime: Contém a data e a hora da criação dos arquivos do
    # diretório especificado.
    ultimo_arquivo = max(lista_arquivos, key=os.path.getctime)
    
    # Ira retornar o ultimo arquivo incluido na pasta papers.
    return ultimo_arquivo

# Função que irá verificar se os downloads foram realizados com sucesso.
# A função recebe como argumento o caminho da pasta especificada e a
# quantidade de arquivos ja foram baixados
def verificar_download(pasta, quantidade_antiga_arquivos):
    
    # Ira pegar a quantidade atual de arquivos na lista de arquivos
    # e diretórios da pasta especificada.
    quantidade_nova_arquivos = len(os.listdir(pasta))
    
    # Ira conter o nome do arquivo mais recente da pasta especificada 
    nome_ultimo_arquivo = pegar_ultimo_arquivo(pasta)
    
    # Irá verificar se a quantidade atual de arquivos é maior que a quantidade de arquivos antigos.
    if quantidade_nova_arquivos > quantidade_antiga_arquivos:
        
        # Se essa condição for verdadeira, vamos atribuir a variável erro
        # o valor False que irá representar que o download não deu erro
        erro = False
    
    else:
        
        # Caso contrário, vamos atribuir a variável erro o valor true,
        # que irá representar que o download não foi concluido 
        erro = True
    
    # Retorno dos resultados (valor do erro e o nome do ultimo arquivo
    # incluido).
    return erro, nome_ultimo_arquivo

# Função que irá registrar o status do erro, o nome do ultimo arquivo
# e o doi de identificação do PDF.
def registrar_log(erro, nome_ultimo_arquivo, doi):

    # Ira verificar se o retorno do erro no método anterior é igual
    # a True
    if erro:
        
        # Se essa condição for verdadeira, vamos registrar o doi
        # do pdf e o erro gerado.
        mensagem = f"{doi}: erro\n"
        
    else:
        
        # Caso contrário, vamos registrar o doi, a mensagem de sucesso
        # e o nome do arquivo que foi baixado.
        mensagem = f"{doi}: Sucesso - arquivo: {nome_ultimo_arquivo}\n"
    
    # Ira imprimir no terminal as mensagens (de erro e de sucesso) 
    print(mensagem)
    
    # Função que tem como objetivo abrir e editar arquivos. A função
    # recebe como argumento o caminho do arquivo que será editado
    # e o comando da edição.
    
    #C:/Users/caike\Documents/Curso-de-automa--o-com-python/Economizando 15 horas de trabalho/logs.txt: Caminho do arquivo logs.txt que irá
    # conter os logs (registro dos downloads)
    
    # a: Comando append do python que irá inserir valores no arquivo
    # logs.txt. 
    with open("C:/Users/caike\Documents/Curso-de-automa--o-com-python/Economizando 15 horas de trabalho/logs.txt", "a") as log_texto:
        
        # Função que tem como objetivo escrever textos em arquivos.
        # A função ira receber como argumento 
        log_texto.write(mensagem)
    
# Abrir o navegador
abrir_navegador()

# para cada navegador: abrir o scihub, pesquisar o download, verificar se
# o download deu certo, registra no log.

# Caminho da pasta que irá conter os downloads
pasta = "C:/Users/caike/Documents/Curso-de-automa--o-com-python/Economizando 15 horas de trabalho/papers"

# For que irá percorrer a lista de doi do arquivo csv.
for doi in lista_doi:
    
    # Ira pegar a quantidade de arquivos da pasta papers 
    quantidade_antiga_arquivos = len(os.listdir(pasta))
    
    # Chamada das funções
    abrir_scihub()
    
    pesquisar_doi(doi)
    
    fazer_download()
    
    erro, nome_ultimo_arquivo = verificar_download(pasta, quantidade_antiga_arquivos)
    
    registrar_log(erro, nome_ultimo_arquivo, doi)
    

 



