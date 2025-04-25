from registrocod import Registro
posts_ligados_email = {} 
lista_geral= []
def formulario():
    print('Prencha os fomulario')
    tipo_animal=input('Qual animal foi visto : ')
    raca= input('Qual a raca: ')
    local= input('Onde o animal foi visto: ')
    bairro= input('Qual bairro: ')
    rua= input('Qual rua: ')
    horas= input('Quando o animal foi visto: ')
    infos=input('Adicione a informação desejada:  ')
    if not tipo_animal or not local or not bairro : 
        print('Preencha as informações obrigatoria')
    
    dic = { 
        'tipo animal': tipo_animal,
        'raca': raca,
        'local' : local,
        'bairro' : bairro,
        'rua': rua,
        'horas': horas,
        'infos': infos  }
    return dic


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
    def __init__(self, email,nome):
       super().__init__(email, nome)
    #pode executar ações
    #criar post
    #pesquisar
    #expluir post 
    
    def crirar_post(self):
        novo_post= formulario() 
        posts_ligados_email[self.email]={novo_post} # lista para atrelar post a uma conta e poder ser expluidop
        lista_geral.append(novo_post) # lista para todos verem 
        #criar forma de adicionar foto

    def ver_meus_posts(self):
        print(posts_ligados_email[self.email])
        

    def pesquisar():
        filtro()

    def excluir(self): 
        print(posts_ligados_email[self.email])
        
    