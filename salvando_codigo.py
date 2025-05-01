from registro import Registro
from utilidades.formularios import Formularios
from manipulação_dados.salvadados import Salvamento_dados


posts_ligados_email = {} 
lista_geral= []



def verifica_filtros_validos(filtro,*args):
         if filtro not in args:
            print('Nao foi possivel fazer essa filtragem') #fazer um sistema de escolha simultanea igual nos sites que escolhe mais de um filtro por vez
            print(lista_geral)                              # dados opções pre selecionadas


def filtro():
        lista_para_usuario=[]
        #fazer filtros que filtrem banco de dados
        print('filtros')
        tipo_filtro= input('O que deseja filtar: tipo animal, raca, local, bairro ,rua ,horas ,infos:')
        filtros_validos=['tipo animal, raca, local, bairro ,rua ,horas ,infos:']
        verifica_filtros_validos(tipo_filtro,filtros_validos)
                                 
        filtro= input('Qual seu filtro: ')
        for dict in lista_geral:
            if dict[tipo_filtro] == filtro: #criando lista filtrada
                lista_para_usuario.append(dict,) #fazer

            if not lista_para_usuario: #verificação
                print('Sem resultados para esses filtros')

        print(lista_para_usuario)

class Usuario(Registro): #USARIO RECEBE A PRIMERY KEY DO REGISTRO 
    def __init__(self, email):
         self.email=email
    def post_animias_achados(self):
            print('entrou na escolha 1')
            dados=Formularios.formulario_animais_achados()
            Salvamento_dados.salvar_formulario_achados(self.email,**dados)
            self.chama_escolhas()

    def post_animais_perdidos(self):
           print('entrou na escolha 2')
           dados=Formularios.formulario_animais_perdidos()
           Salvamento_dados.salvar_formulario_perdidos(self.email,**dados)
           self.chama_escolhas()
                    
            
    def ver_meus_posts(self):
                print(posts_ligados_email[self.email])
                
     
    def pesquisar():
                filtro()
        
    def excluir(self): 
                print(posts_ligados_email[self.email])


    def chama_escolhas(self):
        escolha=int(input('O que você deseja fazer:\n' \
            '1) Registrar animal achado \n'\
            '2) Registrar animal perdido\n'\
            '3) ver meus posts\n'\
            '4) Pesquisar posts\n'\
            '5)Deletar post\n\n'\
            ''))
        

        if escolha == 1:
               self.post_animias_achados()
        if escolha == 2:
               self.post_animais_perdidos()
             
               

        if escolha not in (1, 2, 3, 4):
            print("Não é possível realizar tal ação")

a =Usuario('brandao.pedro13@gmail.com')
a.chama_escolhas()

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
import registro
from usuario import Usuario
from login import LogIn

print('a')
escolha = int(input('1) Fazer login \n 2) Criar Conta'))
print('a')

if escolha == 1:
    seu_login= LogIn() 
    #seu_nome= seu_login.nome
    seu_email= seu_login.email
    seu_usuario=  Usuario(seu_email)
    seu_usuario.chama_escolhas() 

else:
    LogIn.cadastrar()

from registro import Registro
from manipulação_dados.ler_dados import Ler_dados
#AQUI EU ABRO O BANCO DE DADOS 
from utilidades.contador_senha import contador_erro_senha
banco_usuarios = {}


class LogIn:

    def cadastrar(self):
        print('Conta não cadastrada. Vamos criar uma.')
        nome = input('Nome: ')
        email = input('Email: ')
        senha = input('Senha: ')
        novo_usuario = Registro(nome, email, senha)

    def __init__(self):
        email = input("Digite seu email: ")#compara com o banco de cadastros 
        if Ler_dados.ler_email(email) is True:
            self.email=email
            senha = input("Digite sua senha: ")
            if Ler_dados.ler_senha(senha) is True:
                self.senha=senha
                print("Login bem-sucedido!")
            else:
                contador_erro_senha()
                self.__init__()
        else:
            self.cadastrar()
            self.__init__()  # Tenta logar novamente após cadastro
      
    
      

# Início do sistema


import pymysql
import dotenv
import os
from manipulação_dados.ler_dados import Ler_dados
from manipulação_dados.dados import Dados

