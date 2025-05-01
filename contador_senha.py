
erros = 0
def contador_erro_senha():
    global erros
    erros += 1
    print('Senha incorreta!')
    if erros >= 3:
        print('Sua conta foi bloqueada momentaneamente.')
