import json
from rag import build_service
from evals import Judge
import os
from openai import OpenAI
from rag.helper import request_cost

s = build_service()
client = OpenAI()
eval = Judge(os.getenv("MODEL_GEN"), client)
limit = 3
threshold = 0.7
candidate_limit = 10
price_per_million = 0.02
price_per_million_input = 4.0
price_per_million_output = 20.0

with open("evals/eval_set.jsonl") as file:
    passed = 0
    total = 0
    faithful = 0
    for line in file:
        item = json.loads(line)
        answer, selected_chunks, embedding_usage, generation_usage, ranking_usage = s.answer(item["question"], limit, threshold, candidate_limit)
        final_cost = request_cost(embedding_usage, generation_usage, ranking_usage)
        judge_result = eval.judge_model(item["question"], answer, s.make_str(selected_chunks))
        total += 1
        if item["must_contain"].lower() in answer.lower():
            passed += 1
        if judge_result.faithful:
            faithful += 1
        print(f"{item['question']}, | contains: {item['must_contain'].lower() in answer.lower()}, | faithful: {judge_result.faithful}, | cost_usd: {final_cost:.8f}")
    print(f"must_contain: {passed}/{total}  faithful: {faithful}/{total}")
