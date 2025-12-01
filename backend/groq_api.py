"""Groq API client."""

import os
from groq import Groq
from typing import List, Dict, Any, Optional
from .config import GROQ_API_KEY

# Initialize client
client = None
if GROQ_API_KEY:
    client = Groq(api_key=GROQ_API_KEY)

async def generate_response(
    model_name: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.7,
    max_tokens: Optional[int] = None
) -> str:
    """
    Generate a response using Groq API.
    
    Args:
        model_name: Name of the model (e.g., "llama3-70b-8192")
        messages: List of message dicts with 'role' and 'content'
        temperature: Sampling temperature
        max_tokens: Maximum output tokens
        
    Returns:
        Generated text response
    """
    if not GROQ_API_KEY or not client:
        return "Error: GROQ_API_KEY not set in .env file."

    try:
        # Remove 'groq/' prefix if present
        clean_model_name = model_name.replace("groq/", "")
        
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=clean_model_name,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        
        return chat_completion.choices[0].message.content
        
    except Exception as e:
        print(f"Error calling Groq API ({model_name}): {str(e)}")
        return f"Error: {str(e)}"
