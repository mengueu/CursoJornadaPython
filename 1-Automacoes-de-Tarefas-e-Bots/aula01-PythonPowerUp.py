# Passo a passo do seu programa
# Passo 1: Entrar no sistema da empresa
# Passo 2: Fazer login
# Passo 3: Abrir a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar a lista de produtos

# bibliotecas = pacotes de código
# Instalar uma biblioteca: pip install nomedabiblioteca
# Importar (usar) uma biblioteca: import nomedabiblioteca

import pyautogui
import time

# Função para clicar em um local da tela: pyautogui.click
# Função para escrever um texto: pyautogui.write
# Função para pressionar uma tecla: pyautogui.press
# Função para pressionar um atalho: pyautogui.hotkey

# Passo 1: Entrar no sistema da empresa
pyautogui.PAUSE = 0.5 # Define a velocidade de execução entre as funções (por padão é o mais rápido possível)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(2) # Uma pausa maior para esperar o site carregar, usando outra biblioteca

# Passo 2: Fazer login
pyautogui.press("tab") # Passar para a caixa de input
pyautogui.write("EscreverAlgumEmailDeAcesso@aleatorio.com")
pyautogui.press("tab") # Passar para o próximo campo
pyautogui.write("1234")
pyautogui.press("enter")

# Passo 3: Abrir base de dados
import pandas # Biblioteca para manipular arquivos e dados de tabela
tabela = pandas.read_csv("produtos.csv") # Função para ler o arquivo '.csv' que está na minha pasta
print(tabela)
pyautogui.press("tab")  

# Passo 5: Repetir o processo 4 para cada produto
for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto

    pyautogui.PAUSE = 0.5

    # Código
    codigo = str(tabela.loc[linha, "codigo"]) # Transformar a informação em string
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria 
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    # Custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # OBS
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter") # Clicar no botão enviar

    for i in range(7):
        pyautogui.PAUSE = 0.1
        pyautogui.hotkey("shift", "tab")    