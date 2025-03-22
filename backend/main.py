#ChatGPT generated file as part of project setup
from fastapi import FastAPI
from app.db.progress_db import init_db, log_progress
from app.agents.tutor_agent import generate_lesson
from app.memory.chroma_manager import save_lesson_to_memory
from datetime import datetime

app = FastAPI()

@app.on_event("startup")
def setup():
    init_db()
    
@app.get("/lesson/{topic}")
def get_lesson(topic: str):
    lesson = generate_lesson(topic)
    save_lesson_to_memory(topic, lesson)
    return {"topic": topic, "lesson": lesson}

@app.post("/log_progress/")
def update_progress(topic: str, score: int, notes: str):
    today = datetime.now().strftime("%Y-%m-%d")
    log_progress(topic, today, score, notes)
    return {"status": "Progress logged"}