from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv() # Load environment variables from .env file

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.") # Check if API key is available


llm = ChatOpenAI(model="gpt-5-nano", temperature=0) # The best way to create an LLM instance

response = llm.invoke("Hello, how are you?")

print(response.content)