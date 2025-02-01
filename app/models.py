from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base, engine


user_city = Table(
    "user_city",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("city_id", Integer, ForeignKey("cities.id"))
)

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    cars = relationship("Car", back_populates="city")
    users = relationship("User", secondary=user_city, back_populates="cities")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cities = relationship("City", secondary=user_city, back_populates="users")
    cars = relationship("Car", back_populates="owner")

class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    city_id = Column(Integer, ForeignKey("cities.id"))
    owner = relationship("User", back_populates="cars")
    city = relationship("City", back_populates="cars")

Base.metadata.create_all(bind=engine)
