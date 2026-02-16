
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

# BotCity: Framework do python que utiliza imagens de interfaces 
# para realizar automações em sistemas. O ponto principal dessa ferramenta é que ela gera códigos automaticamente com base na
# ação que queremos realizar e na imagem informada. 

# Import da classe desktopbot do modulo core da biblioteca botcity
# que tem como objetivo nos proporcionar os métodos que serão necessários
# para a construção da automação.
from botcity.core import DesktopBot

# Import da biblioteca pandas que tem como objetivo acessar e manipular
# planilhas.
import pandas as pd

# Class bot que irá herdar os métodos e atributos da classe DeskBot.
# A classe Bot irá conter toda a nossa automação
class Bot(DesktopBot):
    
    # Função da classe Bot que ira conter todo o trecho da automação. 
    # self: Sera a variável de referência que utilizaremos para acessar
    # os métodos que o Bot herdou do DeskTop. 
    def action(self, execution=None):
        
        # Browse: Tem como objetivo receber acessar sites através
        # de links que são passados como argumentos
        self.browse("http://web.whatsapp.com")
        
        # Importar a base de dados que contém as mensagens e contatos
        # que queremos enviar uma mensagem.
        tabela = pd.read_excel("whats/Contatos.xlsx")
        
        #print(tabela)
        
        # For que irá percorrer os indices (index) da tabela com o
        # objetivo de acessar os atributos da tabela (contato, msg
        # e arquivo) para enviar mensagens.
        for linha in tabela.index:
            
            # Ira acessar os valores de cada coluna da tabela usando
            # a função do loc do pandas que tem como objetivo localizar
            # valores usando o indice (representado pela linha) e o
            # nome da coluna que queremos acessar.
            contato = tabela.loc[linha, "Contato"]
            
            msg = tabela.loc[linha, "Msg"]
            
            arquivo = tabela.loc[linha, "Arquivo"]
            
            
             # Códigos gerados pelo framework
            # Searching for element 'lupa '
            
            # Esse trecho, irá localizar e clicar na lupa de pesquisa
            # de contatos do whatsapp.
            if not self.find("lupa", matching=0.97, waiting_time=60000):
                self.not_found("lupa")
            self.click()
            
            # Ira escrever o nome do contato com um intervalo de 100
            # milisegundos, dessa forma ele escreverá o nome com um 
            # pouco menos de velocidade.
            self.type_keys_with_interval(100, contato) 
            
            # Após escrever o nome, chamaremos o método enter que irá
            # nos transferir para o campo de mensagem do contato
            # escolhido.
            self.enter()
            
            # Ira conter os valores da coluna mensagem
            mensagem = msg
            
            # Como após o enter já estaremos dentro do campo de mensagem,
            # vamos apenas escreve-la utilizando o método paste
            self.paste(mensagem)
            
            # Vmaos chamar o enter para enviar a mensagem.
            self.enter()
            
            # Ira verificar se a coluna arquivo não possui valores
            # isna: Função do pandas que verifica se os dados de uma
            # coluna são nulos. Ele retorna um valor booleano que indica
            # se o valor nan existe ou não.
            if pd.isna(arquivo) == False:
                
                
                # Searching for element 'anexar '
                
                # Ira localizar e clicar no icone de anexar arquivos
                if not self.find("anexar", matching=0.97, waiting_time=10000):
                    self.not_found("anexar")
                self.click()
                
                # Searching for element 'documento '
                # Ira localizar e clicar no  icone de envio de 
                # documentos.
                if not self.find("documento", matching=0.97, waiting_time=10000):
                 self.not_found("documento")
                self.click()    
                
                # Searching for element 'nome '
                
                # Ira localizar o nome do campo "nome do arquivo"
                # com o objetivo de sinalizar que a página de
                # arquivos ja foi carregada.
                # Observação: Nessa etapa especificamos no botcity
                # a função await que significa "esperar o elemento"
                # que queremos selecionar na imagem.
                if not self.find("nome", matching=0.97, waiting_time=10000):
                    self.not_found("nome")
                    
                # Ira escrever o caminho do arquivo que queremos 
                # enviar para o usuário.
                self.paste(arquivo)
                
                # Após especificar o arquivo vamos dar um enter para 
                # escolher o arquivo especificado.
                self.enter()
                
                 # Searching for element 'enviar '
                 # ira clicar e enviar o arquivo para o contato.
                if not self.find("enviar", matching=0.97, waiting_time=10000):
                     self.not_found("enviar")
                self.click()
                 
                 
                
            
            
    # Função que irá especificar o rótulo que o sistema não encontrou
    # label: ira conter o rótulo que o sistema não encontrou
    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()











