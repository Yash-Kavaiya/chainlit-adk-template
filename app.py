import chainlit as cl
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global agent variable
agent = None

@cl.on_chat_start
async def start():
    """Initialize the chat session"""
    global agent
    
    try:
        # Try to initialize Google ADK agent
        from google_agent import SimpleGoogleAgent
        agent = SimpleGoogleAgent()
        
        await cl.Message(
            content="🤖 Hello! I'm your Google ADK-powered assistant. How can I help you today?"
        ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"⚠️  Google ADK initialization failed: {str(e)}\n\nPlease make sure you have:\n1. Set GOOGLE_API_KEY in your .env file\n2. Installed google-adk package\n\nI'll work in fallback mode for now."
        ).send()

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming messages"""
    global agent
    
    try:
        if agent:
            # Process message through Google ADK agent
            response = await agent.process_message(message.content)
            await cl.Message(content=response).send()
        else:
            # Fallback mode
            await cl.Message(
                content=f"🔄 **Fallback Mode Response**\n\nYou said: *{message.content}*\n\nI'm running in fallback mode since Google ADK isn't properly configured. Please check your .env file and API key setup."
            ).send()
        
    except Exception as e:
        await cl.Message(
            content=f"❌ Error: {str(e)}\n\nPlease check your configuration and try again."
        ).send()

if __name__ == "__main__":
    import chainlit.cli
    chainlit.cli.main(["run", __file__])