from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os

load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")


llm = init_chat_model(model="gpt-5-nano", temperature=0)

response = llm.stream("Tell me a short story about 100 words.")

for chunk in response:
    print(chunk.content, end="", flush=True)