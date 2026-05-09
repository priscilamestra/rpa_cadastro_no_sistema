from time import sleep
import pyautogui

sleep(5) # tempo para o usuário abrir o sistema da empresa e posicionar o mouse no campo de login  
print(pyautogui.position()) # posição do mouse para clicar no campo de login


