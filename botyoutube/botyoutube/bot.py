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

# BotCity: É uma plataforma RPA (Robotic Process Automation) de
# "próxima geração". Ela foi construida para permitir a automatização
# de qualquer coisa no computador - seja um site, um software antigo
# de contabilidade, o SAP, o Excel ou até mesmo o Teams. Pilares que
# definem a BotCity:

# 1. Framework Baseado em Código (Python/Java): Diferente de outras
# ferramentas de RPA que usam "arrastar e soltar", a BotCity é focada
# em desenvolvedores. Você escreve o código Python real. Isso dá total
# liberdade para usar bibliotecas como pandas, OpneCv ou até ChatterBot
# dentro do seu robô.

# 2. Visão Computacional (o "olho" do robô): O grande diferencial da
# BotCity (especialmente o DesktopBot) é que ela não depende apenas
# do código interno do programa (HTML ou IDs). Ela usa Visão Computacional.
    # * Você tira um "print" de um botão.
    
    # * O robô processa a imagem.
    
    # * Ele move o rato e clica exatamente naqueles pixels. Isso resolve
    # o problema de programas que não tem IDs ou XPaths faceis de encontrar.

# 3. O Ecossistema BotCity: A Botcity não é apenas uma biblioteca; é 
# um conjunto de ferramentas:

    # -> BotCity Studio (que vamos utilizar nesse exercicio): Uma ferramenta visual que te ajuda a capturar imagens da tela e gera
    # o código Python automaticamente para você. É onde você "ensina"
    # o robô onde clicar.
    
    # -> BotCity Framework (core/web): As bibliotecas que instalamos
    # via pip para dar comandos ao robô.
    
    # -> BotCity Maestro: É o "Centro de Comando" (Orquestrador) na
    # nuvem. Lá você agenda quando os robõs devem rodar, vê os logs 
    # de erro e controla quantas tarefas cada robô executou.  


# Import da classe DeskBot que possui funções que possibilitam criar
# automações de tarefas como preencher formulários e enviar mensagens
# (pelo teams por exemplo).
from botcity.core import DesktopBot


# Classe que ira conter todas as ações que queremos automatizar.
# Ela ira herdar as funções da classe DesktopBot com o objetivo de
# realizar as automações.
class Bot(DesktopBot):
    
    # Função da classe Bot que irá conter todas as ações do sistema
    # de automação.
    # Self: Variável que iremos usar como referência para acessar as
    # funções da classe DesktopBot.
    # execution = None: Na BotCity, o argumento execution é um objeto que contém informações sobre a tarefa vinda do Maestro (como o ID da tarefa).
    def action(self, execution=None):

        # Opens the BotCity website.
        #self.browse("https://www.youtube.com/watch?v=Y6V_uTGwWqE&list=PLpdAy0tYrnKyjrY1Fr72DhmrRmeWI_5C8&index=4")
        
        # Função que tem como objetivo executar os programas instalados no computador
        # (o teams no nosso caso). A função deve receber como argumento o caminho
        # do aplicativo que queremos solicitar.
        self.execute(r"C:\Users\caike\Desktop\Microsoft Teams.lnk") 
        
        # Searching for element 'mensagem ': 
        # if: Ira verificar o resultado da função find.
        # find: Função que irá procurar o elemento nomeado como
        # "mensagem".
        # click: Ira fazer o robo clicar no elemento encontrado.
        if not self.find("mensagem", matching=0.97, waiting_time=10000):
            self.not_found("mensagem")
        self.click()
        
        # Função que ira conter mensagem que devera ser passada para
        # o campo de mensagem
        self.paste("Ola Caike, tudo bem?")
        
        # Searching for element 'EnviarMensagem'
        # if not: Ira verificar o resultado da função find
        # self.find: Função que tem como objetivo procurar o elemento nomeado
        # como "EnviarMensagem" 
        # self.click: Função que tem como objetivo clicar no elemento encontrado para
        # enviar a mensagem.
        if not self.find("EnviarMensagem", matching=0.97, waiting_time=10000):
            self.not_found("EnviarMensagem")
        
        self.click()        
    
    # Essa função será a Handler de Erro (tratador de erros): 
    # O que ela faz: Ela não é chamada automaticamente pelo
    # sistema, mas sim por nós dentro da função action (quando
    # o find não encontra o elemento solicitado).
    
    # Conceito: Quando o robô procura uma imagem e não a encontra,
    # ele precisa de uma forma de nos avisar o que deu errado.
    
    # label: é o rótulo da que nós demos para a imagem. Assim no terminal,
    # em vez de aparecer um erro genérico, aparacerá "Element not found
    # mensagem".
    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()








