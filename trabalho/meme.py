import json

ARQUIVO = "dados.json"
with open(ARQUIVO, "a+") as arquivo:
    arquivo.seek(0)
    try:
        json.load(arquivo)
    except:
        arquivo.write("[]")

def menu():
    opcao = 0
    while opcao !=5:
        print("\n1 - Criar usuário")
        print("2 - Lista de usuários")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Sair")
        opcao = int(input("Escolha:"))
        if opcao == 1:
            criar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        elif opcao == 5:
            break

def carregar():
    with open(ARQUIVO, "r") as arquivo:
        return json.load(arquivo)

def salvar(dados):
    with open(ARQUIVO, "w") as arquivo:
        json.dump(dados, arquivo)

def criar():

    nome = input("Usuário: ")
    idade = input("Idade: ")
    email = input("Email: ")
    senha_do_usuario = input("Senha: ")

    dados = carregar()
    dados.append({"usuário": nome, "Idade": idade, "Email": email, "Senha": senha_do_usuario})
    salvar(dados)
    print("Salvo!")

def listar():
    dados = carregar()
    for p in dados:
        print(p)

def atualizar():
    nome = input("usuário para atualizar:")
    dados = carregar()
    for linha in dados:
        if linha["usuário"] == nome:
            linha["idade"] = input("Nova idade:")
            linha["email"] = input("Novo email:")
            linha["senha"] = input("Nova senha:")
            salvar(dados)
            print("Atualizado!")
        else:
            print("Não autualizado!")

def deletar():
    nome = input("Nome para deletar:")
    dados = carregar()
    for linha in dados:
        if linha["usuário"] == nome:
            dados.remove(linha)
            salvar(dados)
            print("\n\n ❌ Deletado! \n\n")
        else:
            print("Usuário não encontrado")

menu()