TOKENS_PER_MILLION = 1_000_000
PRICE_PER_MILLION = 0.02
PRICE_PER_MILLION_INPUT = 4.0
PRICE_PER_MILLION_OUTPUT = 20.0


def cost(tokens, PRICE_PER_MILLION):
    return (tokens / TOKENS_PER_MILLION) * PRICE_PER_MILLION

def request_cost(embedding_usage, generation_usage, ranked_usage):
    embed_cost = cost(embedding_usage.prompt_tokens, PRICE_PER_MILLION)
    generation_cost = 0.0
    ranking_cost = 0.0
    if generation_usage is not None:
        input_cost = cost(generation_usage.input_tokens, PRICE_PER_MILLION_INPUT)
        output_cost = cost(generation_usage.output_tokens, PRICE_PER_MILLION_OUTPUT)
        generation_cost = input_cost + output_cost
    if ranked_usage is not None:
        input_cost = cost(ranked_usage.input_tokens, PRICE_PER_MILLION_INPUT) 
        output_cost = cost(ranked_usage.output_tokens, PRICE_PER_MILLION_OUTPUT)
        ranking_cost = input_cost + output_cost
    final_cost = embed_cost + generation_cost + ranking_cost
    return final_cost
