# Medical RAG Chatbot

<div align="center">

### AI-Powered Medical Question Answering using Retrieval-Augmented Generation (RAG)

The **Medical RAG Chatbot** is an AI-powered application that answers medical questions by retrieving relevant information from a medical knowledge base and generating accurate, context-aware responses using a Large Language Model (LLM).

### Live Demo

**Hugging Face Space:**
https://huggingface.co/spaces/Monishram99/Medical-Chatbot

</div>

---

# Overview

Medical RAG Chatbot is an end-to-end Retrieval-Augmented Generation (RAG) application that enables users to ask medical questions and receive context-aware answers from a medical reference document.

Instead of relying only on the knowledge of a Large Language Model, the application first retrieves the most relevant document chunks from a vector database using semantic search. These retrieved chunks are then provided to the LLM as context, ensuring more accurate and reliable responses while minimizing hallucinations.

The project combines modern Generative AI technologies including LangChain, Hugging Face Embeddings, Pinecone Vector Database, Groq Llama-3.3, and Gradio into a complete RAG pipeline.

---

# Features

* Medical PDF-based Question Answering
* Retrieval-Augmented Generation (RAG)
* Semantic Similarity Search
* Pinecone Vector Database
* Groq Llama-3.3-70B Versatile
* Fast AI Response Generation
* Interactive Gradio Interface
* Deployed on Hugging Face Spaces
* Secure API Key Management
* Modular and Scalable Architecture

---

# System Architecture

```text
                     Medical PDF
                          │
                          ▼
                  PDF Document Loader
                          │
                          ▼
         Recursive Character Text Splitter
                          │
                          ▼
      Hugging Face Sentence Transformer
                          │
                          ▼
           Vector Embedding Generation
                          │
                          ▼
           Pinecone Vector Database
                          │
                          ▼
          Semantic Similarity Retrieval
                          │
                          ▼
         Top-K Relevant Document Chunks
                          │
                          ▼
              Prompt Construction
                          │
                          ▼
        Groq Llama-3.3-70B Versatile
                          │
                          ▼
              AI Generated Response
```

---

# Technology Stack

| Category              | Technology                                            |
| --------------------- | ----------------------------------------------------- |
| Programming Language  | Python                                                |
| Framework             | LangChain                                             |
| Embedding Model       | Hugging Face Sentence Transformers (all-MiniLM-L6-v2) |
| Vector Database       | Pinecone                                              |
| Large Language Model  | Groq Llama-3.3-70B Versatile                          |
| User Interface        | Gradio                                                |
| Deployment            | Hugging Face Spaces                                   |
| Environment Variables | python-dotenv                                         |

---

# Project Workflow

### Step 1

Load the medical reference PDF.

↓

### Step 2

Split the document into smaller overlapping text chunks.

↓

### Step 3

Generate dense vector embeddings using Hugging Face Sentence Transformers.

↓

### Step 4

Store the embeddings inside Pinecone Vector Database.

↓

### Step 5

Accept the user's medical question.

↓

### Step 6

Retrieve the Top-K most relevant document chunks using semantic similarity search.

↓

### Step 7

Combine the retrieved context with the user's question using a prompt template.

↓

### Step 8

Generate the final answer using the Groq Llama-3.3-70B Versatile model.

↓

### Step 9

Display the answer through the Gradio web interface.

---

# Project Structure

```text
Medical-RAG/
│
├── app.py
├── Medical_RAG.ipynb
├── requirements.txt
└── README.md
```

---

# Environment Variables

The application requires the following environment variables:

| Variable           | Description      |
| ------------------ | ---------------- |
| `PINECONE_API_KEY` | Pinecone API Key |
| `GROQ_API_KEY`     | Groq API Key     |

> **Note:** API keys are **not included** in this repository. For local development, use a `.env` file. For deployment on Hugging Face Spaces, add the keys under **Settings → Secrets**.

---

# Running the Application

Run the application locally:

```bash
python app.py
```

---

# Deployment

The application is deployed on Hugging Face Spaces.

**Live Demo**

https://huggingface.co/spaces/Monishram99/Medical-Chatbot

---

# Example Questions

* What is diabetes?
* What are the symptoms of asthma?
* Explain hypertension.
* What causes pneumonia?
* What is anemia?
* Explain tuberculosis.
* What are the symptoms of liver disease?
* What are the complications of obesity?

---

# Future Improvements

* Multi-document support
* Parent Document Retriever
* Hybrid Search (Dense + BM25)
* Cross-Encoder Re-ranking
* Source citations with page numbers
* Conversation memory
* Voice input and output
* Streaming responses
* Docker deployment
* User authentication

---

# Concepts Demonstrated

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Dense Retrieval
* Prompt Engineering
* Vector Databases
* Large Language Models
* Context-aware Question Answering
* LangChain Pipelines
* AI Application Deployment

---

# Libraries Used

* LangChain
* Pinecone
* Hugging Face Sentence Transformers
* Gradio
* Groq
* python-dotenv

---

# License

This project is intended for educational and learning purposes only.

---

# Author

**Monish Ram**

Computer Science Engineering Student

**Interests:** Artificial Intelligence • Machine Learning • Deep Learning • Generative AI • Large Language Models • Retrieval-Augmented Generation

