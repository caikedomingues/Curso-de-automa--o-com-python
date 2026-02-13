
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
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

import pandas as pd

class Bot(DesktopBot):
    def action(self, execution=None):
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        self.browse("http://web.whatsapp.com")
        
        # Importar a base de dados
        tabela = pd.read_excel("whats/Contatos.xlsx")
        
        #print(tabela)
        
        for linha in tabela.index:
            
            contato = tabela.loc[linha, "Contato"]
            
            msg = tabela.loc[linha, "Msg"]
            
            arquivo = tabela.loc[linha, "Arquivo"]
            
            
             # Para cada linha da base de dados
            # Searching for element 'lupa '
            if not self.find("lupa", matching=0.97, waiting_time=60000):
                self.not_found("lupa")
            self.click()
            
            self.type_keys_with_interval(100, contato) 
            
            self.enter()
            
            mensagem = msg
            
            self.paste(mensagem)
            
            self.enter()
            
            if pd.isna(arquivo) == False:
                
                
                # Searching for element 'anexar '
                if not self.find("anexar", matching=0.97, waiting_time=10000):
                    self.not_found("anexar")
                self.click()
                
                # Searching for element 'documento '
                if not self.find("documento", matching=0.97, waiting_time=10000):
                 self.not_found("documento")
                self.click()    
                
                # Searching for element 'nome '
                if not self.find("nome", matching=0.97, waiting_time=10000):
                    self.not_found("nome")
                    
                
                self.paste(arquivo)
                
                self.enter()
                
                 # Searching for element 'enviar '
                if not self.find("enviar", matching=0.97, waiting_time=10000):
                     self.not_found("enviar")
                self.click()
                 
                 
                
            
            

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()











