import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def enhance_recipe(recipe_text: str) -> str:
    if not recipe_text or not recipe_text.strip():
        raise ValueError("Recipe text cannot be empty")

    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=300
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a professional chef and food blogger."),
        ("user", "Enhance this recipe with better steps, tips, and variations:\n{recipe}")
    ])

    chain = prompt | llm
    response = chain.invoke({"recipe": recipe_text})

    return response.content.strip()
