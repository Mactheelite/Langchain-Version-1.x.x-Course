from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

llm = init_chat_model(model="gpt-5-nano", temperature=0)

response = llm.stream("Tell me a short story about 50 words.")

for chunk in response:
    print(chunk.content, end="", flush=True)