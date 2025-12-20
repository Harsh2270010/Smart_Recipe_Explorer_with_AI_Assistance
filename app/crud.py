from sqlalchemy.orm import Session
from app import models, schemas

def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    db_recipe = models.Recipe(**recipe.dict())
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def search_recipes(db: Session, query: str):
    return db.query(models.Recipe).filter(
        models.Recipe.name.contains(query)
    ).all()
