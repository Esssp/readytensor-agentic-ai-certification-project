# Module 2 Project Report — Multi-Agent System

## Project Title
Agentic Research Assistant — Planner + Retriever + Reader + Verifier

## Objective
Build a system of specialized agents that coordinate to solve multi-step tasks (e.g., research query -> evidence collection -> summarization -> verification).

## Architecture
- Planner agent: decomposes user request into tasks
- Retriever agent: searches vector DB / web for evidence
- Reader/Summarizer: extracts facts and creates summary
- Verifier: cross-checks claims against sources and marks confidence
- Orchestrator: manages message passing and retries

## Implementation Summary
- Provided lightweight orchestrator (orchestrator.py) that runs agents as Python functions for a dev demo.
- Each agent returns structured JSON: { "result": ..., "sources": [...], "confidence": 0.0 }

## Evaluation
- Handoff success rate
- Correctness vs single-agent baseline
- Latency & cost analysis

## Deliverables
- Code samples (this folder)
- Demo script in root
