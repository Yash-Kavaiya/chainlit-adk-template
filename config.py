"""Configuration settings for the Chainlit + Google ADK application"""

# Chainlit configuration
CHAINLIT_CONFIG = {
    "name": "Google ADK Assistant",
    "description": "A simple AI assistant powered by Google's Agent Development Kit",
    "favicon": "🤖",
    "theme": "light",
}

# Google ADK configuration
GOOGLE_ADK_CONFIG = {
    "model_name": "gemini-1.5-flash",
    "max_tokens": 1000,
    "temperature": 0.7,
}

# System prompts
SYSTEM_PROMPTS = {
    "default": """You are a helpful AI assistant powered by Google's Agent Development Kit (ADK).
    You can assist with a wide variety of tasks including:
    - Answering questions
    - Providing explanations
    - Helping with problem-solving
    - Creative tasks
    
    Be helpful, accurate, and concise in your responses."""
}