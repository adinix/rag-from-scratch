from rag import Chunker, PgVector, Generator, Embedding, Service
import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

load_dotenv()

title = "Computer Troubleshooting Guide"
source = "computer_help.md"
size = 500
overlap_size = 50
limit = 3
threshold = 0.7

with open("data/computer_help.md") as f:
    text = f.read()

client = OpenAI()
pg_vec = PgVector(os.getenv("HOST"), os.getenv("PORT"), os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASS"))
embedder = Embedding(os.getenv("MODEL"), client)
chunker = Chunker(size, overlap_size)
generator = Generator(os.getenv("MODEL_GEN"), client)
s = Service(embedder, pg_vec, chunker, generator)

parser = argparse.ArgumentParser()
parser.add_argument("--ingest", action="store_true")
args = parser.parse_args()

if args.ingest:
    doc_id = s.add_doc(title, source)
    s.ingest(doc_id, text)
    print("Document ingested.")
else:
    question = input("Enter your question: ")
    print(s.answer(question, limit, threshold))
