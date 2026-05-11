from time import sleep
import pyautogui

sleep(5) # tempo para o usuário abrir o sistema da empresa e posicionar o mouse no campo de login  
print(pyautogui.position()) # posição do mouse para clicar no campo de login

# Esse script serve caso o sistema de 'tab' criado no main.py não funcione, ou seja, caso o sistema de 'tab' não clique no campo de código do produto.
# O código acima é para o usuário abrir o sistema da empresa e posicionar o mouse no campo de login, para que a automação possa clicar nesse campo e preencher os dados de login automaticamente. 
# O tempo de 5 segundos é para dar tempo ao usuário de abrir o sistema e posicionar o mouse, mas pode ser ajustado conforme necessário. 
# A função pyautogui.position() retorna a posição atual do mouse, que pode ser usada para clicar no campo de login.