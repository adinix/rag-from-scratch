import argparse
from rag import build_service

title = "Computer Troubleshooting Guide"
source = "computer_help.md"
limit = 3
candidate_limit = 10
threshold = 0.7

s = build_service()
with open("data/computer_help.md") as f:
    text = f.read()

parser = argparse.ArgumentParser()
parser.add_argument("--ingest", action="store_true")
args = parser.parse_args()

if args.ingest:
    doc_id = s.add_doc(title, source)
    s.ingest(doc_id, text)
    s.logger.info(f"Document ingested, document_id: {doc_id}")
else:
    question = input("Enter your question: ")
    print(s.answer(question, limit, threshold, candidate_limit))
