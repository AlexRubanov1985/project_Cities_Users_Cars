from faker import Faker
from database import SessionLocal
from models import City, User, Car

def seed_db():
    fake = Faker()
    db = SessionLocal()
    for _ in range(5):
        city = City(name=fake.city())
        db.add(city)
        db.commit()
        db.refresh(city)
        for _ in range(3):
            user = User(name=fake.name())
            user.cities.append(city)
            db.add(user)
            db.commit()
            db.refresh(user)
            for _ in range(2):
                car = Car(model=fake.company(), owner=user, city=city)
                db.add(car)
                print(f"Добавлен город: {city.name}, id: {city.id}")
                print(f"Добавлен пользователь: {user.name}, id: {user.id}")
                print(f"Добавлена машина: {car.model},id:{car.id}")
    db.commit()
    db.close()

seed_db()