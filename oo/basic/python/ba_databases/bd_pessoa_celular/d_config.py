import os 

DATABASE_NAME = "ifcblu2026"
HOST = os.getenv("DATABASE_HOST", "localhost") 
USER = os.getenv("DATABASE_USER", "root") 
PASSWORD = os.getenv("DATABASE_PASSWORD", "root") 

TABELA_PESSOAS = "tbl_pessoas_hylson"
TABELA_CELULARES = "tbl_celulares_hylson"

'''
como configurar as variáveis:

no linux:

export DATABASE_NAME="pessoas_db"
export DATABASE_HOST="zzzzz"
export DATABASE_USER="yyyyy"
export DATABASE_PASSWORD="KKKKK"

para visualizar:

echo $DATABASE_USER

'''