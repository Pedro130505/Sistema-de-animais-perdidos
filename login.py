from registro import Registro
from manipulação_dados.ler_dados import Ler_dados
#AQUI EU ABRO O BANCO DE DADOS 
from utilidades.contador_senha import contador_erro_senha
banco_usuarios = {}

def retorna():
    return True 
def retorna2():
    return False

class LogIn:

    def cadastrar(self):
        print('Conta não cadastrada. Vamos criar uma.')
        nome = input('Nome: ')
        email = input('Email: ')
        senha = input('Senha: ')
        novo_usuario = Registro(nome, email, senha)

    def __init__(self,email,senha):
       # email = input("Digite seu email: ")#compara com o banco de cadastros 
        self.email=email
        if Ler_dados.ler_email(self.email) is True:
            #senha = input("Digite sua senha: ")
            self.senha=senha
            if Ler_dados.ler_senha(self.senha) is True:
                print("Login bem-sucedido!")
               # retorna()

            else:
                contador_erro_senha()
                #self.__init__()
                print('Senha errada')
                #retorna2()
        else:
            print('Senha errada')
            #retorna2()
           #self.cadastrar()
           # self.__init__()  # Tenta logar novamente após cadastro
      
    
      

# Início do sistema