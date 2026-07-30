from a_classes import *
from e_servicos import *

# criar objeto de serviços
serv = Servico()

# teste de listagem de dados
print("*** listando pessoas")
pessoas = serv.retornar_pessoas()
for p in pessoas: print(p)

# quantas pessoas existem no cadastro?
q = serv.retorna_quantidade_registros(TABELA_PESSOAS)
print(f"Existe(m) {q} pessoa(s) na tabela")

# teste de inclusão
print("*** incluindo pessoa")
serv.incluir_pessoa(Pessoa(0, "Tiago Hill", "tihi@gmail.com"))

# listando novamente para ver se o Tiago entrou
print("*** listando pessoas")
pessoas = serv.retornar_pessoas()
for p in pessoas: print(p)

# quantas pessoas existem no cadastro?
q = serv.retorna_quantidade_registros(TABELA_PESSOAS)
print(f"Existe(m) {q} pessoa(s) na tabela")

# removendo o Tiago
print("*** removendo pessoa")
serv.remover_pessoa_via_email("tihi@gmail.com")
   
# listando novamente para ver se o Tiago entrou
print("*** listando pessoas")
pessoas = serv.retornar_pessoas()
for p in pessoas: print(p)