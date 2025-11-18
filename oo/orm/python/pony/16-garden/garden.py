# https://docs.ponyorm.org/working_with_relationships.html

from pony.orm import *

db = Database()

class Planta(db.Entity):
    planta_id = PrimaryKey(int, auto=True)
    nome = Required(str)
    especie = Required(str)
    jardins = Set('PlantaNoJardim')
    
class Jardim(db.Entity):
    localizacao = Required(str)
    tamanho_em_metros_quadrados = Required(float)
    plantas = Set('PlantaNoJardim')
    
class PlantaNoJardim(db.Entity):
    planta = Required(Planta)
    jardim = Required(Jardim)
    quantidade = Required(int)
    PrimaryKey(planta, jardim)

db.bind(provider='sqlite', filename='jardim.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    # Criar algumas plantas
    rosa = Planta(nome='Rosa', especie='Rosa rubiginosa')
    girassol = Planta(nome='Girassol', especie='Helianthus annuus')
    tulipa = Planta(nome='Tulipa', especie='Tulipa gesneriana')
    margarida = Planta(nome='Margarida', especie='Bellis perennis')
    orquidea = Planta(nome='Orquídea', especie='Orchidaceae')
        
    # Criar tres jardins
    jardim1 = Jardim(localizacao='Quintal de Casa', tamanho_em_metros_quadrados=50.0)
    jardim2 = Jardim(localizacao='Parque Central', tamanho_em_metros_quadrados=200.0)
    jardim3 = Jardim(localizacao='Jardim Botânico', tamanho_em_metros_quadrados=500.0)
        
    # Adicionar plantas aos jardins
    PlantaNoJardim(planta=rosa, jardim=jardim1, quantidade=10)
    PlantaNoJardim(planta=girassol, jardim=jardim1, quantidade=5)
    PlantaNoJardim(planta=tulipa, jardim=jardim2, quantidade=15)
    PlantaNoJardim(planta=margarida, jardim=jardim2, quantidade=20)
    PlantaNoJardim(planta=orquidea, jardim=jardim3, quantidade=8)
    
    commit()