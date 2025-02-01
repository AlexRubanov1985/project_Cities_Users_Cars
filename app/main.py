from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from seed import seed_db
from database import SessionLocal, engine
from models import City, Car

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/cars/{city_name}")
def get_cars_by_city(city_name: str, db: Session = Depends(get_db)):
    city = db.query(City).filter(City.name == city_name).first()
    if not city:
        return {"error": "City not found"}
    return {"city": city_name, "cars": [{"id": car.id, "model": car.model} for car in city.cars]}


@app.get("/cities")
def get_all_cities(db: Session = Depends(get_db)):
    cities = db.query(City).all()
    print(f"Найдено {len(cities)} городов")  # Логируем количество городов
    return {"cities": [{"id": city.id, "name": city.name} for city in cities]}

@app.on_event("startup")
def startup_event():
  seed_db()