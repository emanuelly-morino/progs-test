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
    email: Mapped[Optional[str]] # optional and without length limit
    telefone: Mapped[str] 

    # reverse list of celulares
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

# sqlite
engine = create_engine("sqlite:///person.db")# , echo=True) 

# mysql / mariadb
# pip install sqlalchemy pymysql
# engine = create_engine('mysql+pymysql://user:password@localhost:3306/mydatabase', echo=True)

# oracle
# pip install sqlalchemy oracledb
# engine = create_engine('oracle+oracledb://user:password@localhost:1521/?service_name=xe', echo=True)

# db2
# pip install sqlalchemy ibm_db_sa
# engine = create_engine('db2+ibm_db://user:password@localhost:50000/mydatabase', echo=True)

# postgresql
# engine = create_engine('postgresql+psycopg2://user:password@localhost/mydatabase', echo=True)

# ms sql server
# pip install sqlalchemy pyodbc
# engine = create_engine('mssql+pyodbc://user:password@localhost/mydatabase?driver=ODBC+Driver+17+for+SQL+Server', echo=True)

# cria a base de dados, se não houver
Base.metadata.create_all(engine)

# inicia uma sessão
with Session(engine) as session:

    # create a new Pessoa object
    alguem = Pessoa(nome = "Joao da Silva", 
                    email = "josilva@gmail.com", 
                    telefone = "47 9 9234 1324")

    # add the object to the session, to be persisted 
    session.add(alguem)

    # persist the object to the database
    session.commit()

    # show the object
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