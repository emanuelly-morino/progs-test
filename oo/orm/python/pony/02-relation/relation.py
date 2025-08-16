# https://docs.ponyorm.org/working_with_relationships.html

from pony.orm import *

db = Database()

class Person(db.Entity):
    name = Required(str)
    cars = Set('Car')

class Car(db.Entity):
    make = Required(str) # fabricante
    model = Required(str)
    owner = Optional(Person)

db.bind(provider='sqlite', filename='person.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    p1 = Person(name='John')
    c1 = Car(make='Toyota', model='Camry')
    c2 = Car(make='Volksvagem', model='Fox')
    p1.cars.add(c1)
    p1.cars.add(c2)
    commit()

    # mostrar a pessoa
    print("pessoa:", p1.name)
    # mostrar os carros da pessoa
    print("carros:")
    for c in p1.cars:
        print("*", c.make, c.model)