
# 🧠 Mental Health Support Chatbot 💙

A **RAG-powered** (Retrieval-Augmented Generation) mental health support chatbot with a beautiful Gradio web interface. It provides empathetic, context-aware responses grounded in mental health literature using NVIDIA's Llama 3.1 70B model.

🔗 **[Try it live on Hugging Face Spaces](https://huggingface.co/spaces/chandrakant2311/mental-health-chatbot)**

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Gradio](https://img.shields.io/badge/Gradio-5.x-orange?logo=gradio)
![NVIDIA](https://img.shields.io/badge/NVIDIA-NIM%20API-76b900?logo=nvidia)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- 🤖 **RAG Pipeline** — Answers grounded in a mental health knowledge base (PDF documents)
- 🧠 **NVIDIA NIM API** — Powered by Meta Llama 3.1 70B Instruct model
- 💬 **Gradio Web UI** — Clean, themed chat interface with example questions
- 🛡️ **Safety Guardrails** — Crisis resource referrals, professional help encouragement
- 🔍 **Semantic Search** — ChromaDB + Sentence Transformers for intelligent retrieval
- ⚡ **Eager Loading** — Model initializes at startup for instant responses

## 🏗️ Architecture

```
User Question
      ↓
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Gradio UI  │ ──→ │   LangChain  │ ──→ │  NVIDIA NIM │
│  (app.py)   │     │  RAG Chain   │     │  Llama 3.1  │
└─────────────┘     └──────┬───────┘     └─────────────┘
                           │
                    ┌──────┴───────┐
                    │   ChromaDB   │
                    │ Vector Store │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │  PDF Docs    │
                    │ (Knowledge)  │
                    └──────────────┘
```

## 📁 Project Structure

```
chatbot/
├── app.py                 # Gradio web frontend (entry point)
├── main.py                # RAG backend (LLM + ChromaDB + QA chain)
├── data/
│   └── mental_health_Document.pdf    # Knowledge base source
├── chroma_db/             # Auto-generated vector database
├── requirements.txt       # Python dependencies
├── .env                   # API keys (not committed)
├── .env.example           # API key template
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | Meta Llama 3.1 70B Instruct via NVIDIA NIM |
| **Framework** | LangChain |
| **Vector Database** | ChromaDB |
| **Embeddings** | Sentence Transformers (all-MiniLM-L6-v2) |
| **Frontend** | Gradio 5.x |
| **PDF Parsing** | PyPDF |
| **Deployment** | Hugging Face Spaces |

---

## 🚀 Quick Start (Local)

### Prerequisites

- Python 3.8 or higher
- A free NVIDIA NIM API key from [build.nvidia.com](https://build.nvidia.com)

### 1. Clone the Repository

```bash
git clone https://github.com/chandrakant1212/mental-health-chatbot.git
cd mental-health-chatbot
```

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

Get a free API key from [build.nvidia.com](https://build.nvidia.com) → search for **Meta Llama 3.1 70B Instruct** → click **Get API Key**.

**Option A — Environment variable:**

```bash
# Windows PowerShell
$env:NVIDIA_API_KEY = "nvapi-your-key-here"

# macOS/Linux
export NVIDIA_API_KEY="nvapi-your-key-here"
```

**Option B — `.env` file:**

```bash
cp .env.example .env
# Edit .env and paste your key
```

### 5. Run the Chatbot

```bash
python app.py
```

Open **http://127.0.0.1:7860** in your browser.

> 📝 **First run** takes 1-2 minutes to build the vector database from the PDF. Subsequent runs load the cached database instantly.

### CLI Mode (Optional)

```bash
python main.py
```

---

## 🔧 Customization

### Change the LLM Model

Edit `main.py` → `initialize_llm()`:

```python
llm = ChatNVIDIA(
    model="meta/llama-3.1-8b-instruct",  # Smaller, faster model
    ...
)
```

### Add More Knowledge

Drop additional PDF files into the `data/` folder and delete `chroma_db/` to rebuild:

```bash
# Windows
Remove-Item -Recurse chroma_db

# macOS/Linux
rm -rf chroma_db
```

### Modify the Prompt

Edit the `MENTAL_HEALTH_PROMPT` in `main.py` to customize the chatbot's personality and safety guidelines.

---

## ⚠️ Disclaimer

> This chatbot is for **informational and supportive purposes only**. It is **NOT a substitute** for professional mental health care. If you are in crisis, please contact:
>
> - 🇺🇸 **988 Suicide & Crisis Lifeline** (US): Call or text **988**
> - 🇮🇳 **AASRA** (India): **9820466726**
> - 🇮🇳 **iCall** (India): **9152987821**
> - 🌍 **Crisis Text Line**: Text HOME to **741741**

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

Made with 💙 by [Chandrakant](https://github.com/chandrakant1212)
