
# Text prompts
# Text prompts are strings - ideal for straightforward generation tasks 
# where you don’t need to retain conversation history.

# Use text prompts when:
# ~ You have a single, standalone request
# ~ You don’t need conversation history
# ~ You want minimal code complexity

from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

llm = init_chat_model(model="gpt-5-nano")

response = llm.invoke("Write a short story about 'orange' in 25 words.")  # Returns AIMessage
print(response.content)