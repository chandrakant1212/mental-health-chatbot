"""
Mental Health Chatbot — Gradio Frontend
A beautiful, connected UI for the mental health RAG chatbot.
"""

import gradio as gr
from main import get_response, initialize_chatbot, _qa_chain
import main


def respond(message, history):
    """Handle user messages and return chatbot responses."""
    if not message.strip():
        return ""
    response = get_response(message, chat_history=history)
    return response


# Eagerly initialize at startup so first message is fast
print("=" * 50, flush=True)
print("Starting Mental Health Chatbot...", flush=True)
print("=" * 50, flush=True)
main._qa_chain = initialize_chatbot()


# Custom CSS for mental health theme
CUSTOM_CSS = """
.gradio-container {
    max-width: 800px !important;
    margin: auto !important;
}
.disclaimer {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px 20px;
    border-radius: 12px;
    margin-bottom: 15px;
    font-size: 14px;
    line-height: 1.6;
}
"""

DISCLAIMER = """
<div class="disclaimer">
    💙 <strong>Mental Health Support Assistant</strong><br>
    This AI chatbot provides supportive information based on mental health resources. 
    It is <strong>NOT a substitute</strong> for professional care.<br>
    🆘 <strong>Crisis?</strong> Call <strong>988</strong> (US) | <strong>AASRA: 9820466726</strong> (India) | 
    <strong>iCall: 9152987821</strong> (India)
</div>
"""

# Build the Gradio interface
with gr.Blocks(
    title="Mental Health Support Chatbot",
    theme=gr.themes.Soft(
        primary_hue="purple",
        secondary_hue="blue",
        neutral_hue="slate",
    ),
    css=CUSTOM_CSS,
) as demo:

    gr.HTML(DISCLAIMER)

    gr.ChatInterface(
        fn=respond,
        type="messages",
        title="🧠 Mental Health Support Chatbot",
        description="Ask questions about mental health, wellness strategies, coping mechanisms, and more. "
                    "Powered by AI with a knowledge base of mental health resources.",
        examples=[
            "What are some effective coping strategies for anxiety?",
            "How can I improve my sleep quality?",
            "What are the signs of depression?",
            "Can you suggest some mindfulness exercises?",
            "How do I deal with stress at work?",
        ],
    )

    gr.Markdown(
        "---\n"
        "*This chatbot uses RAG (Retrieval-Augmented Generation) to provide answers grounded in mental health literature. "
        "Always consult a qualified professional for medical advice.*"
    )


if __name__ == "__main__":
    print("Starting Mental Health Chatbot UI...", flush=True)
    print("Open http://127.0.0.1:7860 in your browser\n", flush=True)
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
    )
