from manipulação_dados.salvadados import Salvamento_dados
from utilidades.pass_hash import password_hash


class Registro:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha =senha#jogar infos no banco de daDOS 
        # fazer umj if email ja esta na base de dados 
        senha_alterada= password_hash(self.senha)
      
        Salvamento_dados.salvar_dados(self.nome,self.email,senha_alterada) 