from a_classes import *
from e_servicos import *

# criar objeto de serviços
serv = Servico()

# quantos celulares existem no cadastro?
q = serv.retorna_quantidade_registros(TABELA_CELULARES)
print(f"Existe(m) {q} celular(es) na tabela")
 
# listando os celulares
print("*** listando celulares")
celulares = serv.retornar_celulares()
for c in celulares: print(c)