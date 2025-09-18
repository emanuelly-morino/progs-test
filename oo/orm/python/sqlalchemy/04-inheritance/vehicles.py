from sqlalchemy import String, Integer, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Veiculo(Base):
    __tablename__ = 'veiculo'
    id: Mapped[int] = mapped_column(primary_key=True)

    # the value can be None (NULL in the database) or a string
    placa: Mapped[str | None] = mapped_column(String, nullable=True)

    cor: Mapped[str] = mapped_column(String, nullable=False)
    marca: Mapped[str] = mapped_column(String, nullable=False)
    modelo: Mapped[str] = mapped_column(String, nullable=False)

    # field to distinguish the type of vehicle (inheritance)
    type: Mapped[str] = mapped_column(String, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'veiculo',
        'polymorphic_on': type
    }

    def __str__(self):
        s = f'{self.cor}, {self.marca}, {self.modelo}'
        if self.placa:
            s += self.placa
        return s

class Carro(Veiculo):
    __tablename__ = 'carro'
    id: Mapped[int] = mapped_column(ForeignKey("veiculo.id"),
                                    primary_key=True)
    lugares: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'carro',
    }

    def __str__(self):
        s = super().__str__()
        s += f', {self.lugares}'
        return s

class Moto(Veiculo):
    __tablename__ = 'moto'
    id: Mapped[int] = mapped_column(ForeignKey("veiculo.id"),
                                    primary_key=True)
    cilindradas: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'moto',
    }

    def __str__(self):
        s = super().__str__()
        s += f', {self.cilindradas}'
        return s

engine = create_engine('sqlite:///vehicles.db')
Base.metadata.create_all(engine)

with Session(engine) as session:
    v1 = Carro(placa="FXX 1234", cor="azul", marca="ford", modelo="ka", lugares=5)

    # the motocycle does not have a license plate yet
    v2 = Moto(cor="preta", marca="honda", modelo="biz", cilindradas=150)

    session.add_all([v1, v2])
    session.commit()