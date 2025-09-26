import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Access API key
API_KEY = os.getenv("API_KEY")