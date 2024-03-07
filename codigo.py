# Passo a passo do projeto:



# Passo 1: Entrar no sistema da empresa:
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui no terminal
import time
import pyautogui

pyautogui.PAUSE = 0.5
tempo_seguranca = 3

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Fazer uma pausa
time.sleep(tempo_seguranca)



# Passo 2: Fazer o login
pyautogui.click(-1181, 406)
pyautogui.write("teste@gmail.com")

pyautogui.click(-1168, 505)
pyautogui.write("123456789")

pyautogui.click(-957, 572)

# Fazer outra pausa
time.sleep(tempo_seguranca)

# ex.: pyautogui.click(0, 0, clicks=2, button='left/right/middle')



# Passo 3: Importar a base da dados

import pandas

tabela = pandas.read_csv("./produtos.csv")



# Passo 4: Cadastrar um produto.
# Passo 5: Repitir o processo de cadastro até cadastrar todos os produtos


for linha in tabela.index:

    # Clica no primeiro campo
    pyautogui.click(-1130, 290)

    # Começa a inserir as informações do produtos
    # Código
    pyautogui.write(tabela.loc[linha, 'codigo'])

    # Marca
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, 'marca'])

    # Tipo
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha, 'tipo'])

    # Categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'categoria']))

    # Preço
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))

    # Custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, 'custo']))

    # Observação
    pyautogui.press("tab")

    observacao = tabela.loc[linha, 'obs']
    if not pandas.isna(observacao):
        pyautogui.write(observacao)

    # Enviar Fomrulário
    pyautogui.click(-1048, 961)
    pyautogui.click(-1048, 961)

    # Scroll
    pyautogui.scroll(5000)
