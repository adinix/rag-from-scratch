from rag import Chunker, PgVector, Generator, Embedding, Service
import os
from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI
from models import QuestionIn

load_dotenv()

size = 500
overlap_size = 50
limit = 3
threshold = 0.7

client = OpenAI()
pg_vec = PgVector(os.getenv("HOST"), os.getenv("PORT"), os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASS"))
embedder = Embedding(os.getenv("MODEL"), client)
chunker = Chunker(size, overlap_size)
generator = Generator(os.getenv("MODEL_GEN"), client)
s = Service(embedder, pg_vec, chunker, generator)

app = FastAPI()

@app.post("/ask")
def ask(payload: QuestionIn):
    return {"answer": s.answer(payload.question, limit, threshold)}
