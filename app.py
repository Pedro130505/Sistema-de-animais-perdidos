from flask import Flask, render_template, request, redirect,flash,session
from login import * # Importando a classe Registro do arquivo backend
from manipulação_dados.ler_dados import *

app = Flask(__name__)

# Rota para exibir o login (GET)
@app.route('/')
def index():
    return render_template('login.html')  # Renderiza o template 'login.html'

app.secret_key = 'seu_valor_aqui'
# Rota para processar o login (POST)
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']
    
    usuario = LogIn(email, senha)
    if   Ler_dados.ler_senha(senha) is  True:
        return "Você entrou com sucesso!" # redireciona pagina usuario
    elif Ler_dados.ler_email(email) is False:
        return "Este email nao esta cadastrado, faça seu registro" # redireciona pagina registrop
    else:
        return"Senha incoreta" # retorna mesma pagina 
        
if __name__ == '__main__':
    app.run(debug=True)