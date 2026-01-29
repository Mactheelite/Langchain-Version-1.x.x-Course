from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")


llm = ChatOpenAI(model="gpt-4.1-nano", temperature=0)

messages = [
    SystemMessage(content="You are a helpful assistant. Give me the most recent answers. Make it short."),
    HumanMessage(content="Who is the president of Nigeria?"),
]

response = llm.invoke(messages)

print(response.content)