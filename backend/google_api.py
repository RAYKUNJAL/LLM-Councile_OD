"""Google Generative AI API client."""

import os
import google.generativeai as genai
from typing import List, Dict, Any, Optional
from .config import GOOGLE_API_KEY

# Configure the library
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

async def generate_response(
    model_name: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.7,
    max_tokens: Optional[int] = None
) -> str:
    """
    Generate a response using Google's Generative AI API.
    
    Args:
        model_name: Name of the model (e.g., "gemini-1.5-flash")
        messages: List of message dicts with 'role' and 'content'
        temperature: Sampling temperature
        max_tokens: Maximum output tokens
        
    Returns:
        Generated text response
    """
    if not GOOGLE_API_KEY:
        return "Error: GOOGLE_API_KEY not set in .env file."

    try:
        # Convert standard messages format to Gemini format
        # Gemini uses 'user' and 'model' roles, and history list
        history = []
        last_user_message = ""
        
        for msg in messages:
            role = "user" if msg["role"] == "user" else "model"
            content = msg["content"]
            
            # If it's the last message and it's from user, save it for generate_content
            if msg == messages[-1] and role == "user":
                last_user_message = content
            else:
                history.append({"role": role, "parts": [content]})

        # Initialize model
        model = genai.GenerativeModel(model_name)
        
        # Start chat with history
        chat = model.start_chat(history=history)
        
        # Generate response
        response = await chat.send_message_async(
            last_user_message,
            generation_config=genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens
            )
        )
        
        return response.text
        
    except Exception as e:
        print(f"Error calling Google API ({model_name}): {str(e)}")
        return f"Error: {str(e)}"
