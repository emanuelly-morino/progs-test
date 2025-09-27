from flask import Flask, request, render_template, redirect, url_for
from pony.orm import Database, Required, Optional, Set, db_session

app = Flask(__name__)

# ----------------------
# DATABASE CONFIGURATION
# ----------------------
db = Database()
db.bind(provider='sqlite', filename='garage.db', create_db=True)

# ----------------------
# MODELS
# ----------------------
class Person(db.Entity):
    name = Required(str)
    email = Required(str)
    telephone = Required(str)
    cars = Set("Car")  # one person can own multiple cars


class Car(db.Entity):
    maker = Required(str)
    model = Required(str)
    year = Required(int)
    owner = Optional(Person)  # car may or may not have an owner

# Create tables
db.generate_mapping(create_tables=True)


# HOME
@app.route("/")
def home():
    return render_template("home.html")

# ----------------------
# ROUTES: PERSON
# ----------------------
@app.route("/persons")
@db_session
def list_persons():
    persons = Person.select()
    return render_template("person_list.html", persons=persons)


@app.route("/person/create", methods=["GET", "POST"])
@db_session
def create_person():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        telephone = request.form["telephone"]
        Person(name=name, email=email, telephone=telephone)
        return redirect(url_for("list_persons"))
    return render_template("person_new.html")


@app.route("/person/update/<int:person_id>", methods=["GET", "POST"])
@db_session
def update_person(person_id):
    person = Person.get(id=person_id)
    if not person:
        return redirect(url_for("list_persons"))

    if request.method == "POST":
        person.name = request.form["name"]
        person.email = request.form["email"]
        person.telephone = request.form["telephone"]
        return redirect(url_for("list_persons"))

    return render_template("person_edit.html", person=person)


@app.route("/person/delete/<int:person_id>")
@db_session
def delete_person(person_id):
    person = Person.get(id=person_id)
    if person:
        person.delete()
    return redirect(url_for("list_persons"))


# ----------------------
# ROUTES: CAR
# ----------------------
@app.route("/cars")
@db_session
def list_cars():
    cars = Car.select()
    return render_template("car_list.html", cars=cars)


@app.route("/car/create", methods=["GET", "POST"])
@db_session
def create_car():
    persons = Person.select()
    if request.method == "POST":
        maker = request.form["maker"]
        model = request.form["model"]
        year = int(request.form["year"])
        owner_id = request.form.get("owner_id")

        owner = Person.get(id=int(owner_id)) if owner_id else None
        Car(maker=maker, model=model, year=year, owner=owner)
        return redirect(url_for("list_cars"))

    return render_template("car_new.html", persons=persons)


@app.route("/car/update/<int:car_id>", methods=["GET", "POST"])
@db_session
def update_car(car_id):
    car = Car.get(id=car_id)
    if not car:
        return redirect(url_for("list_cars"))

    persons = Person.select()

    if request.method == "POST":
        car.maker = request.form["maker"]
        car.model = request.form["model"]
        car.year = int(request.form["year"])
        owner_id = request.form.get("owner_id")
        car.owner = Person.get(id=int(owner_id)) if owner_id else None
        return redirect(url_for("list_cars"))

    return render_template("car_edit.html", car=car, persons=persons)


@app.route("/car/delete/<int:car_id>")
@db_session
def delete_car(car_id):
    car = Car.get(id=car_id)
    if car:
        car.delete()
    return redirect(url_for("list_cars"))


# ----------------------
# START APP
# ----------------------
app.run(debug=True, host="0.0.0.0", port=80)
