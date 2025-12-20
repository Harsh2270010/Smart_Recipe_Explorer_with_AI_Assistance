# 🍲 Smart Recipe Explorer with AI Assistance

A FastAPI-based backend application for managing recipes, searching/filtering them, and enhancing user experience with free Generative AI integration via Groq API.

---

## ✨ Features

- **Recipe Management**
  - Create, read, update, and delete recipes
  - Store ingredients, steps, cuisine, difficulty, tags, and more
  - SQLite database for persistence

- **Search & Filtering**
  - Keyword search across recipe titles, cuisines, and descriptions
  - Semantic search 
  - Filter recipes by cuisine, difficulty, or tags

- **AI Integration**
  - Generate recipe titles (`/ai/suggest-title`)
  - Create semantic embeddings (`/ai/embed`)
  - Powered by Grok API 

- **Interactive API Docs**
  - Swagger UI available at `/docs`
  - ReDoc available at `/redoc`

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite with SQLModel
- **AI Services**: Groq API
- **Environment Management**: Python `dotenv`
- **Server**: Uvicorn

---




