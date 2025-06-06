import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Read the OpenAI key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set. Please add it to your .env file.")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
