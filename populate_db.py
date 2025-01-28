from models import Car, db
from app import app

with app.app_context():
    cars = [
        Car(brand="Toyota", model="Corolla", color="Blue", year=2012, price=8500),
        Car(brand="Toyota", model="Avensis", color="Blue", year=2002, price=3200),
        Car(brand="BMW", model="x3", color="Grey", year=2008, price=6000),
        Car(brand="Audi", model="a4", color="White", year=2016, price=17000),
        Car(brand="Porsche", model="Taycan", color="Cement", year=2021, price=105000),
        Car(brand="Porsche", model="Panamera", color="Lime", year=2018, price=110000)

    ]

    db.session.add_all(cars)
    db.session.commit()
    print("Data added")