class Salvamento_dados():

    def salvar_dados(nome,email,hash):
            connection = Dados.chama_arquivo()
            with connection.cursor() as cursor:
                sql = 'INSERT INTO REGISTRO (nome, email, pass_hash) VALUES (%s, %s, %s)' # o sql guarda quais colunas eu quero adicionar  #%s funciona como em c
                cursor.execute(sql, (nome,email,hash))# executa o processo nas colunas que o sql guardou 
                connection.commit()
    
    def salvar_formulario_achados(email,**kwargs):
        usuario_id=Ler_dados.pega_id(email)
        connection = Dados.chama_arquivo()
        #id = Ler_dados.pega_id(email) 
        with connection.cursor() as cursor:
    # Corrigindo a consulta SQL
          kwargs['usuario__id'] = usuario_id
          #print(kwargs)
          sql = '''
            INSERT INTO animais_achados
            (usuario__id, tipo_animal, raca, bairro, cidade, rua, horas, infos) 
            VALUES (%(usuario__id)s, %(tipo_animal)s, %(raca)s, %(bairro)s, 
                    %(cidade)s, %(rua)s, %(horas)s, %(infos)s)
        '''
          #print(kwargs)
          cursor.execute(sql, kwargs)
          connection.commit()
          # print("Linhas afetadas:", cursor.rowcount)
          #print('comite realizado')
        
    def salvar_formulario_perdidos(email,**kwargs):
        usuario_id=Ler_dados.pega_id(email)
        connection = Dados.chama_arquivo()
            #id = Ler_dados.pega_id(email) 
        with connection.cursor() as cursor:

            kwargs['usuario_id'] = usuario_id
            #print(kwargs)
            sql = '''
                INSERT INTO animais_perdidos
                (usuario_id, tipo_animal, raca, bairro, cidade, rua, horas, infos,nome) 
                VALUES (%(usuario_id)s,%(nome)s, %(tipo_animal)s, %(raca)s, %(bairro)s, 
                        %(cidade)s, %(rua)s, %(horas)s, %(infos)s)
            '''
            #print(kwargs)
            cursor.execute(sql, kwargs)
            connection.commit()
            # print("Linhas afetadas:", cursor.rowcount)
            #print('comite realizado')


import pymysql
import dotenv
import os
import bcrypt
from manipulação_dados.dados import Dados



class Ler_dados(Dados):

    def pega_id(email_desejado):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
            sql = "SELECT id FROM REGISTRO WHERE email = %s"
            cursor.execute(sql, (email_desejado,))
            resultado = cursor.fetchone() 
            somente_id = resultado[0]
            return somente_id
        
    def ler_email(email):
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
                    dados = ''
                    sql = 'SELECT email FROM REGISTRO '   # o sql guarda quais colunas eu quero adicionar  #%s funciona como em c
                    cursor.execute(sql)# executa o processo nas colunas que o sql guardou 
                    dados = cursor.fetchall()
                    for emails in dados:
                        for email_fora_tupla in emails: 
                            if email == email_fora_tupla:
                                print('ta na base')
                                return True
                                break
                    else:
                        print('n ta na base')
                        return False
    def ler_senha(senha):
        senha_hash=senha.encode('utf-8')
        connection = Dados.chama_arquivo()
        with connection.cursor() as cursor:
                    dados = ''
                    sql = 'SELECT pass_hash FROM REGISTRO '   # o sql guarda quais colunas eu quero adicionar  #%s funciona como em c
                    cursor.execute(sql)# executa o processo nas colunas que o sql guardou 
                    dados = cursor.fetchall()
                    for senhas in dados:
                        print(senhas)
                        for senha_fora_tupla in senhas: 
                            senha_fora_tupla = senha_fora_tupla.encode('utf-8') # fazendo o dado do banco virar bits
                            if bcrypt.checkpw(senha_hash, senha_fora_tupla):
                                #print('ta na base')
                                return True            
                    else:
                        #print('n ta na base')
                        return False

import pymysql
import dotenv
import os
import bcrypt


class Dados: 
    @staticmethod
    def chama_arquivo():
        dotenv.load_dotenv()
        connection = pymysql.connect( 
            host= os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'],
    )   
        return connection
def password_hash(senha):

    import bcrypt
    senha_bytes = senha.encode('utf-8')

    salt = bcrypt.gensalt()  # Gera um salt aleatório e seguro

    # Hashing Password
    hashed = bcrypt.hashpw(password=senha_bytes, salt=salt)  # Gera o hash da senha usando o salt
    return hashed 
    # Hashed Password
    #print(f"Hashed Password: {hashed.decode('utf-8')}")

erros = 0
def contador_erro_senha():
    global erros
    erros += 1
    print('Senha incorreta!')
    if erros >= 3:
        print('Sua conta foi bloqueada momentaneamente.')
class Formularios():
    def formulario_animais_achados():
        print('Prencha o fomulario')
        tipo_animal=input('Qual animal foi visto : ')
        raca= input('Qual a raca: ')
        cidade= input('Onde o animal foi visto: ')
        bairro= input('Qual bairro: ')
        rua= input('Qual rua: ')
        horas= input('Quando o animal foi visto: ')
        infos=input('Adicione a informação desejada:  ')
        if not tipo_animal or not cidade or not bairro : 
            print('Preencha as informações obrigatoria')
        
        dic = { 
            'tipo_animal': tipo_animal,
            'raca': raca,
            'cidade' : cidade,
            'bairro' : bairro,
            'rua': rua,
            'horas': horas,
            'infos': infos  }
        
        return dic

    def formulario_animais_perdidos():
        print('Prencha o fomulario')
        nome=input('Qual nome do animal perdido: ')
        tipo_animal=input('Qual animal foi visto : ')
        raca= input('Qual a raca: ')
        cidade= input('Onde o animal foi visto: ')
        bairro= input('Qual bairro: ')
        rua= input('Qual rua: ')
        horas= input('Quando o animal foi visto: ')
        infos=input('Adicione a informação desejada:  ')
        if not tipo_animal or not cidade or not bairro : 
            print('Preencha as informações obrigatoria')
        
        dic = { 
            'tipo_animal': tipo_animal,
            'raca': raca,
            'cidade' : cidade,
            'bairro' : bairro,
            'rua': rua,
            'horas': horas,
            'infos': infos,
            'nome':nome }
        
        return dic
