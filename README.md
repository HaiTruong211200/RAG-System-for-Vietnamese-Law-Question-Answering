# **Overview**
This project implements a Retrieval-Augmented Generation (RAG) system designed to answer Vietnamese legal questions related to traffic laws. It leverages the power of large language models (LLMs) in combination with an efficient hybrid retrieval mechanism, enabling the system to provide accurate, explainable, and citation-backed answers grounded in legal documents.

# **Data Collection**
The data used in this project consists of Vietnamese legal documents related to road traffic laws, sourced from official government portals and legal repositories. These documents provide the foundation for retrieval-augmented answers and are carefully processed to ensure high quality and relevance.

## **Source of legal text**
- Luật Giao thông đường bộ(2008)
- Luật Bảo đảm trật tự an toàn giao thông đường bộ(2024)
- Nghị định xử phạt vi phạm hành chính lĩnh vực giao thông đường bộ(2019)

# **System Component**
The system is composed of several interconnected modules, each responsible for a critical step in the RAG pipeline. The overall goal is to take a natural language legal question and return a grounded answer with supporting legal context.

![image](https://github.com/user-attachments/assets/e4e46001-ae1c-4e48-90d8-b4d0c67d2ad7)

## **1. User Input Interface**
Input: User query + chat history (context-aware).

Purpose: Support conversational multi-turn interaction.

## **2. Query Rewriting**
A lightweight LLM or rule-based module rewrites the user query based on chat history to make it clearer and more focused for retrieval.

Output: Rewritten query that improves retrieval precision.

## **3. LLM with Tools**
Acts as the main orchestrator.

Uses Tool Calling to invoke the retrieval module when it requires external knowledge.

If the LLM already knows the answer it provides a Direct Answer.

## **4. Retrieval Module**
Combines Hybrid Retrieval:

Semantic Search using dense vector similarity (Sentence Transformers).

Keyword Search using sparse methods (BM25).

Results from both methods are passed to a Reranker to improve final relevance before giving them to the LLM.

Output: Top-k legal text chunks relevant to the user’s query.

## **5. Document Store & Chunking**
Legal documents are semantically chunked into articles.

Chunks are stored with metadata in a vector database (Chroma).

This enables fast hybrid search on both semantic and keyword-based queries.

## **6. LLM Answer Generator**
The main LLM generates a natural language response using:

The rewritten query

Retrieved legal chunks as context

Outputs an answer with source citations
