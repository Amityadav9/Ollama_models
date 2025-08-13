import gradio as gr
import requests
import os
from dotenv import load_dotenv
import traceback

# Load environment variables
load_dotenv()

# Ollama configuration
DEFAULT_OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://")
MODEL_NAME = "gpt-oss:20b"


# Test Ollama connection
def test_ollama_connection():
    try:
        response = requests.get(f"{DEFAULT_OLLAMA_HOST}/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get("models", [])
            model_names = [m.get("name", "") for m in models]
            if any(MODEL_NAME in name for name in model_names):
                return True, f"✅ Connected to Ollama! Found {MODEL_NAME}"
            else:
                return (
                    False,
                    f"❌ Model {MODEL_NAME} not found. Available: {model_names}",
                )
        else:
            return False, f"❌ Ollama server error: HTTP {response.status_code}"
    except Exception as e:
        return False, f"❌ Connection failed: {str(e)}"


# Initialize connection
connection_status, connection_message = test_ollama_connection()
print(connection_message)


# Define the chat function using Ollama
def chat(message, history):
    if not connection_status:
        return f"❌ Ollama connection failed: {connection_message}"

    try:
        # Format the conversation history for the model
        conversation = []
        for user_msg, assistant_msg in history:
            conversation.append(f"User: {user_msg}")
            conversation.append(f"Assistant: {assistant_msg}")

        # Add the current user message
        conversation.append(f"User: {message}")
        conversation.append("Assistant:")

        # Create the prompt
        prompt = "\n".join(conversation)

        # Call Ollama API
        response = requests.post(
            f"{DEFAULT_OLLAMA_HOST}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.7, "top_p": 0.9, "max_tokens": 256},
            },
            timeout=30,
        )

        if response.status_code == 200:
            result = response.json()
            return result.get("response", "No response generated")
        else:
            return f"❌ Ollama API error: HTTP {response.status_code}"

    except Exception as e:
        error_msg = f"Error generating response: {str(e)}"
        print(error_msg)
        print("Traceback:")
        traceback.print_exc()
        return f"Sorry, I encountered an error while processing your request: {str(e)}"


# Create the Gradio chat interface using ChatInterface
demo = gr.ChatInterface(
    fn=chat,
    type="messages",
    examples=[
        "Hello! How are you?",
        "Tell me about real estate investing",
        "What's the weather like?",
        "Explain quantum computing in simple terms",
    ],
    title="🤖 GPT-OSS-20B Chatbot via Ollama",
    description=f"""
    A chatbot powered by OpenAI's GPT-OSS-20B model running locally via Ollama.
    
    🔗 **Connection Status**: {connection_message}
    🖥️ **Ollama Host**: {DEFAULT_OLLAMA_HOST}
    🤖 **Model**: {MODEL_NAME}
    
    **Features:**
    - ✅ 100% Local Processing (No data sent to external servers)
    - ✅ OpenAI's first open-source model in ~5 years
    - ✅ Privacy-focused chat interface
    """,
)

# Launch the interface
if __name__ == "__main__":
    demo.launch()
