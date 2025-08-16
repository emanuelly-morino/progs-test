from a_config import *

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