# Module 1 Project Report — RAG-Powered AI App

## Project Title
RAG Assistant — A Retrieval-Augmented Generation application for document-backed Q&A.

## Objective
Build an application that answers user queries using retrieval from a vector store and an LLM generator, with clear source citations and minimal hallucination.

## Architecture
- Ingestion: PDF/HTML/text -> cleaned text -> chunking (300-500 tokens, 20-30% overlap)
- Embedding: openai/sentence-transformers -> vectors
- Vector DB: FAISS / Milvus / Pinecone
- Retrieval: similarity search (top_k=5) + reranking
- LLM prompt: system + retrieved context + user query
- Frontend: Streamlit (or simple Flask)

## Implementation Summary
- Provided a Streamlit app skeleton (app.py) that demonstrates:
  - document upload
  - chunking & embeddings (placeholder)
  - similarity search (placeholder)
  - generate answer using LLM (placeholder)
- Logging: suggestions to store queries and responses for evaluation.

## Evaluation
- Precision@k on a 50-question test set
- Hallucination checks: verify claims against source excerpts
- Latency: measure retrieval + generation time (target 2-4s for dev)

## Deliverables
- Source code (this folder)
- README + run instructions
- Demo script (in root)

