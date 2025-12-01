"""HuggingFace Inference API client."""

import os
from huggingface_hub import InferenceClient
from typing import List, Dict, Any, Optional
from .config import HUGGINGFACE_API_KEY

# Initialize client
client = None
if HUGGINGFACE_API_KEY:
    client = InferenceClient(token=HUGGINGFACE_API_KEY)

async def generate_response(
    model_name: str,
    messages: List[Dict[str, str]],
    temperature: float = 0.7,
    max_tokens: Optional[int] = None
) -> str:
    """
    Generate a response using HuggingFace Inference API.
    
    Args:
        model_name: Name of the model (e.g., "meta-llama/Meta-Llama-3-8B-Instruct")
        messages: List of message dicts with 'role' and 'content'
        temperature: Sampling temperature
        max_tokens: Maximum output tokens
        
    Returns:
        Generated text response
    """
    if not HUGGINGFACE_API_KEY or not client:
        return "Error: HUGGINGFACE_API_KEY not set in .env file."

    try:
        # Remove 'hf/' prefix if present
        clean_model_name = model_name.replace("hf/", "")
        
        # HuggingFace Inference API uses chat_completion for supported models
        response = client.chat_completion(
            messages=messages,
            model=clean_model_name,
            temperature=temperature,
            max_tokens=max_tokens or 1024, # HF often requires explicit max_tokens
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"Error calling HuggingFace API ({model_name}): {str(e)}")
        return f"Error: {str(e)}"
