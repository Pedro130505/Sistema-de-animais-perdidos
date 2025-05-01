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