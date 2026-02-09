
# É importante utilizar o comando "playwright install" para garantir que ele instale ou atualize as extensões que o possibilita a acessar os navegadores

# Observação: vale lembrar que o formato ipynb (notebook jupyter) não
# possibilita a utilização de comandos que contém o trecho sync_api

# playwright: Biblioteca para automação de navegadores (Web Scraping e RPA).
# Ele foi criado pela Microsoft para permitir que você controle o Chrome,
# Firegox e Safari de forma programática, como se você fosse um usuário
# real sentado na frente do computador. Caracteristicas do playwright:

# 1. Multi-Navegador e Multi-Plataforma: Com um único código, você pode
# rodar sua automação nos principais motores de busca:

# Chromium (Chrome, Edge, Brave), Firefox, WebKit(Safari).

# 2. Auto-Waiting (Espera Automática): Essa é a função que resolveu muitos 
# problemas que as bibliotecas antigas (como o Selenium) tinham. O playwright
# espera automaticamente que os elementos da página estejam:
# visiveis (não escondidos)
# Estáveis (não mexendo na tela)
# Habilitados (clicáveis).

# Isso evita que seu código dê erro por que tentou clicar em um botão antes
# da página terminar de carregar totalmente.

# 3. Ferramentas de "Super-Poderes": O Playwright não apenas uma biblioteca
# de código, ele vem com ferramentas auxiliares importantes para o desenvolvimento:

# codegen (Gerador de Código): Você abre o navegador, clica nos botões 
# manualmente e ele escreve o código Python para você em tempo real.

# Modo Headless (Sem Cabeça): Você pode rodar o robô vendo a janela
# abrir (headless=False) ou de forma invisivel no servidor (headless=True)
# para ganhar velocidade.

# Import da função sync_playwright do modulo sync_api da biblioteca
# playwright que tem como objetivo gerenciar o contexto que inicia
# encerra a execução do navegador de forma segura. O termo sync_api
# indica que estamos usando a versão sincrona da bilioteca. Isso 
# significa que o Python vai executar uma linha de cada vez e esperar
# que cada comando do navegador (como abrir uma página ou clicar) termine
# antes de ir para a próxima. É o ideal para scripts de automação simples. 
from playwright.sync_api import sync_playwright

# Import da biblioteca time que serve para manipular o tempo de execução
# do problema.
import time

# Usando o with, garantimos que o python inicie e encerre o navegador
# automaticamente. Dessa forma conseguiremos criar uma automação com 
# inicio e fim, ou seja, não correremos o risco de executar passos
# adicionais no sistema.
with sync_playwright() as pw:
    
    # Chromium: Classe que será instanciada com o objetivo de possibilitar
    # o acesso do python ao navegador Chrome.
    
    # launch: método da classe chromium que irá definir se o navegador deve ou não aparecer na tela. Ira receber como argumento o valor headless (sem cabeça) = False, ou seja, ela fara o navegador aparecer na tela.
    navegador = pw.chromium.launch(headless=False)
    
    # O contexto tem como objetivo gerenciar mais de uma página criada pelo
    # chromium. Com o contexto também poderemos trabalhar a comunicação entre
    # 2 páginas diferentes.
    contexto = navegador.new_context()
    
    # metodo do chromium que irá criar uma nova página
    pagina = contexto.new_page()
    
    # Método da classe chromium que tem como objetivo acessar sites nos navegadores 
    pagina.goto("https://www.hashtagtreinamentos.com/?origemurl=75502579145&base-brand")
    
    # Metodo da classe chromium que irá acessar o titulo da página que está sendo acessada. Acredito que o método pegue o conteúdo da tag title do site acessado.
    print(pagina.title())
    
    #Maneira não recomendada de fazer a busca de elementos (usando o xpath): pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()
    
    # Maneira Correta de acessar os elementos da página: Devemos acessar a ferramenta codegen através do comando "playwright codegen link do
    # site que você esta tentando acessar". Dessa forma, ele irá abrir
    # a ferramenta e retornará o codigo python que seleciona o elemento
    # que queremos manipular.
    
    # get_by_role: Função gerada pelo codegen que seleciona o botão
    # de "quero aprender" da página. O atributp first do chromium
    # indica que o seletor deve acessar o primeiro elemento que
    # contém o name indicado na função get_by_role. Dessa forma,
    # evitaremos que o python se confunda caso o site tenha 2 names
    # iguais ou parecidos
    botao = pagina.get_by_role("link", name="Quero aprender").first  
    
    # locator: Método da classe chromium que tem como objetivo localizar
    # elementos de um site. A função recebe como argumento o nome do
    # elemento que você quer acessar.
    # All: Metodo do chromium que ira selecionar todos os elementos que
    # foram especificados no locator, ou seja, todas as tag divs no
    # nosso caso.
    divisorias = pagina.locator("div").all()
    
    print(divisorias)
    
    # Ira imprimir a quantidade de divs presentes na página.
    print("Quantidade de divisorias: ", len(divisorias))
    
    # with: ira garantir a comunicação entre as 2 páginas
    # expect_page: O 'expect_page' prepara o código para capturar uma  nova aba que será aberta após o clique no botão, permitindo 
    # controlar ambas simultaneamente.
    with contexto.expect_page() as pagina2_info:
        
        # clique que será realizado na primeira página
        botao.click()  
    
    # Ira receber as informações do contexto apelidado de pagina2_info
    pagina2 = pagina2_info.value
    
    # Após o click feito na página 1, vamos redirecionar o usuário
    # para a pagina de curso de python do site.
    pagina2.goto("https://www.hashtagtreinamentos.com/curso-python")
    
    # Após acessar a página, vamos usar o codegen para selecionar
    # os campos do formuário.
    # O método fill da classe chromium tem como objetivo escrever textos
    # nos elementos de um site usando uma string como argumento
    pagina2.get_by_role("textbox", name="Seu primeiro nome").fill("Caio")
    
    pagina2.get_by_role("textbox", name="Seu melhor e-mail").fill("email@gmail.com")
    
    pagina2.get_by_role("textbox", name="Seu WhatsApp com DDD").fill("11999999999")
    
    # Vamos usar o codegen para acessar o botão de envio de informações
    # do formulário. O método click da classe chromium tem como objetivo
    # clicar nos elementos do site.
    pagina2.get_by_role("button", name="Quero acessar as informações").click()
    
    # Ira dar um intervalo de 15 segundos antes de fechar o navegador.
    time.sleep(15)
    
    # Ira fechar o navegador.
    navegador.close()