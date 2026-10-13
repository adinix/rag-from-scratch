from rag import Chunker, PgVector, Generator, Embedding, Service, Reranker
from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

load_dotenv()

size = 500
overlap_size = 50

def build_service():
    client = OpenAI()
    pg_vec = PgVector(os.getenv("HOST"), os.getenv("PORT"), os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASS"))
    embedder = Embedding(os.getenv("MODEL"), client)
    chunker = Chunker(size, overlap_size)
    generator = Generator(os.getenv("MODEL_GEN"), client)
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("rag")
    reranker = Reranker(os.getenv("MODEL_GEN"), client)
    return Service(embedder, pg_vec, chunker, generator, logger, reranker)
