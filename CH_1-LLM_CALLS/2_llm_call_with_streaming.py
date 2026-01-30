from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

response = llm.stream("Tell me a short story about 100 words.")

for chunk in response:
    print(chunk.content, end="", flush=True)