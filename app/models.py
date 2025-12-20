from sqlalchemy import Column, Integer, String, Text
from app.database import Base


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cuisine = Column(String)
    ingredients = Column(Text)
    cooking_time = Column(Integer)
    instructions = Column(Text)
