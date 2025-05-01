import registro
from usuario import Usuario
from login import LogIn

escolha = int(input('1) Fazer login \n 2) Criar Conta'))


if escolha == 1:
    seu_login= LogIn() 
    #seu_nome= seu_login.nome
    seu_email= seu_login.email
    seu_usuario=  Usuario(seu_email)
    seu_usuario.chama_escolhas() 

else:
    LogIn.cadastrar()
