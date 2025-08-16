# reference: 
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

'''
upgrading sqlalchemy:
$ pip3 install sqlalchemy --upgrade

check:
$ pip3 show sqlalchemy

'''

from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class Base(DeclarativeBase):
    pass

class Pessoa(Base):
    __tablename__ = "pessoa"
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(250))
    email: Mapped[Optional[str]] # opcional e sem tamanho definido
    telefone: Mapped[str] 
    
    def __repr__(self) -> str:
        return f'''
        Pessoa: id={self.id!r}, nome={self.nome!r}, 
        email={self.email!r},
        telefone={self.telefone}
        '''

# configura o mecanismo de armazenamento
# engine = create_engine("sqlite://", echo=True) # em memória
engine = create_engine("sqlite:///person.db", echo=True) # sqlite

# cria a base de dados, se não houver
Base.metadata.create_all(engine)

# inicia uma sessão
with Session(engine) as session:

    # cria um objeto
    alguem = Pessoa(nome = "Joao da Silva", 
                    email = "josilva@gmail.com", 
                    telefone = "47 9 9234 1324")

    # persiste 
    session.add(alguem)

    # confirma a gravação
    session.commit()

    # mostra as informações
    print(alguem)