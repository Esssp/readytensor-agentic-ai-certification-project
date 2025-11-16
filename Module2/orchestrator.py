"""
Simple orchestrator that runs agent functions sequentially.
This is a dev/demo scaffold — replace with real async queues / services for production.
"""
import json
from typing import Dict, Any, List

def planner(user_request: str) -> Dict[str, Any]:
    # Decompose into subtasks (very naive)
    tasks = [
        {"task": "retrieve", "query": user_request},
        {"task": "summarize", "query": user_request},
        {"task": "verify", "query": user_request}
    ]
    return {"tasks": tasks}

def retriever(query: str) -> Dict[str, Any]:
    # Placeholder retrieval
    hits = [
        {"id": "doc1#ch0", "text": "Evidence snippet 1"},
        {"id": "doc2#ch3", "text": "Evidence snippet 2"}
    ]
    return {"hits": hits, "count": len(hits)}

def reader(hits: List[Dict]) -> Dict[str, Any]:
    # Create a short summary
    summary = " ".join([h["text"] for h in hits])
    return {"summary": summary}

def verifier(summary: str, hits: List[Dict]) -> Dict[str, Any]:
    # Very naive verification: mark high confidence if there are at least 2 sources
    confidence = 0.9 if len(hits) >= 2 else 0.5
    return {"confidence": confidence, "issues": []}

def run(user_request: str):
    plan = planner(user_request)
    print("Plan:", json.dumps(plan, indent=2))
    # run retrieval
    ret = retriever(user_request)
    print("Retriever:", ret)
    # run reader
    read = reader(ret["hits"])
    print("Reader summary:", read["summary"])
    # run verifier
    ver = verifier(read["summary"], ret["hits"])
    print("Verifier:", ver)

if __name__ == "__main__":
    run("Summarize recent papers about RAG architectures for education")
