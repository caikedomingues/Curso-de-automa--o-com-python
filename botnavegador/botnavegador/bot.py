"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

"""
********************************************************************************
*                                   WARNING                                    *
********************************************************************************

You are using an outdated version of the template which is no longer recommended.
While this template works and is valid, it is strongly recommended to create a new project with the latest template version.

Please refer to our documentation: https://documentation.botcity.dev/tutorials/python-automations/desktop/
"""

# BotCity: É um framework de RPA (Robotic Process Automation) focado em
# Python. Em termos simples, ele é uma "estrutura pronta" que organiza
# e facilita a criação de robos. O BotCity age como um facilitador. Ele
# traz funções prontas que tornam o código mais limpo, como o self.browse()
# ou o self.wait(), além de integrar ferramentas de visão computacional
# para clicar botões que o selenium as vezes não alcança.

# O grande diferencial do BotCity é que ele permite criar robôs que
# "enxergam" a tela. Se você precisar automatizar um programa que não
# é um site (como um sistema antigo da empresa ou o próprio Excel),
# você pode tirar print do botão e o BotCity o encontrará usando
# reconhecimento de imagem.

# O BotCity foi feito para escalar. Além do código que você está escrevendo
# no VS Code, eles oferecem uma plataforma (o maestro) para você agendar
# quando o robô deve rodar, ver logs de erro e saber se a tarefa foi
# concluida com sucesso.

from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

# Import da classe ChromeDriverManager do módulo chrome da biblioteca
# Webdriver_manager. Vamos usar essa classe para adquirir o driver que possibilita
# que o python se comunique com o chrome. 
from webdriver_manager.chrome import ChromeDriverManager

# Classe bot que irá conter a automação realizada pelo framework BotCity.
# Como escolhemos na etapa de criação e configuração do projeto o tipo
# web, a nossa classe irá herdar os atributos e métodos da classe WebBot. 
class Bot(WebBot):
    
    # Metodo da classe bot que irá conter as açoes da nossa automação.
    # O método irá receber como argumento:
    
    # self: Variável que será a referência de acesso aos
    # métodos da classe.
    
    # execution=None: Ira conter o numero (id) tarefa que deverá ser
    # executada. Como o nosso sistema não irá rodar em um servidor,
    # vamos deixar o execution com o valor padrão (None), dessa forma
    # o BotCity envia um objeto cheio de informações para dentro do
    # execution.
    
    def action(self, execution=None):
    
        # Configure whether or not to run on headless mode
        self.headless = False
        
        # Como esse arquivo do botcity é do tipo web, precisamos
        # especificar o driver do navegador que vamos utilizar.
        # Para isso vamos instanciar a classe ChromeDriverManager
        # e chamar o método install que irá baixar ou atualizar
        # o driver do chrome e armazenar o caminho do arquivo
        # driver
        self.driver_path = ChromeDriverManager().install()


        # Função que tem como objetivo acessar sites no navegador usando
        # como argumento o link (endereço) do site que queremos acessar.
        self.browse("https://www.google.com")
        
        # Searching for element 'campo_pesquisa '(trecho gerado pelo
        # BotCity após a realização de um print): Esse trecho irá
        # clicar no campo de pesquisa do google.   
        if not self.find("campo_pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("campo_pesquisa")
        self.click()
        
        # Função do BotCity que irá escrever a pesquisa no campo do google
        self.paste('cotação do dolar')
        
        # Função do botcity que irá dar "enter" na pesquisa do Google.
        self.enter()
        
        # Searching for element 'dolaramericano'(Trecho gerado pelo
        # print do BotCity): Trecho que ira dar clicar e selecionar(click
        # relativo que possibilita que você especifique uma "área"
        # do site para clicar) no valor da cotação do dolar.
        if not self.find("dolaramericano", matching=0.97, waiting_time=10000):
            self.not_found("dolaramericano")
        self.double_click_relative(14, 75)
        
        # Função do BotCity que dá control + c no valor selecionado
        # pelo click relativo
        self.control_c()
        
        # o get_clipboard do BotCity é a função que contém os valores
        # armazenados no control_c
        cotacao = self.get_clipboard()
        
        # Ira imprimir o valor da cotação.
        print("Valor atual da cotação do dolar: ", cotacao)
        
        # Por algum motivo, o navegador não ficou aberto após eu comentar
        # os trechos self.await(1000) (que espera 10 segundos para fechar o
        # navegador) e self.stop_browser (função que fecha o navegador).
        # Para resolver isso, decidi colocar um inpút que ficara executando
        # infinitamente até o usuário encerra-lo com um enter
        input("Pressione enter para fechar o navegador")
        # Wait for 10 seconds before closing
        self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()


    # Função que será chamada caso as funções não encontre os rótulos
    # definidos nos prints
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

