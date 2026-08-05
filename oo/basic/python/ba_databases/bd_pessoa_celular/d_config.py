import os 

DATABASE_NAME = "ifcblu2026"
HOST = os.getenv("DATABASE_HOST", "localhost") 
USER = os.getenv("DATABASE_USER", "root") 
PASSWORD = os.getenv("DATABASE_PASSWORD", "root") 
PORT = os.getenv("DATABASE_PORT", "3306")

TABELA_PESSOAS = "tbl_pessoas_hylson"
TABELA_CELULARES = "tbl_celulares_hylson"

'''
como configurar as variáveis:

no WINDOWS (prompt de comando):
----------

* definir:
set MINHA_VARIAVEL=valor

* visualizar:
echo %MINHA_VARIAVEL%


no WINDOWS (powershell):
----------

* definir:
$env:MINHA_VARIAVEL = "valor"

* visualizar:
echo $env:MINHA_VARIAVEL

no LINUX:
---------

* definir:

export DATABASE_NAME="pessoas_db"
export DATABASE_HOST="zzzzz"
export DATABASE_USER="yyyyy"
export DATABASE_PASSWORD="KKKKK"

* visualizar:

echo $DATABASE_USER

'''