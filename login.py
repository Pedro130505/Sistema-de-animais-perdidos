from registrocod import Registro


banco_usuarios = {}
erros = 0
def contador_erro_senha():
    global erros
    erros += 1
    print('Senha incorreta!')
    if erros >= 3:
        print('Sua conta foi bloqueada momentaneamente.')

# Verificação de email
def verifica_email(email):
    return email in banco_usuarios

# Verificação de senha
def verifica_senha(email, senha):
    return banco_usuarios.get(email) == senha

# Cadastro
def dados_cadastro():
    print('Conta não cadastrada. Vamos criar uma.')
    nome = input('Nome: ')
    email = input('Email: ')
    senha = input('Senha: ')
    novo_usuario = Registro(nome, email, senha)
    banco_usuarios[email] = senha
    print(f'Usuário {nome} cadastrado com sucesso!')





class LogIn:
    def __init__(self):
        email = input("Digite seu email: ")#compara com o banco de cadastros 
        if verifica_email(email) is True:
            senha = input("Digite sua senha: ")
            if verifica_senha(email, senha) is True:
                print("Login bem-sucedido!")
            else:
                contador_erro_senha()
                self.__init__()
        else:
            dados_cadastro()
            self.__init__()  # Tenta logar novamente após cadastro

# Início do sistema