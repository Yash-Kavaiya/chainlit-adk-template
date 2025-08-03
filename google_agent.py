import os
import asyncio

try:
    from google.adk.agents import Agent
    ADK_AVAILABLE = True
except ImportError as e:
    print(f"Google ADK not available: {e}")
    ADK_AVAILABLE = False

class SimpleGoogleAgent:
    """Simple Google ADK agent wrapper for Chainlit integration"""
    
    def __init__(self):
        """Initialize the Google ADK agent"""
        self.api_key = os.getenv("GOOGLE_API_KEY")
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        
        if self.api_key == "your_google_ai_studio_api_key_here":
            raise ValueError("Please replace the placeholder API key with your actual Google AI Studio API key")
        
        self.use_adk = False
        self.agent = None
        self.genai_model = None
        
        # Initialize ADK agent
        if ADK_AVAILABLE:
            try:
                # Create ADK agent using the correct pattern
                self.agent = Agent(
                    name="chainlit_assistant",
                    model="gemini-2.0-flash",
                    description="A helpful AI assistant integrated with Chainlit",
                    instruction="""You are a helpful AI assistant powered by Google's ADK.
                    You can answer questions, help with tasks, and provide information on various topics.
                    Be concise, helpful, and friendly in your responses."""
                )
                self.use_adk = True
            except Exception as e:
                raise RuntimeError(f"ADK initialization failed: {e}")
        else:
            raise ImportError("Google ADK is not available")
    
    async def process_message(self, message: str) -> str:
        """Process a message through Google ADK"""
        try:
            if self.use_adk and self.agent:
                response_parts = []
                async for response_chunk in self.agent.run_async(message):
                    # Extract content from different possible response formats
                    if hasattr(response_chunk, 'content'):
                        content = response_chunk.content
                    elif hasattr(response_chunk, 'text'):
                        content = response_chunk.text
                    elif hasattr(response_chunk, 'output'):
                        content = response_chunk.output
                    elif isinstance(response_chunk, str):
                        content = response_chunk
                    else:
                        content = str(response_chunk)
                    
                    if content and content.strip():
                        response_parts.append(content)
                
                if response_parts:
                    full_response = ''.join(response_parts).strip()
                    return full_response if full_response else response_parts[-1]
                else:
                    return "I'm sorry, I didn't receive a response from the ADK model."
            else:
                return "No ADK agent available for processing"
                
        except Exception as e:
            return f"Error processing your message: {str(e)}"
    
    def process_message_sync(self, message: str) -> str:
        """Synchronous wrapper for message processing"""
        return asyncio.run(self.process_message(message))