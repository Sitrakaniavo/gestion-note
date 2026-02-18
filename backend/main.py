from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Configuration CORS pour autoriser le frontend Vite
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Port par défaut de Vite
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modèle de donnée pour une note
class Note(BaseModel):
    id: int
    title: str
    content: str

# Simulation d'une base de données
db_notes = [
    {"id": 1, "title": "Ma première note", "content": "Contenu de test pour mon app sur Kali."}
]

@app.get("/api/notes", response_model=List[Note])
async def get_notes():
    return db_notes

@app.post("/api/notes")
async def add_note(note: Note):
    db_notes.append(note.dict())
    return {"status": "success"}