
# É importante utilizar o comando "playwright install" para garantir que ele instale ou atualize as extensões que o possibilita a acessar os navegadores

# Observação: vale lembrar que o formato ipynb (notebook jupyter) não
# possibilita a utilização de comandos que contém o trecho sync_api

from playwright.sync_api import sync_playwright

import time

with sync_playwright() as pw:
    
    navegador = pw.chromium.launch(headless=False)
    
    contexto = navegador.new_context()
    
    pagina = contexto.new_page()
    
    pagina.goto("https://www.hashtagtreinamentos.com/?origemurl=75502579145&base-brand")
    
    print(pagina.title())
    
    # pagina.locator('xpath=/html/body/main/section[1]/div[2]/a').click()
    
    # playwright codegen  https://www.hashtagtreinamentos.com
    
    botao = pagina.get_by_role("link", name="Quero aprender").first  
    
    divisorias = pagina.locator("div").all()
    
    print(divisorias)
    
    print("Quantidade de divisorias: ", len(divisorias))
    
    with contexto.expect_page() as pagina2_info:
        
        botao.click()  
    
    pagina2 = pagina2_info.value
    
    pagina2.goto("https://www.hashtagtreinamentos.com/curso-python")
    
    pagina2.get_by_role("textbox", name="Seu primeiro nome").fill("Caio")
    
    pagina2.get_by_role("textbox", name="Seu melhor e-mail").fill("email@gmail.com")
    
    pagina2.get_by_role("textbox", name="Seu WhatsApp com DDD").fill("11999999999")
    
    pagina2.get_by_role("button", name="Quero acessar as informações").click()
    time.sleep(15)
        
    navegador.close()