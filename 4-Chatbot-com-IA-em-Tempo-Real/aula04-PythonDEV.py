# Passo a Passo do Projeto
# Título
# Input do chat (Campo de Mensagem)
# A cada mensagem que o usuário enviar:
    # Mostrar a mensagem que o usuário enviou no chat
    # Pegar a pegunta e enviar para uma IA responder
    # Exibir a resposta da IA na tela

# Framework: 
    # Streamlit: Criar o BackEnd e o FrontEnd com Python
    # IA: OpenAI, Gemini, Grok...

# pip install streamlit openai cerebras-cloud-sdk

# Para rodar o site deve-se salvar o arquivo e rodar no terminal: "streamlit run 'caminho ou nome do arquivo'"

import streamlit as st
from openai import OpenAI # Importando a função 'OpenAI' da biblioteca 'openai'
from cerebras.cloud.sdk import Cerebras # Achei essa aqui na internet que a API é de 'graça'

# Criar e definir a chave de API
modelo_IA_OpenIA = OpenAI(api_key = "api da OpenAI")

modelo_IA_Cerebras = Cerebras(api_key = "api da Cerebras")

# st.write(): Escrever alguma coisa
# st.button(): Criar um botão
# st.chat_input(): Criar um input

st.write("# ChatBot com IA DO MIGUEL") # Markdown

if not "lista_mensagens" in st.session_state: # session_state: Cria a lista de mensagens (se não existir)
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem") # Cria uma caixa de input para digitar a mensagem

# Exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]: # Cada item da lista é um dicionário
    role = mensagem["role"] # Define quem enviou a mensagem
    content = mensagem["content"] # Texto da mensagem
    st.chat_message(role).write(content) # Mostra a mensagem no chat usando o formato visual do Streamlit

if texto_usuario:

    # Usuário:
    st.chat_message("user").write(texto_usuario) # .chat_message - Mostra o ícone da mensagem, pode ser: 'Nome', user ou assistant

    mensagem_usuario = {"role":"user", "content": texto_usuario}  # Cria um valor no dicionário representando a mensagem do usuário
    st.session_state["lista_mensagens"].append(mensagem_usuario) # Adiciona essa nova mensagem
    
    # IA
    resposta_ia = modelo_IA_Cerebras.chat.completions.create(
      messages = st.session_state["lista_mensagens"],
      model = "llama3.1-8b", # Modelo de linguagem utilizado
      max_completion_tokens = 1024, # Limite máximo de tokens da resposta
      temperature = 0.2, # Controla a criatividade da IA: valores baixos → respostas mais previsíveis // valores altos → respostas mais criativas
      top_p = 1, # Outro parâmetro de controle de diversidade de palavras
      stream = False) # Se True, a resposta viria em partes (streaming)

    # A resposta da IA vem dentro de uma estrutura de dados:
    texto_resposta_ia = resposta_ia.choices[0].message.content # choices[0] → primeira resposta gerada // # message.content → conteúdo textual da resposta

    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role":"assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

    # OBS: Definindo a resposta do OpenAI:
    # resposta_ia_OpenAI = modelo_IA_OpenIA.chat.completions.create(messages=st.session_state["lista_mensagens"], model="gpt-4o")

