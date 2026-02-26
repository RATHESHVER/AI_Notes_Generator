AI Notes Generator using Generative AI
----------------------------------------
Overview

AI Notes Generator is a Generative AI-based application that converts academic PDF documents into structured, exam-oriented study notes and important questions. The system processes large documents using a chunking strategy and applies prompt engineering to generate clear and concise outputs. The project runs with a locally hosted Large Language Model using Ollama, enabling offline AI inference without relying on external APIs.

Features

Upload academic PDF files

Automatic text extraction from documents

Chunking mechanism for handling large PDFs

Exam-oriented notes generation

Key points and important question creation

Difficulty level selection

Subject-based prompting

Offline LLM inference using Ollama

Download generated notes

Tech Stack

Programming Language: Python
Framework: Streamlit
Generative AI: LLaMA (via Ollama)
Libraries: PyPDF2, Requests
Concepts Used: Generative AI, Prompt Engineering, NLP, Document Processing

System Architecture

The application follows a structured workflow:

User uploads a PDF through the Streamlit interface.

PyPDF2 extracts text from each page of the document.

The extracted text is split into smaller chunks to handle context limitations.

Each chunk is processed by a locally hosted LLaMA model through Ollama using structured prompts.

Generated outputs are combined and displayed as exam-oriented notes.
