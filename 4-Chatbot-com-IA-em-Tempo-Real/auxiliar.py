# Entendendo listas e dicionários para aplicar o conceito nos modelos de IA

# listas
lista = []
nomes = ["Nome 1", "Nome 2", "Nome 3"]

print(nomes)

nomes.append("Nome 4")
print(nomes)


# Dicionário = {chave: valor, chave: valor}
idades = {"Nome 1": 31, "Nome 2": 20, "Nome 3": 90}

print(idades["Nome 1"]) # Pega a informação do "Nome 1" no dicionário - dicionario[chave]

idades["Nome 4"] = 26 # Adicionando uma informação
idades["Nome 1"] = 10 # Editando a informação

print(idades)

# role = quem é o usuário
# content = conteúdo da mensagem
mensagem1 = {"role": "assistant", "content": "Olá, Chat! Me tira uma dúvida?"}
mensagem2 = {"role": "assistant", "content": "Claro! Qual a sua dúvida?"}
mensagem3 = {"role": "assistant", "content": "Então..."}

lista_mensagens = [mensagem1, mensagem2, mensagem3]

nova_mensagem = {"role":"assistant", "Content":"Ok! Entendi seu problema..."}

lista_mensagens.append(nova_mensagem)

