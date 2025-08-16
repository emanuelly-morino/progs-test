from a_config import *
from b_model import *

# cria a base de dados, se não houver
Base.metadata.create_all(engine)