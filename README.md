# Mental Health Chatbot

A conversational AI chatbot designed to provide mental health support, guidance, and resources. This project leverages advanced language models and the [LangChain](https://github.com/langchain-ai/langchain) framework to enable context-aware, human-like interactions for users seeking mental wellness assistance.

## Table of Contents

- [Features](#features)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Conversational interface for mental health support
- Contextual understanding using LangChain and LLMs
- Example Jupyter notebooks for interactive experimentation
- Modular and extensible codebase for custom mental health scenarios
- Resource suggestions and wellness tips

## How It Works

This chatbot utilizes the LangChain framework to orchestrate conversations with language models (such as OpenAI's GPT or Groq's LLMs). Prompts and dialogue flows are managed to provide empathetic, helpful, and safe responses to users. The Jupyter Notebook format allows for rapid prototyping and demonstration of chatbot capabilities.

## Getting Started

These instructions will help you set up and run the chatbot locally.

### Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- Jupyter Notebook or JupyterLab

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/chandrakant1212/mental-health-chatbot.git
    cd mental-health-chatbot
    ```

2. **Create and activate a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required libraries:**

    You need to install the following libraries before running the notebook.

    ```bash
    pip install langchain_groq langchain_core langchain_community pypdf chromadb sentence-transformers torch gradio --upgrade
    ```

    Alternatively, you can install them all at once with:

    ```bash
    pip install langchain langchain-community langchain-groq chromadb sentence-transformers torch gradio pypdf --upgrade
    ```

    - `langchain`, `langchain-core`, `langchain-community`, `langchain-groq`: For managing conversation flows and integrating various language models.
    - `chromadb`: For vector storage and retrieval.
    - `sentence-transformers`: For embedding and semantic search.
    - `torch`: Required for some transformer models.
    - `gradio`: For building simple web UIs (optional, if you want a demo interface).
    - `pypdf`: For PDF parsing (if your chatbot uses document ingestion).

    **Note:** If you encounter issues with package versions, try upgrading (`--upgrade` or `-U`) or install specific versions as required by your environment.

4. **(Optional) Set up environment variables:**

    If you are using OpenAI, Groq, or another API, ensure you set your API key(s):

    ```bash
    export OPENAI_API_KEY="your-api-key-here"
    export GROQ_API_KEY="your-groq-api-key-here"
    ```

    Or create a `.env` file with:

    ```
    OPENAI_API_KEY=your-api-key-here
    GROQ_API_KEY=your-groq-api-key-here
    ```

## Usage

1. **Launch Jupyter Notebook:**

    ```bash
    jupyter notebook
    ```

2. **Open the provided notebook(s):**

    - Explore the main notebook to interact with the chatbot.
    - Run the cells step by step to initialize the model and start chatting.

3. **Customize Prompts or Chains:**

    - Modify the prompt templates, chains, or components in the notebook to tailor the chatbot to specific mental health themes or requirements.

## Customization

- **Swap Language Models:**  
  You can use different LLM providers supported by LangChain (OpenAI, Groq, HuggingFace, etc.).
- **Enhance Dialogue:**  
  Add new intents, resource links, or conversation routes for richer interactions.
- **Integrate UI:**  
  This chatbot can be adapted into web or mobile apps using frameworks like Streamlit or Gradio.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for new features, bug fixes, or improvements.

1. Fork the repository
2. Create your branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Disclaimer:**  
This chatbot is intended for informational and supportive purposes only. It is not a substitute for professional mental health care. If you are in crisis, please seek help from a qualified professional or contact emergency services.
