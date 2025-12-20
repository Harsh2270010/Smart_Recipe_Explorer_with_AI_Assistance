# 🍲 Smart Recipe Explorer with AI Assistance

A FastAPI-based backend application for managing recipes, searching/filtering them, and enhancing user experience with free Generative AI integration via Hugging Face.

---

## ✨ Features

- **Recipe Management**
  - Create, read, update, and delete recipes
  - Store ingredients, steps, cuisine, difficulty, tags, and more
  - SQLite database for persistence

- **Search & Filtering**
  - Keyword search across recipe titles, cuisines, and descriptions
  - Semantic search using embeddings (`sentence-transformers/all-MiniLM-L6-v2`)
  - Filter recipes by cuisine, difficulty, or tags

- **AI Integration**
  - Generate recipe titles (`/ai/suggest-title`)
  - Create semantic embeddings (`/ai/embed`)
  - Powered by Hugging Face Inference API (via `https://router.huggingface.co`)

- **Interactive API Docs**
  - Swagger UI available at `/docs`
  - ReDoc available at `/redoc`

---

## 🛠️ Tech Stack

- **Backend Framework**: FastAPI
- **Database**: SQLite with SQLModel
- **AI Services**: Hugging Face Inference API
- **Environment Management**: Python `dotenv`
- **Server**: Uvicorn

---



