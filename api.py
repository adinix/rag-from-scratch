from rag import build_service
from fastapi import FastAPI, HTTPException
from models import QuestionIn
from openai import OpenAIError
from rag.helper import request_cost
from time import perf_counter

limit = 3
threshold = 0.7
candidate_limit = 10

s = build_service()

app = FastAPI()

@app.post("/ask")
def ask(payload: QuestionIn):
    try:
        start = perf_counter()
        answer, selected_chunks, embedding_usage, generation_usage, ranking_usage = s.answer(payload.question, limit, threshold, candidate_limit)
        end = perf_counter()
    except OpenAIError:
        raise HTTPException(status_code=503, detail="AI service unavailable, try again")
    
    final_cost = request_cost(embedding_usage, generation_usage, ranking_usage)
    elapsed = end - start
    generation_input_tokens = 0
    generation_output_tokens = 0
    if generation_usage is not None:
        generation_input_tokens = generation_usage.input_tokens
        generation_output_tokens = generation_usage.output_tokens
    ranking_input_tokens = 0
    ranking_output_tokens = 0
    if ranking_usage is not None:
        ranking_input_tokens = ranking_usage.input_tokens
        ranking_output_tokens = ranking_usage.output_tokens
    for chunk in selected_chunks:
        s.logger.info(f"chunk_index: {chunk[1]}, documnet_id: {chunk[2]}, distance: {chunk[3]:.3f}")
    s.logger.info(
        f"{payload.question}, cost:{final_cost:.8f}, chunks: {len(selected_chunks)}, elapsed_seconds: {elapsed:.3f}, embedding_tokens: {embedding_usage.prompt_tokens}, generation_input_tokens: {generation_input_tokens}, generation_output_tokens: {generation_output_tokens}, reranking_input_tokens: {ranking_input_tokens}, reranking_output_tokens: {ranking_output_tokens}"
        )
    return {"answer":answer, "cost": final_cost}
