# importações...
from a_classes import Pessoa, Celular
from d_config import *
# biblioteca para trabalhar com MySQL
import mysql.connector

# ---------------------------
# FUNÇÕES INTERNAS AUXILIARES
# ---------------------------

# configure nesta função parâmetros do banco de dados
# função interna auxiliar, com retorno múltiplo :-)
def retornar_conexao_e_cursor():
    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        port=PORT
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute(f"USE {DATABASE_NAME}")      
    
    return conn, cursor

# função que procura uma pessoa na lista de pessoas
def localizar_pessoa_por_id(lista_de_pessoas: list[Pessoa], id_procurado):
    for p in lista_de_pessoas:
        if p.id == id_procurado:
            return p
    return None

# ------------------
# CLASSE DE SERVIÇOS
# ------------------

class Servico:

    def criar_tabelas(self):
        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        
        
        # executar o comando SQL para incluir a pessoa
        cursor.execute(f'''
                CREATE TABLE {TABELA_PESSOAS} (
                id INT NOT NULL AUTO_INCREMENT,
                nome varchar(255) NOT NULL,
                email varchar(255) NOT NULL,
                PRIMARY KEY (id)
                );
        ''')

        # confirmar as alterações
        conn.commit()

        cursor.execute(f'''
                CREATE TABLE {TABELA_CELULARES} (
                id INT NOT NULL AUTO_INCREMENT,
                numero varchar(50) NOT NULL,
                marca varchar(50) NOT NULL,
                operadora varchar(50) NOT NULL,
                pessoa_id int NULL,
                PRIMARY KEY (id),
                FOREIGN KEY (pessoa_id) REFERENCES {TABELA_PESSOAS}(id)
                );
        ''')

        # confirmar as alterações
        conn.commit()
        
        # fechar a conexão com o banco de dados
        conn.close()

    def popular_tabelas(self):
        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        
        
        # cadastrar duas pessoas
        cursor.execute(f"INSERT INTO {TABELA_PESSOAS} VALUES (NULL, %s, %s)",
                        ("João da Silva", "jo@gmail.com"))

        cursor.execute(f"INSERT INTO {TABELA_PESSOAS} VALUES (NULL, %s, %s)",
                                        ("Maria Oliveira", "maliv@gmail.com"))

        # cadastrar um celular
        # esse celular será da pessoa "1"
        cursor.execute (f"INSERT INTO {TABELA_CELULARES} VALUES (NULL, %s, %s, %s, %s)",
                        ("47 9 99887766", "Nokia", "Claro", 1))

        # confirmar as alterações
        conn.commit()
        
        # fechar a conexão com o banco de dados
        conn.close()

    def incluir_pessoa(self, pessoa: Pessoa):

        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        
        
        # executar o comando SQL para incluir a pessoa
        cursor.execute(f"INSERT INTO {TABELA_PESSOAS} (nome, email) VALUES (%s, %s)", (pessoa.nome, pessoa.email))

        # confirmar as alterações
        conn.commit()
        
        # fechar a conexão com o banco de dados
        conn.close()

    def retornar_pessoas(self):

        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        
    
        # executar o comando SQL para selecionar todas as pessoas
        cursor.execute(f'SELECT id, nome, email FROM {TABELA_PESSOAS}')
        
        # obter os resultados da consulta
        pessoas = cursor.fetchall()

        # construção de uma lista de objetos em uma linha só!
        retorno = [Pessoa(*p) for p in pessoas]

        # fechar a conexão com o banco de dados
        conn.close()

        # retornar o retorno :-)
        return retorno

    def remover_pessoa_via_email(self, email: str):

        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        
        
        # executar o comando SQL para incluir a pessoa
        cursor.execute(f"DELETE from {TABELA_PESSOAS} WHERE email = %s", (email,))

        # confirmar a exclusão
        conn.commit()
        
        # fechar a conexão com o banco de dados
        conn.close()

    def retorna_quantidade_registros(self, tabela : str):
        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        
    
        # executar o comando SQL para selecionar todas as pessoas
        cursor.execute(f"SELECT count(*) from {tabela}")
        
        # obter os resultados da consulta
        registros = cursor.fetchall()

        # construção de uma lista de objetos em uma linha só!
        retorno = int(registros[0][0])

        # fechar a conexão com o banco de dados
        conn.close()

        # retornar o retorno :-)
        return retorno

    def retornar_celulares(self):
    
        # obter conexão e cursor
        conn, cursor = retornar_conexao_e_cursor()        

        # obtém todas as pessoas
        pessoas = self.retornar_pessoas()

        # obtém os celulares
        cursor.execute(f"SELECT id, numero, marca, operadora, pessoa_id FROM {TABELA_CELULARES}")
        
        # pega os resultados
        resultados = cursor.fetchall()

        # prepara a lista de retorno (celulares)
        retorno = []

        # percorrer os resultados
        # "r" contém número, marca, operadora e pessoa_id
        for r in resultados:

            # localiza a pessoa que é dona daquele celular
            p = localizar_pessoa_por_id(pessoas, r[4])

            if p == None:
                # pula esse registro, pois deu algum erro :-/
                # toda pessoa devia existir,
                # por causa da integridade referecial
                continue
            else:
                # cria o celular com a pessoa 
                c = Celular(r[0], r[1], r[2],r[3], p)
                # adiciona na lista de retorno
                retorno.append(c)
        
        # fechar a conexão com o banco de dados
        conn.close()

        # retornar o retorno :-)
        return retorno