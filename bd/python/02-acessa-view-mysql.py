'''

* install library:

windows:
pip install mysql-connector-python

linux:
pip3 install mysql-connector-python --break-system-packages

* create the table and the view

CREATE TABLE pessoa (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  data_nascimento DATE
);

INSERT INTO pessoa (nome, email, data_nascimento) VALUES
('Maria Oliveira', 'maoliv@gmail.com', '1985-03-22'),
('João Silva', 'josilva@gmail.com', '1990-07-15'),
('Ana Costa', 'acosta@gmail.com', '1978-11-30'),
('Pedro Santos', 'pesantos@gmail.com', '1995-05-10');



CREATE OR REPLACE
    DEFINER = 'root'@'%'
    SQL SECURITY DEFINER
VIEW vw_pessoa AS
SELECT nome, email FROM pessoa WHERE YEAR(data_nascimento) >= 1990 ORDER BY nome;

GRANT SELECT ON vw_pessoa TO 'marcosoliveira'@'%';

show grants for 'marcosoliveira'@'%';

SQL SECURITY DEFINER: visão é executada com privilégio do criador da visão (definer), e não do usuário que a acessa.
SQL SECURITY INVOKER: visão é executada com privilégio do usuário que a acessa (invoker). É a opção padrão.

'''

import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="localhost",       # Your database host
    user="marcosoliveira",            # Your MySQL username
    password="moliveira",  # Your MySQL password
    database="hylson_pessoa_mysql_python"      # The database name
)

cursor = connection.cursor()
query = "SELECT * FROM vw_pessoa"
cursor.execute(query)
rows = cursor.fetchall()
print("Pessoas que nasceram a partir de 1990:")
for row in rows:
    print(f"Nome: {row[0]}, Email: {row[1]}")
cursor.close()
connection.close()

'''
$ python3 02-acessa-view-mysql.py
Pessoas que nasceram a partir de 1990:
Nome: João Silva, Email: josilva@gmail.com
Nome: Pedro Santos, Email: pesantos@gmail.com

'''
