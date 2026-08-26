# RAG with pgvector

A RAG pipeline that chunks a document, embeds the chunks with OpenAI, stores them in PostgreSQL using `pgvector` extension, and answers questions using only the data in the database.

## How it works

1. **Chunk** the document
2. **Embed** each chunk with OpenAI
3. **Store** chunks and embeddings in Postgres `pgvector`
4. **Retrieve** the closest chunks by cosine distance
5. **Generate** an answer using only those chunks

## I used these stacks:
- Python 3.12
- Postgres/pgvector
- OpenAI API
  - Embedding: `text-embedding-3-small`
  - Generation: `gpt-5.6`

## Instruction:

1. Clone the repo

2. Create virtual environment:

`python -m venv <name>`

3. Install dependencies

`pip install -r requirements.txt`

4. Start Postgres + pgvector with Docker:

```bash
docker run --name pg-vector \
   -e POSTGRES_USER=<user_name> \
   -e POSTGRES_PASSWORD=<your_password> \
   -e POSTGRES_DB=<db_name> \
   -p 5432:5432 \
   -d pgvector/pgvector:pg16
```
5. Create tables

```bash 
psql -h localhost -U <user_name> -d <db_name> -f schema.sql
```

6. Create `.env` file(see `.env.example`)

7. Ingest a document
```bash
python main.py --ingest
```
8. Run the API
```bash
uvicorn api:app --reload
```
Then open http://127.0.0.1:8000/docs

### Or with Docker
Skip steps 2, 3 and 8:
```bash
docker build -t rag-app .
docker run -p 8000:8000 --env-file .env rag-app
```
