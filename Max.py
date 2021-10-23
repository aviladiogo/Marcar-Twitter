import schedule
import webbrowser
from keyboard import press_and_release, write
from time import sleep
from pynput.mouse import Button, Controller

mouse = Controller()
n = 0

def marca():
    press_and_release('shift+2') # @
    write('victorialuquett')
    press_and_release('enter')
    sleep(0.5)
    press_and_release('shift+2') # @
    write('Quequeh0uve')
    press_and_release('enter')
    sleep(0.5)
    press_and_release('shift+2') # @
    write('juuldecereja')
    press_and_release('enter')

def envia():
    mouse.position = (1007, 458) # envia o cursor para o botao de enviar do twitter
    mouse.click(Button.left, 1)

def fechar():
    mouse.position = (1514, 11) # envia o cursor para o botão de fechar o chrome
    mouse.click(Button.left, 1)

def VôMax():
    webbrowser.open('https://twitter.com/vomaxroupa', new=2) # abre a pagina do twitter no chrome
    sleep(5)
    mouse.position = (739, 803) # Abre a Publicação mais recente
    sleep(0.1)
    mouse.click(Button.left, 1)
    sleep(0.1)
    press_and_release('r') # Aperta R para responder o tweet
    sleep(0.5)
    marca()
    sleep(0.5)
    envia()
    sleep(0.1)
    fechar()
    print("Rodou")   

def progress_bar(done):
    print("\rCarregando: [{0:50s}] {1:.1f}%".format('|' * int(done * 50), done * 100),end='')

def test():
    global n
    if(n == 100):
        n = 0
    progress_bar(n/100)
    n += 1

schedule.every().day.at("14:30").do(VôMax) # Função da biblioteca Schedule, ira todo dia as 14:30 realizar a função 



while 1:
    schedule.run_pending()
    test()
    sleep(1)