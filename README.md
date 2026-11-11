# RAG with pgvector

A RAG pipeline that chunks a document, embeds the chunks with OpenAI, stores them in PostgreSQL using `pgvector` extension, and answers questions using only the data in the database.

## How it works

1. **Chunk** the document
2. **Embed** each chunk with OpenAI
3. **Store** chunks and embeddings in Postgres `pgvector`
4. **Retrieve** the 10 closest chunks by cosine distance
5. **Rerank** them with the model and keep the best 3
6. **Generate** an answer using only those chunks, with citation like [1]

## Two ways to ask 
- `POST /ask` - always searches the user's words once, reranks, then answers.
- `POST /agent` -  agentic RAG: the model decides to search, rewrites the question for a better search query, and can search several times.

## Evaluation
I test the answers with a small eval set (`evals/eval_set.jsonl`): questions with a word the answer must contain.

Each answer is checked two ways:
- **must_contain**: Does the answer include the key fact I expected?
- **faithful**: A second model reads the answer and the source chunck, and checks that answer only says things the chunks actually say.

Result: `must_contain:4/4, faithful: 4/4`

Run it:
```bash
python -m evals.run_eval
```
## Example

Request:
```bash
curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"question": "why won'\''t my laptop turn on?"}'
```

Response:
```json
{
  "answer": "If pressing the power button causes no lights, fan noise, or sound, the computer may not be receiving power. [1] Test the wall socket with another device. [1] ...",
  "cost": 0.0111
}
```
## I used these stacks:
- Python 3.13
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
