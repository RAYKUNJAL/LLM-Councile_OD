"""Configuration for the LLM Council."""

import os
from dotenv import load_dotenv

load_dotenv()

# OpenRouter API key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Council members - list of OpenRouter model identifiers
# Council members - list of OpenRouter model identifiers
# Google API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
# Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# HuggingFace API key
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Council members - list of model identifiers with provider prefixes
COUNCIL_MODELS = [
    "google/gemini-2.0-flash-exp",
    "groq/llama3-70b-8192",
    "groq/mixtral-8x7b-32768",
    "hf/meta-llama/Meta-Llama-3-8B-Instruct",
]

# Chairman model - synthesizes final response
CHAIRMAN_MODEL = "google/gemini-flash-latest"

# OpenRouter API endpoint (Legacy/Unused)
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Data directory for conversation storage
DATA_DIR = "data/conversations"
