from keyboard import press_and_release, write
from time import sleep, localtime
import webbrowser
from pynput.mouse import Button, Controller

mouse = Controller()


def marca():
    press_and_release('shift+2') # @
    write('victorialuquett')
    press_and_release('enter')
    sleep(1)
    press_and_release('shift+2') # @
    write('Quequeh0uve')
    press_and_release('enter')
    sleep(1)
    press_and_release('shift+2') # @
    write('juuldecereja')
    press_and_release('enter')
def envia():
    mouse.position = (1007, 458) # envia o cursor para o botao de enviar do twitter
    mouse.click(Button.left, 1)
def fechar():
    mouse.position = (1514, 11) # envia o cursor para o botão de fechar o chrome
    mouse.click(Button.left, 1)

while True:
    hora = localtime()
    if(hora.tm_hour != 14): # caso não seja 14 horas  
        print("esperando proxima hora")
        sleep(3600)
    elif(hora.tm_hour == 14 and hora.tm_min == 30): # caso seja a hora exata do novo post
        webbrowser.open('https://twitter.com/vomaxroupa', new=2) # abre a pagina do twitter no chrome
        sleep(8)
        mouse.position = (739, 803) # Abre a Publicação mais recente
        sleep(0.1)
        mouse.click(Button.left, 1)
        sleep(2)
        press_and_release('r') # Aperta R para responder o tweet
        sleep(2)
        marca()
        sleep(2)
        envia()
        sleep(2)
        fechar()
        break
    else:
        print("esperando minutagem") #caso seja 14 horas porém não seja 14:30
        print(hora.tm_min)
        sleep(60)
