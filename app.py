import os
from dotenv import load_dotenv
import gradio as gr

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq

# ===========================
# Load Environment Variables
# ===========================

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ===========================
# Embedding Model
# ===========================

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# ===========================
# Connect to Existing Pinecone Index
# ===========================

index_name = "medical-chatbot"

vectorstore = PineconeVectorStore(
    index_name=index_name,
    embedding=embedding,
    pinecone_api_key=PINECONE_API_KEY
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# ===========================
# Groq LLM
# ===========================

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ===========================
# Prompt Template
# ===========================

prompt = ChatPromptTemplate.from_template(
"""
You are a medical assistant.

Answer ONLY using the provided context.

If the answer is not available in the context, reply only:

"I don't know."

Context:
{context}

Question:
{question}
"""
)

# ===========================
# RAG Function
# ===========================

def ask(question):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    messages = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(messages)

    return response.content

# ===========================
# Gradio UI
# ===========================

demo = gr.Interface(
    fn=ask,
    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask your medical question..."
    ),
    outputs=gr.Textbox(label="Answer"),
    title="🩺 Medical RAG Chatbot",
    description="Ask questions from the indexed medical textbook."
)

if __name__ == "__main__":
    demo.launch()