from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

if os.environ.get("OPENAI_API_KEY") is None:
    raise ValueError("OPENAI_API_KEY environment variable not set.")


llm = ChatOpenAI(model="gpt-5-nano", temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Give me the most recent answers. Make it short."),
    ("human", "Tell me a joke about {topic}.")
    ])

formated_prompt = prompt_template.invoke({"topic": "computers"})


response = llm.invoke(formated_prompt)

print(response.content)