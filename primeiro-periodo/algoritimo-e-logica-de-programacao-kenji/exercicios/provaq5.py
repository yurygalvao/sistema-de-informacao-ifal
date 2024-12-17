import re


usuarios = []

def validar_nome_usuario(nome_usuario):

    if len(nome_usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        return False
    

    if "@" not in nome_usuario or "." not in nome_usuario:
        print("O nome de usuário deve conter ao menos um '@' e um '.'")
        return False
    

    for usuario in usuarios:
        if usuario['nome'] == nome_usuario:
            print("Este nome de usuário já está cadastrado.")
            return False
    
    return True


def validar_senha(senha):

    if len(senha) < 6 or len(senha) > 8:
        print("A senha deve ter entre 6 e 8 caracteres.")
        return False
    

    if len(re.findall(r'\d', senha)) < 2:
        print("A senha deve conter pelo menos 2 números.")
        return False
    

    if len(re.findall(r'[a-zA-Z]', senha)) < 2:
        print("A senha deve conter pelo menos 2 letras.")
        return False
    

    if len(re.findall(r'[\W_]', senha)) < 2:
        print("A senha deve conter pelo menos 2 caracteres especiais.")
        return False
    
    return True


def cadastrar_usuario():
    nome_usuario = input("Digite o nome de usuário: ")
    if not validar_nome_usuario(nome_usuario):
        return
    
    senha = input("Digite a senha: ")
    if not validar_senha(senha):
        return
    
 
    usuarios.append({"nome": nome_usuario, "senha": senha})
    print(f"Usuário {nome_usuario} cadastrado com sucesso.")


def acessar_sistema():
    nome_usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    
    for usuario in usuarios:
        if usuario['nome'] == nome_usuario:
            
            if usuario['senha'] == senha:
                print("Acesso concedido!")
                return
            else:
                print("Senha incorreta.")
                return
    print("Usuário não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Cadastrar usuário e senha")
        print("2 - Acessar o sistema")
        print("3 - Sair")
        
        try:
            opcao = int(input("Escolha uma opção: "))
            
            if opcao == 1:
                cadastrar_usuario()
            elif opcao == 2:
                acessar_sistema()
            elif opcao == 3:
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número de 1 a 3.")

menu()  