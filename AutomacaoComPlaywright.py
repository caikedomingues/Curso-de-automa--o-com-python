# Para esse exercicio, precisaremos usar o formato .py, pois o módulo
# sync é incompativel com o formato ipynb (jupyter notebook) que utiliza
# o módulo async

# Import da função sync_playwright do módulo sync_api da biblioteca playwright que tem como objetivo automatizar ações que podem ser realizadas em navegadores como firefox, chrome, Opera entre outros.
# Com essa função, podemos acessar site e manipula-los através de
# seletores (como o xpath, por exemplo) que podem identificar elementos
# de um site. 

# Observação após instalar a biblioteca via "pip install playwright" é necessário 
# utilizar o comando "playwright install" para conseguir instalar as extensões
# que possibilitam o acesso aos navegadores do computador.
from playwright.sync_api import sync_playwright

# Biblioteca que tem como objetivo manipular o tempo
import time

# Esse trecho serve para garantir que o sistema consiga fechar o
# navegador após a execução completa da automação.Também usamos
# essa lógica em CRUDS com banco de dados, onde iniciamos a conexão
# e encerramos conexões com o objetivo de não tornar o banco vulnerável.
# Aqui a lógica é mais ou menos parecida, já que a abertura de varias
# páginas pode tornar o sistema mais lento e pesado
with sync_playwright() as p:
    
    # Chamada da função sync_playwright:
    # p: Objeto da retornado pela função que nos permite controlar
    # os navegadores que iremos manipular.
    # chromium: Atributo do objeto p que possibilita o acesso ao navegador
    # launch: Função do atributo chromium que tem como objetivo abrir o 
    # navegador. Ele recebe como argumento o headless que define se o navegador deve ou não aparecer na tela através de valores booleanos.
    # Observação: Por padrão o headless possui valor True, ou seja,
    # ele abre o navegador sem mostra-lo na tela.
    navegador = p.chromium.launch(headless=False)
    
    # Tem como objetivo criar uma nova página no navegador que vamos armazenar na variável "pagina".
    pagina = navegador.new_page()
    
    # Função do objeto que tem como objetivo acessar um site dentro do navegador, para isso, devemos fornecer como argumento da função o link
    # do site que queremos acessar.
    pagina.goto("https://www.hashtagtreinamentos.com/?origemurl=75502579145&base-brand&gad_source=1&gad_campaignid=2057505825&gbraid=0AAAAADLlh8-judlWkuq6krE0f16W1pDi_&gclid=Cj0KCQiAprLLBhCMARIsAEDhdPemCl_52f4c-Bb7VVcyhl-3E3--z9fdYdPoXT6HXlbU81ZHY27xz-caAuytEALw_wcB")
    
    # locator: Método do objeto pagina que tem como objetivo acessar elementos do site especificado. A
    # função irá receber como argumento o xpath do elemento que queremos acessar. Observação: O locator
    # pode receber outros tipos de seletores
    # click: Tem como objetivo clicar no elemento especificado.
    pagina.locator('xpath =/html/body/header/div/div[2]/a[1]' ).click()
    
    # Método do objeto página que tem como objetivo escrever textos nos elementos
    # especificados (geralmente formulários). A função recebe como argumento
    # o xpath do elemento e o texto que deve ser escrito no elemento.
    pagina.fill('xpath=//*[@id="email-login"]', "email@gmail.com")
    
     # locator: Método do objeto pagina que tem como objetivo acessar elementos do site especificado. A
    # função irá receber como argumento o xpath do elemento que queremos acessar. Observação: O locator
    # pode receber outros tipos de seletores
    # click: Tem como objetivo clicar no elemento especificado.
    pagina.locator('xpath=//*[@id="login-grupo-conteudos"]/div/div/div[2]/div/button').click()
    
    # Ira dar um intervalo de 5 segundos antes de fechar o navegador.
    time.sleep(5)
    
    
    