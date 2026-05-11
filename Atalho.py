# Objetivo da atividade da aula: Fazer uma automação que abre o navegador
# e acesse o site do google meet

# Observação: Para o keyboard funcionar no seu computador, você deve abrir
# a sua ide como administrador, dessa forma, o windows ira conceder ao
# keyboard o atalho que você definiu no argumento da função.

# Biblioteca de automação do python que tem como objetivo controlar o seu
# computador através do teclado e do mouse
import pyautogui

# Biblioteca do python que possibilita a criação de atalhos para realizações
# de tarefas.
import keyboard

# Biblioteca de manipulação de tempo do python
import time

# Fluxo da Tatrefa: abra o navegador -> entrar no meet
# Função que irá conter o script que acessara o navegador e procurar
# o google meet. 
def tarefa():
    
    # Acessando o meet
    
    # Ira dar um intervalo de 1 segundo antes de iniciar a execução da
    # da tarefa.
    time.sleep(1)

    # press: função que tem como objetivo pressionar as teclas do seu computador.
    
    # Ira pressionar a tecla win que acessa o menu do windows que contém
    # o navegador. 
    pyautogui.press("win")
    
    # Ira dar um intervalo de 1 segundo com o objetivo de garantir que 
    # o menu esteja carregado antes de seguir com a execução da tarefa.
    time.sleep(1)

    # write: Função do pyautogui que tem como objetivo escrever textos em
    # campos de texto presentes em sites, menus, etc.
    
    # Ira escrever no campo de pesquisa do menu, o nome do navegador 
    # que queremos acessar.
    pyautogui.write("microsoft edge")
    
    # Irá pressionar enter na busca pelo navegador.
    pyautogui.press("enter")
    
    # Ira dar um intervalo de 1 segundo com o objetivo de garantir que
    # o navegador esteja 100% carregado antes de prosseguir com a
    # execução da tarefa.
    time.sleep(1)
    
    # entrar no meet
    
    # Ira escrever o link do site no navegador
    pyautogui.write("https://meet.google.com/")
    
     # Ira pressionar o enter na pesquisa realizada
    pyautogui.press("enter")
        
# Função que tem como objetivo criar atalhos para tarefas. A função recebe como argumento o conjunto de teclas que você quer utilizar como atalho e a função que irá conter o script da tarefa       
keyboard.add_hotkey("ctrl+shift+l", tarefa)

# Função que recebe como argumento uma tecla (de sua escolha) que indica
# o encerramento da execução do programa.
keyboard.wait("esc")