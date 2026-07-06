# importar a classe
from bc_classe import Pessoa

# importar a biblioteca para trabalhar com MySQL
import mysql.connector

def retornar_pessoas():

    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE pessoas_db")
    
    # executar o comando SQL para selecionar todas as pessoas
    cursor.execute('SELECT nome, email, telefone FROM pessoas')
    
    # obter os resultados da consulta
    pessoas = cursor.fetchall()

    # preparar uma lista de retorno
    retorno = []

    # percorrer a lista de pessoas obtidas
    for pessoa in pessoas:

        # converter cada pessoa obtida em um OBJETO
        nova = Pessoa(pessoa[0], pessoa[1], pessoa[2])

        # adicionar a nova pessoa_objeto na lista de retorno
        retorno.append(nova)

     # fechar a conexão com o banco de dados
    conn.close()

    # retornar o retorno :-)
    return retorno

'''
alternativas:

a) retorno = [Pessoa(nome, email, telefone) for nome, email, telefone in cursor.fetchall()]

b) return [Pessoa(*pessoa) for pessoa in cursor.fetchall()]

'''