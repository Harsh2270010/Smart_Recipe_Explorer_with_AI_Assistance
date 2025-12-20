from pydantic import BaseModel

class RecipeCreate(BaseModel):
    name: str
    cuisine: str
    ingredients: str
    cooking_time: int
    instructions: str

class RecipeResponse(RecipeCreate):
    id: int

    class Config:
        from_attributes = True
