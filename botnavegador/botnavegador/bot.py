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

from botcity.web import WebBot, Browser
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *

# Import da classe ChromeDriverManager do módulo chrome da biblioteca
# chrome. Vamos usar essa classe para adquirir o driver que possibilita
# que o python se comunique com o chrome. 
from webdriver_manager.chrome import ChromeDriverManager

class Bot(WebBot):
    def action(self, execution=None):
    
        # Configure whether or not to run on headless mode
        self.headless = False
        
        # Como esse arquivo do botcity é do tipo web, precisamos
        # especificar o driver do navegador que vamos utilizar.
        # Para isso vamos instanciar a classe ChromeDriverManager
        # e chamar a função isntall que irá baixar ou atualizar
        # o driver do chrome e armazenar o caminho do arquivo
        # driver
        self.driver_path = ChromeDriverManager().install()


        # Opens the BotCity website.
        self.browse("https://www.google.com")
        
        # Searching for element 'campo_pesquisa '
        if not self.find("campo_pesquisa", matching=0.97, waiting_time=10000):
            self.not_found("campo_pesquisa")
        self.click()
        
        self.paste('cotação do dolar')
        
        self.enter()
        
        # Searching for element 'dolaramericano '
        if not self.find("dolaramericano", matching=0.97, waiting_time=10000):
            self.not_found("dolaramericano")
        self.double_click_relative(14, 75)
        
        self.control_c()
        
        cotacao = self.get_clipboard()
        
        print("Valor atual da cotação do dolar: ", cotacao)
        
    
        input("Pressione enter para fechar o navegador")
        # Wait for 10 seconds before closing
        self.wait(10000)

        # Stop the browser and clean up
        self.stop_browser()



    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()

