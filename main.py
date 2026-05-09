# Lógica da automação do desktop para cadastro de produtos em um sistema da empresa
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto 
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

import pandas as pd
import pyautogui
from time import sleep

pyautogui.PAUSE = 1
link = 'http://localhost:8000/.venv/sistema/cadastro_de_produtos/login.html'

pyautogui.hotkey('win', 'r') # abrir o menu executar do Windows
pyautogui.write('chrome --incognito') # abrir o navegador Google Chrome no modo anônimo
pyautogui.press('enter')

sleep(1) # pausa para o navegador abrir

pyautogui.write(link)
pyautogui.press('enter')

sleep(3)

pyautogui.click(x=-818, y=382) # clicar no campo email
pyautogui.write('usuario@exemplo.com')
pyautogui.press('tab') # passar para o campo de senha
pyautogui.write('senha123')
pyautogui.press('tab') # passar para o botão de login
pyautogui.press('enter')

sleep(1)

tabela = pd.read_csv('produtos.csv')

# Cadastrar primeiro produto
# Para cada linha da tabela, ou seja, para cada produto
# O código dentro do for vai ser repetido, ou seja, o processo de cadastro de produto vai ser repetido para cada produto da tabela
# Index é o número da linha, ou seja, o número do produto na tabela (índice começa em 0, então o primeiro produto tem índice 0, o segundo produto tem índice 1, e assim por diante)

for linha in tabela.index: 

    # Codigo do produto
    pyautogui.click(x=-856, y=291) # clicar no campo de código do produto
    codigo = str(tabela.loc[linha, 'codigo'])# pegar o código do produto da tabela
    pyautogui.write(codigo)
    pyautogui.press('tab')

    # Marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)
    pyautogui.press('tab')

    # Tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)
    pyautogui.press('tab')

    # Categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('tab')

    # Preco
    preco = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco)
    pyautogui.press('tab')

    # Custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('tab')

    # Obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan': # se a observação não for NaN, ou seja, diferente de NaN, então escreva a observação, caso contrário, deixe o campo de observação vazio
        pyautogui.write(obs)
    pyautogui.press('tab')

    pyautogui.press('enter') # passar para o botão de enviar

    # voltar para o início da tela para cadastrar o próximo produto
    pyautogui.scroll(5000) # rolar a tela para cima (positivo para rolar para cima, negativo para rolar para baixo)


# NaN = Not a Number, ou seja, um valor que não é um número, um valor vazio ou nulo.