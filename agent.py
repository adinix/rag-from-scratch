from rag import build_service
from dotenv import load_dotenv
from openai import OpenAI
import os
import json

load_dotenv()

client = OpenAI()
s = build_service()

threshold = 0.7
candidate_limit = 10
  

def search_documents(question):
    chunks, embedding_usage = s.embed_quest(question, candidate_limit, threshold)
    if chunks:
        return s.make_str(chunks)
    return "No relevant documents found."

tools = [
    {
        "type": "function",
        "name": "search_documents",
        "description": "search the computer troubleshooting guide for passages relevant to a query. Use it for questiuons about computer problems",
        "parameters": {
            "type": "object",
            "properties": {
                "question": {
                    "type": "string",
                    "description": "a short search query about one topic"
                },
            },
            "required": ["question"],
        },
    }
]


def ask_agent(question):
    input_list = [
        {"role": "developer", "content": "Answer only using result from search_documents. Always search before answering a question about computers. If the search finds nothing, say you dont know. cite sources like [1]."}, 
        {"role": "user", "content": question}
    ]

    for round in range(5):
        response = client.responses.create(
            model = os.getenv("MODEL_GEN"),
            input = input_list,
            tools = tools
        )
        
        input_list += response.output
        
        called = False
        for item in response.output:
            if item.type == "function_call":
                called = True
                args = json.loads(item.arguments)
                if item.name == "search_documents":
                    result = search_documents(**args)
                else:
                    result = f"Unknown function {item.name}"
                input_list.append(
                    {
                        "type": "function_call_output",
                        "call_id": item.call_id,
                        "output": result
                    }
                )
                
        if not called:
            return response.output_text
    return "Sorry, I couldn't find an answer."
