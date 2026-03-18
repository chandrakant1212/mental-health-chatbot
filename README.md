---
title: Mental Health Chatbot
emoji: 🧠
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 5.34.2
app_file: app.py
pinned: false
license: mit
---

# 🧠 Mental Health Support Chatbot 💙

A **RAG-powered** (Retrieval-Augmented Generation) mental health support chatbot with a beautiful Gradio web interface. It provides empathetic, context-aware responses grounded in mental health literature using NVIDIA's Llama 3.1 70B model.

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

## ☁️ Deploy to Hugging Face Spaces (Free)

### Step 1: Create a Hugging Face Account

Sign up at [huggingface.co](https://huggingface.co) if you haven't already.

### Step 2: Create a New Space

1. Go to [huggingface.co/new-space](https://huggingface.co/new-space)
2. Fill in:
   - **Space name:** `mental-health-chatbot`
   - **SDK:** Select **Gradio**
   - **Visibility:** Public or Private
3. Click **Create Space**

### Step 3: Add Your API Key as a Secret

1. Go to your Space → **Settings** → **Variables and Secrets**
2. Click **New Secret**
3. Name: `NVIDIA_API_KEY`
4. Value: Your NVIDIA API key (e.g., `nvapi-...`)
5. Click **Save**

### Step 4: Push Your Code

```bash
# Set remote with your HF token for authentication
git remote set-url hf https://YOUR_HF_USERNAME:YOUR_HF_TOKEN@huggingface.co/spaces/YOUR_USERNAME/mental-health-chatbot

# Push to HuggingFace
git add .
git commit -m "Deploy mental health chatbot to HF Spaces"
git push hf main --force
```

> Replace `YOUR_HF_USERNAME` and `YOUR_HF_TOKEN` with your Hugging Face username and access token.

### Step 5: Wait for Build

Hugging Face will automatically:
- Install your `requirements.txt`
- Run `app.py`
- Build the ChromaDB from your PDF on first run
- Make your chatbot live at `https://huggingface.co/spaces/YOUR_USERNAME/mental-health-chatbot`

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | Meta Llama 3.1 70B Instruct via NVIDIA NIM |
| **Framework** | LangChain |
| **Vector Database** | ChromaDB |
| **Embeddings** | Sentence Transformers (all-MiniLM-L6-v2) |
| **Frontend** | Gradio 5.x |
| **PDF Parsing** | PyPDF |

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
