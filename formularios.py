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

