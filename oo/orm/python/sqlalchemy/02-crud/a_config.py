# reference: 
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html

from typing import List
from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import select

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# configura o mecanismo de armazenamento
# engine = create_engine("sqlite://", echo=True) # em memória
engine = create_engine("sqlite:///person.db", echo=True) # sqlite