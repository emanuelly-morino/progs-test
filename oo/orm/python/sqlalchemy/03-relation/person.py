# reference: 
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

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

    celulares: Mapped[List["Celular"]] = relationship(back_populates="pessoa", 
                                                cascade="all, delete-orphan")
    
    def __repr__(self) -> str:
        return f'''
        Pessoa: id={self.id}, nome={self.nome}, 
        email={self.email},
        telefone={self.telefone}
        '''

class Celular(Base):
    __tablename__ = "celular"
    id: Mapped[int] = mapped_column(primary_key=True)
    marca: Mapped[str]
    modelo: Mapped[str]
    pessoa_id: Mapped[int] = mapped_column(ForeignKey("pessoa.id"))
    pessoa: Mapped["Pessoa"] = relationship(back_populates="celulares")

    def __repr__(self) -> str:
        return f'''
        Marca: {self.marca}, modelo: {self.modelo},
        proprietário: {self.pessoa}
        '''

# configura o mecanismo de armazenamento
# engine = create_engine("sqlite://", echo=True) # em memória
engine = create_engine("sqlite:///person.db")# , echo=True) # sqlite

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

    # cria um celular
    cel = Celular(marca = "Xiaomi",
                  modelo = "A2 lite",
                  pessoa = alguem)
    
    session.add(cel)
    session.commit()

    # cria outro celular
    cel2 = Celular(marca = "Samsung",
                  modelo = "S5",
                  pessoa = alguem)
    
    session.add(cel2)
    session.commit()

    # mostra os celulares da pessoa
    print("celulares de", alguem.nome,":")
    for c in alguem.celulares:
        print(c)

