from aplicacao import database, login_manager
# UserMixin tem todos os métodos e atributos necessários para criar uma classse login
from flask_login import UserMixin


# Criar função para procurar um usuário através de um id
# login_manager gerencia o login
@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

# A classe serve para criar as tabelas através do sqlalchemy
# A classe Model possui um padrão para a criação da tabela
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key = True)
    usuario = database.Column(database.String, nullable= False)
    email =  database.Column(database.String, nullable= False, unique = True)
    senha = database.Column(database.String, nullable= False)