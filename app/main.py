# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session

# from app.database import SessionLocal, engine
# from app import models, schemas, crud
# from app.ai import enhance_recipe

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI(title="Smart Recipe AI")

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/recipes", response_model=schemas.RecipeResponse)
# def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
#     return crud.create_recipe(db, recipe)

# @app.get("/recipes/search")
# def search(query: str, db: Session = Depends(get_db)):
#     return crud.search_recipes(db, query)

# @app.post("/recipes/ai-enhance")
# def ai_enhance(recipe_text: str):
#     return {"enhanced_recipe": enhance_recipe(recipe_text)}

from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from pathlib import Path

from app.database import SessionLocal, engine
from app import models, schemas, crud
from app.ai import enhance_recipe

# -------------------- DB SETUP --------------------
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Recipe AI")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------- FRONTEND SETUP --------------------
BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
def serve_frontend():
    return (FRONTEND_DIR / "index.html").read_text(encoding="utf-8")

# -------------------- RECIPE APIs --------------------
@app.post("/recipes", response_model=schemas.RecipeResponse)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe)

@app.get("/recipes/search")
def search(query: str, db: Session = Depends(get_db)):
    return crud.search_recipes(db, query)

# -------------------- AI API --------------------
@app.post("/recipes/ai-enhance")
def ai_enhance(recipe_text: str):
    return {"enhanced_recipe": enhance_recipe(recipe_text)}
