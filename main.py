"""
Mental Health Chatbot — RAG Backend
Uses NVIDIA NIM API + LangChain + ChromaDB to answer mental health questions
from a knowledge base (PDF documents).
"""

import os
import sys

# Prevent transformers from trying to load TensorFlow/Keras
os.environ["TRANSFORMERS_NO_TF"] = "1"
os.environ["USE_TORCH"] = "1"
from dotenv import load_dotenv
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load .env file if it exists
load_dotenv()

# Paths (relative to project root)
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CHROMA_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Mental health prompt with safety guardrails
MENTAL_HEALTH_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""You are a compassionate and knowledgeable mental health support assistant. 
Your role is to provide empathetic, helpful, and evidence-based responses using the provided context.

IMPORTANT GUIDELINES:
- Be warm, empathetic, and non-judgmental in every response.
- Use the provided context to give accurate, grounded answers.
- If the user expresses suicidal thoughts or self-harm, ALWAYS include crisis resources:
  * National Suicide Prevention Lifeline: 988 (US)
  * Crisis Text Line: Text HOME to 741741
  * AASRA (India): 9820466726
  * iCall (India): 9152987821
- Clearly state that you are an AI assistant, NOT a licensed therapist.
- Encourage professional help when the situation seems beyond general advice.
- Never diagnose conditions — suggest the user consult a professional.
- If you don't know the answer or the context doesn't cover it, say so honestly.

Context from knowledge base:
{context}

User's question: {question}

Supportive response:"""
)


def get_embeddings():
    """Initialize the embedding model."""
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)


def initialize_llm():
    """Initialize the NVIDIA NIM LLM."""
    api_key = os.getenv("NVIDIA_API_KEY")
    if not api_key:
        print("ERROR: NVIDIA_API_KEY not found!")
        print("Set it with: $env:NVIDIA_API_KEY = 'nvapi-your-key-here'")
        print("Or create a .env file (see .env.example)")
        sys.exit(1)

    llm = ChatNVIDIA(
        model="meta/llama-3.1-70b-instruct",
        api_key=api_key,
        base_url="https://integrate.api.nvidia.com/v1",
        temperature=0.3,
        max_tokens=1024,
    )
    return llm


def create_vector_db():
    """Load PDFs from data/ folder, split into chunks, and store in ChromaDB."""
    if not os.path.exists(DATA_DIR):
        print(f"ERROR: Data directory not found: {DATA_DIR}")
        sys.exit(1)

    print("Loading PDF documents...", flush=True)
    loader = DirectoryLoader(DATA_DIR, glob="*.pdf", loader_cls=PyPDFLoader)
    
    try:
        documents = loader.load()
    except Exception as e:
        print(f"ERROR: Failed to load PDFs: {e}")
        sys.exit(1)

    if not documents:
        print("ERROR: No PDF documents found in data/ folder.")
        sys.exit(1)

    print(f"Loaded {len(documents)} pages from PDFs.", flush=True)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} text chunks.")

    print("Creating embeddings and building vector database...", flush=True)
    embeddings = get_embeddings()
    vector_db = Chroma.from_documents(
        texts,
        embeddings,
        persist_directory=CHROMA_DIR,
    )
    print("ChromaDB created and saved successfully!", flush=True)
    return vector_db


def load_vector_db():
    """Load an existing ChromaDB from disk."""
    embeddings = get_embeddings()
    vector_db = Chroma(
        persist_directory=CHROMA_DIR,
        embedding_function=embeddings,
    )
    return vector_db


def setup_qa_chain(vector_db, llm):
    """Create the RetrievalQA chain with the mental health prompt."""
    retriever = vector_db.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": MENTAL_HEALTH_PROMPT},
    )
    return qa_chain


def initialize_chatbot():
    """Full initialization: LLM + Vector DB + QA Chain. Returns the QA chain."""
    print("Initializing Mental Health ChatBot...", flush=True)

    llm = initialize_llm()

    if os.path.exists(CHROMA_DIR) and os.listdir(CHROMA_DIR):
        print("Loading existing knowledge base...", flush=True)
        vector_db = load_vector_db()
    else:
        print("Building knowledge base from PDFs (first run)...", flush=True)
        vector_db = create_vector_db()

    qa_chain = setup_qa_chain(vector_db, llm)
    print("ChatBot ready!\n", flush=True)
    return qa_chain


def get_response(question, chat_history=None):
    """
    Get a response from the chatbot.
    This is the main entry point used by the Gradio frontend.
    
    Args:
        question: The user's question string
        chat_history: Optional list of (user_msg, bot_msg) tuples (for context)
    
    Returns:
        The chatbot's response string
    """
    global _qa_chain

    # Lazy initialization
    if _qa_chain is None:
        _qa_chain = initialize_chatbot()

    try:
        result = _qa_chain.invoke({"query": question})
        return result.get("result", "I'm sorry, I couldn't generate a response. Please try again.")
    except Exception as e:
        error_msg = str(e)
        if "api_key" in error_msg.lower() or "unauthorized" in error_msg.lower():
            return "⚠️ API key error. Please check that your NVIDIA_API_KEY is set correctly."
        elif "rate" in error_msg.lower() or "limit" in error_msg.lower():
            return "⚠️ Rate limit reached. Please wait a moment and try again."
        else:
            return f"⚠️ Something went wrong: {error_msg}\nPlease try again or rephrase your question."


# Global QA chain (lazy-initialized on first call)
_qa_chain = None


# CLI mode: run directly with `python main.py`
if __name__ == "__main__":
    qa_chain = initialize_chatbot()
    _qa_chain = qa_chain

    print("=" * 50)
    print("Mental Health Support ChatBot")
    print("Type 'exit' to quit")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye! Take care of yourself. 💙")
            break

        if not user_input:
            continue
        if user_input.lower() in ("exit", "quit", "bye"):
            print("\nChatBot: Take care of yourself. Remember, it's okay to ask for help. Goodbye! 💙")
            break

        response = get_response(user_input)
        print(f"\nChatBot: {response}")
